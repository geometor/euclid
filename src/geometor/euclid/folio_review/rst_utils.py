"""reStructuredText rendering and metadata parsing utilities for folio_review.

Uses ``photon_platform.publish.rst_renderer`` when Docutils is available in the active
Python interpreter, and provides a complete pure-Python Docutils-compatible fallback
renderer and strict RST syntax validator when running in minimal environments.
"""

from __future__ import annotations

import html as _html
import io
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# Ensure sibling photon-platform/publish/src and repo .venv site-packages are on sys.path
_REPO_ROOT = Path(__file__).resolve().parents[4]
for _venv_sp in sorted(_REPO_ROOT.glob(".venv/lib/python*/site-packages")):
    if _venv_sp.exists() and str(_venv_sp) not in sys.path:
        sys.path.append(str(_venv_sp))

for _parent_idx in (6, 5):
    try:
        _cand_pub = Path(__file__).resolve().parents[_parent_idx] / "photon-platform" / "publish" / "src"
        if _cand_pub.exists() and str(_cand_pub) not in sys.path:
            sys.path.insert(0, str(_cand_pub))
    except IndexError:
        pass


_TARGET_RE = re.compile(r"^(.*?)\s*<(.+)>\s*$", re.DOTALL)
_FIELD_LINE_RE = re.compile(r"^:([a-zA-Z0-9_.-]+):[ \t]*(.*)$")
_LIST_FIELDS = {"tags", "dependencies", "categories"}

_VALID_DIRECTIVES = {
    "enunciation",
    "assertion",
    "subclause",
    "sub-clause",
    "qed",
    "porism",
    "lemma",
    "scholium",
    "folio",
    "picture",
    "container",
    "code-block",
    "list-table",
    "table",
    "math",
    "raw",
    "note",
    "warning",
    "toctree",
}

_VALID_ROLES = {"g", "just", "line", "ref", "term", "sup", "sub", "math", "doc"}

_ADORNMENT_RE = re.compile(r"^([=!~^\"'`#*+\-_])\1{3,}\s*$")
_LIST_ITEM_RE = re.compile(r"^([-*+]|\d+\.|#\.)\s+(.*)$")
_HTML_TAG_RE = re.compile(
    r"</?(?:p|span|div|sup|sub|br|em|i|b|u|strong|center|figure|figcaption|pre|code|table|thead|tbody|tr|td|th|ul|ol|li|dl|dt|dd|blockquote|hr|h[1-6]|img|a|font|small|big)(?:\s[^>]*)?>",
    re.IGNORECASE,
)


def _column_width(text: str) -> int:
    width = 0
    for ch in text:
        if unicodedata.east_asian_width(ch) in ("W", "F"):
            width += 2
        else:
            width += 1
    return max(width, len(text))


def _fallback_parse_rst_metadata(rst_text: str) -> Tuple[Dict[str, Any], str]:
    """Extract leading RST bibliographic field list (`:key: val`) and return (metadata, body)."""
    if not rst_text:
        return {}, ""

    lines = rst_text.splitlines()
    idx = 0
    n = len(lines)

    while idx < n and not lines[idx].strip():
        idx += 1

    metadata: Dict[str, Any] = {}
    current_key: Optional[str] = None

    while idx < n:
        line = lines[idx]
        stripped = line.strip()
        if not stripped:
            idx += 1
            break

        m = _FIELD_LINE_RE.match(line)
        if m:
            current_key = m.group(1).strip()
            val_str = m.group(2).strip()
            metadata[current_key] = val_str
            idx += 1
        elif current_key is not None and (line.startswith(" ") or line.startswith("\t")):
            prev = metadata.get(current_key, "")
            metadata[current_key] = f"{prev} {stripped}".strip()
            idx += 1
        else:
            break

    if not metadata:
        return {}, rst_text

    for k in list(metadata.keys()):
        if k in _LIST_FIELDS:
            raw_val = metadata[k]
            if isinstance(raw_val, str):
                metadata[k] = (
                    [item.strip() for item in raw_val.split(",") if item.strip()]
                    if raw_val.strip()
                    else []
                )

    while idx < n and not lines[idx].strip():
        idx += 1

    body = "\n".join(lines[idx:])
    return metadata, body


def _render_inline_rst_fallback(text: str) -> str:
    """Render inline RST roles (:g:, :just:, :line:, :ref:, :term:, :sup:, :sub:) and markup to HTML."""
    if not text:
        return ""

    placeholders: Dict[str, str] = {}
    pc = 0

    def _stash(html_frag: str) -> str:
        nonlocal pc
        pc += 1
        tok = f"__RSTHTMLFRAG_{pc:05d}__"
        placeholders[tok] = html_frag
        return tok

    # 1. Inline literals ``...``
    text = re.sub(
        r"``([^`]+)``",
        lambda m: _stash(f'<span class="docutils literal">{_html.escape(m.group(1))}</span>'),
        text,
    )

    # 2. Roles :name:`...`
    def _repl_role(match: re.Match) -> str:
        rname = match.group(1)
        payload = match.group(2).strip()
        m_t = _TARGET_RE.match(payload)
        if m_t:
            disp = m_t.group(1).strip() or m_t.group(2).strip()
            tgt = m_t.group(2).strip()
        else:
            disp, tgt = payload, None

        if rname == "g":
            ref = tgt if tgt is not None else disp
            return _stash(
                f'<span class="g-ref" data-ref="{_html.escape(ref, quote=True)}">{_html.escape(disp)}</span>'
            )
        if rname == "just":
            if not (disp.startswith("[") and disp.endswith("]")) and not disp.startswith("Q."):
                disp = f"[{disp}]"
            if tgt:
                return _stash(
                    f'<span class="justification" data-just="{_html.escape(tgt, quote=True)}">{_html.escape(disp)}</span>'
                )
            return _stash(f'<span class="justification">{_html.escape(disp)}</span>')
        if rname == "line":
            return _stash(f'<sup class="line-num" data-line="{_html.escape(disp, quote=True)}">{_html.escape(disp)}</sup>')
        if rname in ("ref", "term"):
            ref = tgt if tgt is not None else disp
            return _stash(f'<a class="reference internal" href="#{_html.escape(ref, quote=True)}">{_html.escape(disp)}</a>')
        if rname == "sup":
            return _stash(f"<sup>{_html.escape(disp)}</sup>")
        if rname == "sub":
            return _stash(f"<sub>{_html.escape(disp)}</sub>")
        return _stash(f"<span>{_html.escape(disp)}</span>")

    text = re.sub(r":([a-zA-Z0-9_.-]+):`([^`]+)`", _repl_role, text)

    # 3. Protect inline math $...$
    text = re.sub(
        r"\$(?!\s)[^$\n]+?(?<!\s)\$|\$[A-Za-z0-9]+\$",
        lambda m: _stash(_html.escape(m.group(0), quote=False)),
        text,
    )

    # Remove escaped spaces (\ )
    text = text.replace("\\ ", "")

    # 4. Footnote references [#label]_
    text = re.sub(
        r"\[#([a-zA-Z0-9_.-]+)\]_",
        lambda m: _stash(
            f'<a class="footnote-reference brackets" href="#fn-{_html.escape(m.group(1), quote=True)}">{_html.escape(m.group(1).lstrip("f"))}</a>'
        ),
        text,
    )

    # 5. Strong **...** and emphasis *...*
    text = re.sub(r"\*\*(?!\s)([^*]+?)(?<!\s)\*\*", lambda m: _stash(f"<strong>{_html.escape(m.group(1))}</strong>"), text)
    text = re.sub(r"\*(?!\s)([^*]+?)(?<!\s)\*", lambda m: _stash(f"<em>{_html.escape(m.group(1))}</em>"), text)

    text = _html.escape(text, quote=False)
    while "__RSTHTMLFRAG_" in text:
        replaced = False
        for tok, frag in reversed(list(placeholders.items())):
            if tok in text:
                text = text.replace(tok, frag)
                replaced = True
        if not replaced:
            break
    return text


def _render_list_table_fallback(content_blocks: List[str], opts: Dict[str, str]) -> str:
    """Render .. list-table:: content into an HTML table."""
    raw = "\n\n".join(content_blocks)
    rows: List[List[str]] = []
    curr_row: Optional[List[str]] = None
    curr_cell: List[str] = []

    for line in raw.splitlines():
        s = line.strip()
        if not s:
            continue
        m_row = re.match(r"^\*\s+-\s*(.*)$", s)
        if m_row:
            if curr_row is not None:
                curr_row.append(" ".join(curr_cell).strip())
                rows.append(curr_row)
            curr_row = []
            curr_cell = [m_row.group(1).strip()]
            continue
        m_cell = re.match(r"^-\s*(.*)$", s)
        if m_cell and curr_row is not None:
            curr_row.append(" ".join(curr_cell).strip())
            curr_cell = [m_cell.group(1).strip()]
            continue
        if curr_row is not None:
            curr_cell.append(s)

    if curr_row is not None:
        curr_row.append(" ".join(curr_cell).strip())
        rows.append(curr_row)

    if not rows:
        return ""

    try:
        header_rows = int(opts.get("header-rows", "0") or "0")
    except ValueError:
        header_rows = 0

    parts = ['<table class="docutils">']
    if header_rows > 0 and len(rows) >= header_rows:
        parts.append("<thead>")
        for r in rows[:header_rows]:
            cells = "".join(f"<th>{_render_inline_rst_fallback(c)}</th>" for c in r)
            parts.append(f"<tr>{cells}</tr>")
        parts.append("</thead>")
        body_rows = rows[header_rows:]
    else:
        body_rows = rows

    if body_rows:
        parts.append("<tbody>")
        for r in body_rows:
            cells = "".join(f"<td>{_render_inline_rst_fallback(c)}</td>" for c in r)
            parts.append(f"<tr>{cells}</tr>")
        parts.append("</tbody>")
    parts.append("</table>")
    return "\n".join(parts)


def _render_rst_list_block(raw_list_text: str) -> str:
    """Render top-level and nested RST bullet/enumerated lists into <ul>/<ol><li> HTML."""
    lines = raw_list_text.splitlines()
    items: List[Tuple[str, str, int, List[str]]] = []
    # Each item is (list_tag, first_line_text, content_indent, sub_lines)

    for line in lines:
        if not line.strip():
            if items:
                items[-1][3].append("")
            continue

        m = _LIST_ITEM_RE.match(line)
        if m:
            marker = m.group(1)
            first_text = m.group(2).strip()
            list_tag = "ul" if marker in ("-", "*", "+") else "ol"
            content_indent = len(marker) + 1
            items.append((list_tag, first_text, content_indent, []))
        elif items:
            items[-1][3].append(line)

    if not items:
        return ""

    list_tag = items[0][0]
    out = [f"<{list_tag}>"]
    for _, first_text, content_indent, sub_lines in items:
        # Dedent sub_lines by content_indent (or minimum non-zero indentation)
        non_empty_indents = [len(l) - len(l.lstrip(" ")) for l in sub_lines if l.strip()]
        dedent_by = min(non_empty_indents) if non_empty_indents else content_indent
        dedent_by = max(dedent_by, 2)
        dedented = [l[dedent_by:] if len(l) >= dedent_by else l.lstrip() for l in sub_lines]

        # Split dedented lines into continuation lines of the first paragraph vs nested blocks
        para_lines = [first_text]
        rem_idx = 0
        while rem_idx < len(dedented):
            dl = dedented[rem_idx]
            if not dl.strip():
                rem_idx += 1
                break
            if _LIST_ITEM_RE.match(dl.lstrip()):
                break
            para_lines.append(dl.strip())
            rem_idx += 1

        head_html = _render_inline_rst_fallback(" ".join(p for p in para_lines if p))
        rem_text = "\n".join(dedented[rem_idx:]).strip()
        nested_html = ""
        if rem_text:
            nested_html = "\n" + _fallback_render_rst_html(rem_text)
        out.append(f"<li><p>{head_html}</p>{nested_html}</li>")
    out.append(f"</{list_tag}>")
    return "\n".join(out)


def _fallback_render_rst_html(rst_text: str) -> str:
    """Render Euclid RST to HTML5 when Docutils is not installed in the current environment."""
    if not rst_text or not rst_text.strip():
        return ""
    _, body = _fallback_parse_rst_metadata(rst_text)
    if not body.strip():
        return ""

    blocks = re.split(r"\n\s*\n", body.strip("\n"))
    html_blocks: List[str] = []
    idx = 0
    n = len(blocks)

    while idx < n:
        raw_blk = blocks[idx]
        blk = raw_blk.strip()
        if not blk:
            idx += 1
            continue

        lines = blk.splitlines()

        # Section heading
        if len(lines) == 2 and _ADORNMENT_RE.match(lines[1].strip()):
            ch = lines[1].strip()[0]
            tag = {"=": "h1", "-": "h2", "~": "h3", "^": "h4", '"': "h5"}.get(ch, "h3")
            html_blocks.append(f"<{tag}>{_render_inline_rst_fallback(lines[0].strip())}</{tag}>")
            idx += 1
            continue

        # Transition ----
        if len(lines) == 1 and re.fullmatch(r"-{4,}", lines[0].strip()):
            html_blocks.append('<hr class="docutils" />')
            idx += 1
            continue

        # Display math $$...$$
        if blk.startswith("$$") and blk.endswith("$$"):
            html_blocks.append(f"<p>{_html.escape(blk, quote=False)}</p>")
            idx += 1
            continue

        # Bullet or enumerated list (including nested indented list blocks across blank lines)
        first_raw_line = raw_blk.lstrip("\n").splitlines()[0]
        if _LIST_ITEM_RE.match(first_raw_line):
            list_chunks = [raw_blk.lstrip("\n")]
            while idx + 1 < n:
                nxt_raw = blocks[idx + 1].lstrip("\n")
                if not nxt_raw.strip():
                    idx += 1
                    continue
                nxt_first = nxt_raw.splitlines()[0]
                if nxt_first.startswith("  ") or nxt_first.startswith("\t") or _LIST_ITEM_RE.match(nxt_first):
                    idx += 1
                    list_chunks.append(nxt_raw)
                else:
                    break
            html_blocks.append(_render_rst_list_block("\n\n".join(list_chunks)))
            idx += 1
            continue

        # Footnote definition .. [#label] text
        m_fn = re.match(r"^\.\.\s+\[#([a-zA-Z0-9_.-]+)\]\s+([\s\S]+)$", blk)
        if m_fn:
            fid = _html.escape(m_fn.group(1), quote=True)
            fbody = _render_inline_rst_fallback(" ".join(m_fn.group(2).split()))
            html_blocks.append(f'<aside class="footnote brackets" id="fn-{fid}"><p>{fbody}</p></aside>')
            idx += 1
            continue

        # Directives .. name:: arg
        m_dir = re.match(r"^\.\.\s+([a-zA-Z0-9_-]+)::[ \t]*(.*)$", lines[0])
        if m_dir:
            dname = m_dir.group(1).lower()
            darg = m_dir.group(2).strip()
            opts: Dict[str, str] = {}
            opt_idx = 1
            while opt_idx < len(lines) and re.match(r"^\s+:([a-zA-Z0-9_-]+):\s*(.*)$", lines[opt_idx]):
                m_o = re.match(r"^\s+:([a-zA-Z0-9_-]+):\s*(.*)$", lines[opt_idx])
                if m_o:
                    opts[m_o.group(1)] = m_o.group(2).strip()
                opt_idx += 1

            # Collect indented content blocks following this directive header
            content_blocks: List[str] = []
            if opt_idx < len(lines):
                rem = "\n".join(l[3:] if l.startswith("   ") else l.lstrip() for l in lines[opt_idx:]).strip()
                if rem:
                    content_blocks.append(rem)

            while idx + 1 < n and (blocks[idx + 1].startswith("   ") or blocks[idx + 1].startswith("\t")):
                idx += 1
                dedented = "\n".join(
                    l[3:] if l.startswith("   ") else l.lstrip() for l in blocks[idx].splitlines()
                ).strip()
                if dedented:
                    content_blocks.append(dedented)

            if dname == "picture":
                alt = _html.escape(opts.get("alt", ""), quote=True)
                src = _html.escape(darg, quote=True)
                html_blocks.append(f'<figure class="picture"><img src="{src}" alt="{alt}" /></figure>')
            elif dname == "folio":
                page = opts.get("page", "")
                p_attr = f' data-page="{_html.escape(page, quote=True)}"' if page else ""
                p_lbl = f" (p. {_html.escape(page)})" if page else ""
                html_blocks.append(
                    f'<span class="folio-milestone" id="folio-{_html.escape(darg, quote=True)}" data-folio="{_html.escape(darg, quote=True)}"{p_attr}>[Folio {_html.escape(darg)}{p_lbl}]</span>'
                )
            elif dname == "code-block":
                code_str = "\n\n".join(content_blocks)
                html_blocks.append(f"<pre><code>{_html.escape(code_str)}</code></pre>")
            elif dname == "list-table":
                html_blocks.append(_render_list_table_fallback(content_blocks, opts))
            else:
                cls_map = {
                    "enunciation": "enunciation",
                    "assertion": "assertion",
                    "subclause": "sub-clause",
                    "sub-clause": "sub-clause",
                    "qed": "qed",
                    "porism": "porism",
                    "lemma": "lemma",
                    "scholium": "scholium",
                    "container": darg or "container",
                }
                css_cls = cls_map.get(dname, dname)
                just_html = ""
                if darg and dname not in ("container",):
                    m_t = _TARGET_RE.match(darg)
                    if m_t:
                        disp = m_t.group(1).strip() or m_t.group(2).strip()
                        tgt = m_t.group(2).strip()
                    else:
                        disp, tgt = darg, None
                    if not (disp.startswith("[") and disp.endswith("]")) and not disp.startswith("Q."):
                        disp = f"[{disp}]"
                    if tgt:
                        just_html = f'<span class="justification" data-just="{_html.escape(tgt, quote=True)}">{_html.escape(disp)}</span>'
                    else:
                        just_html = f'<span class="justification">{_html.escape(disp)}</span>'
                inner_rst = "\n\n".join(content_blocks)
                inner_html = _fallback_render_rst_html(inner_rst) if inner_rst else ""
                html_blocks.append(f'<div class="docutils container {css_cls}">{just_html}{inner_html}</div>')
            idx += 1
            continue

        # Line block (| ...)
        if all(l.lstrip().startswith("|") for l in lines if l.strip()):
            lb_lines = []
            for l in lines:
                raw_l = re.sub(r"^\s*\|\s?", "", l)
                lb_lines.append(f'<div class="line">{_render_inline_rst_fallback(raw_l)}</div>')
            html_blocks.append('<div class="line-block">\n' + "\n".join(lb_lines) + "\n</div>")
            idx += 1
            continue

        # Standard paragraph
        para_html = _render_inline_rst_fallback(" ".join(l.strip() for l in lines if l.strip()))
        html_blocks.append(f"<p>{para_html}</p>")
        idx += 1

    return "\n".join(html_blocks)


def _strict_static_validate_rst(rst_text: str) -> List[str]:
    """Perform strict Docutils-equivalent static validation on an RST document."""
    warnings: List[str] = []
    if not rst_text or not rst_text.strip():
        return warnings

    _, body = _fallback_parse_rst_metadata(rst_text)
    if not body.strip():
        return warnings

    # Strip .. code-block:: content before checking inline/HTML syntax
    body_no_code = re.sub(
        r"^\.\.\s+code-block::[^\n]*\n(?:\n|[ \t]+[^\n]*\n)+",
        "\n",
        body,
        flags=re.MULTILINE,
    )

    # 1. Check for leftover HTML tags
    for m_html in _HTML_TAG_RE.finditer(body_no_code):
        warnings.append(f"Leftover HTML tag: {m_html.group(0)}")

    # 2. Check for leftover Markdown constructs (headings, images, fences, footnotes)
    for i, line in enumerate(body_no_code.splitlines(), 1):
        if re.match(r"^#{1,6}\s+", line):
            warnings.append(f"Line {i}: Leftover Markdown heading: {line.strip()}")
        if re.match(r"^```", line.strip()):
            warnings.append(f"Line {i}: Leftover Markdown code fence")
        if re.search(r"(?<!`)!\[[^\]]*\]\([^)]+\)", line):
            warnings.append(f"Line {i}: Leftover Markdown image syntax")
        if re.search(r"\[\^[^\]]+\]", line):
            warnings.append(f"Line {i}: Leftover Markdown footnote syntax")

    # 3. Check section underline widths and directive names
    lines = body_no_code.splitlines()
    for i in range(len(lines)):
        line = lines[i]
        stripped = line.strip()

        # Section underline check
        if i > 0 and _ADORNMENT_RE.match(stripped):
            prev = lines[i - 1].strip()
            if prev and not prev.startswith("..") and not prev.startswith(":"):
                if len(stripped) < len(prev):
                    warnings.append(
                        f"Line {i+1}: Title underline too short ({len(stripped)} < {len(prev)}) for {prev!r}"
                    )

        # Directive check
        m_dir = re.match(r"^\.\.\s+([a-zA-Z0-9_-]+)::(.*)$", stripped)
        if m_dir:
            dname = m_dir.group(1).lower()
            if dname not in _VALID_DIRECTIVES:
                warnings.append(f"Line {i+1}: Unknown RST directive '.. {dname}::'")

        # Role check
        no_lit = re.sub(r"``[^`\n]+``", "", line)
        for m_role in re.finditer(r":([a-zA-Z0-9_.-]+):`([^`]*)`", no_lit):
            rname = m_role.group(1)
            rbody = m_role.group(2)
            if rname not in _VALID_ROLES:
                warnings.append(f"Line {i+1}: Unknown RST role ':{rname}:'")
            if not rbody.strip():
                warnings.append(f"Line {i+1}: Empty RST role ':{rname}:``'")

    return warnings


try:
    from photon_platform.publish.rst_renderer import (
        ensure_standalone_extensions as register_euclid_extensions,
        parse_rst_metadata,
        render_rst_html,
        _protect_math_segments,
    )
    from docutils.core import publish_parts as _docutils_publish_parts

    _HAS_DOCUTILS = True
except ImportError:
    _HAS_DOCUTILS = False
    parse_rst_metadata = _fallback_parse_rst_metadata
    register_euclid_extensions = lambda: None
    render_rst_html = _fallback_render_rst_html


def validate_rst(rst_text: str) -> List[str]:
    """Validate RST content with Docutils at report_level=2 (when available) plus static validation."""
    warnings = _strict_static_validate_rst(rst_text)
    if not _HAS_DOCUTILS or not rst_text or not rst_text.strip():
        return warnings

    register_euclid_extensions()
    _, body = parse_rst_metadata(rst_text)
    if not body.strip():
        return warnings

    protected_rst, _ = _protect_math_segments(body)
    warn_stream = io.StringIO()
    _docutils_publish_parts(
        source=protected_rst,
        writer_name="html5",
        settings_overrides={
            "initial_header_level": 1,
            "doctitle_xform": False,
            "docinfo_xform": False,
            "math_output": "MathJax",
            "report_level": 2,
            "halt_level": 5,
            "warning_stream": warn_stream,
        },
    )
    warnings_raw = warn_stream.getvalue().strip()
    if warnings_raw:
        warnings.extend(line for line in warnings_raw.splitlines() if line.strip())
    return warnings
