"""Deterministic, lossless Markdown-to-reStructuredText converter for Euclid folios."""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import yaml


_STANDARD_FIELD_ORDER = [
    "folio",
    "page",
    "volume",
    "book",
    "section",
    "title",
    "canonical_id",
    "type",
    "tags",
    "dependencies",
]

_INT_TO_ROMAN = {
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX",
    "10": "X",
    "11": "XI",
    "12": "XII",
    "13": "XIII",
    "14": "XIV",
    "15": "XV",
}

_HEADING_CHARS = {
    1: "=",
    2: "-",
    3: "~",
    4: "^",
    5: '"',
    6: "+",
}

_OPENERS = set(" \t\n([{\"“‘—–-/>:")
_CLOSERS = set(" \t\n.,;:!?)]}\"”’—–-/<")


def _normalize_roman(val: Any) -> str:
    """Normalize integer or string volume/book identifiers (e.g. 8 -> VIII)."""
    s = str(val or "").strip()
    return _INT_TO_ROMAN.get(s, s)


def _column_width(text: str) -> int:
    """Compute display column width of text for Docutils section underlines."""
    width = 0
    for ch in text:
        if unicodedata.east_asian_width(ch) in ("W", "F"):
            width += 2
        else:
            width += 1
    return max(width, len(text), 4)


def _resolve_single_ref(part: str, book: str) -> Optional[str]:
    """Resolve a single Euclid citation string (without brackets) to a canonical reference ID."""
    s = part.strip()
    if not s:
        return None

    # Post. N
    m = re.match(r"^Post\.?\s*(\d+)$", s, re.IGNORECASE)
    if m:
        return f"I.post.{m.group(1)}"

    # C. N. N or C.N. N
    m = re.match(r"^C\.?\s*N\.?\s*(\d+)$", s, re.IGNORECASE)
    if m:
        return f"I.cn.{m.group(1)}"

    # Def. N
    m = re.match(r"^Def\.?\s*(\d+)$", s, re.IGNORECASE)
    if m:
        return f"{book}.def.{m.group(1)}"

    # BOOK. Def. N
    m = re.match(r"^([IVXLCDM]+)\.\s*Def\.?\s*(\d+)$", s, re.IGNORECASE)
    if m:
        return f"{m.group(1).upper()}.def.{m.group(2)}"

    # BOOK. Post. N
    m = re.match(r"^([IVXLCDM]+)\.\s*Post\.?\s*(\d+)$", s, re.IGNORECASE)
    if m:
        return f"{m.group(1).upper()}.post.{m.group(2)}"

    # BOOK. C. N. N
    m = re.match(r"^([IVXLCDM]+)\.\s*C\.?\s*N\.?\s*(\d+)$", s, re.IGNORECASE)
    if m:
        return f"{m.group(1).upper()}.cn.{m.group(2)}"

    # BOOK. N (e.g. I. 33, III. 10)
    m = re.match(r"^([IVXLCDM]+)\.\s*(\d+)$", s)
    if m:
        return f"{m.group(1)}.{m.group(2)}"

    return None


def resolve_justification_target(just_text: str, book: str = "I") -> Optional[str]:
    """Resolve a bracketed justification label (e.g. ``[Post. 3]``, ``[Def. 15]``) to canonical target(s)."""
    s = just_text.strip()
    if not (s.startswith("[") and s.endswith("]")):
        return None
    inner = s[1:-1].strip()
    if not inner:
        return None

    single = _resolve_single_ref(inner, book)
    if single:
        return single

    # Compound references separated by ';', ',', or 'and'
    parts = re.split(r"\s*(?:;|,|\band\b)\s*", inner)
    if len(parts) > 1:
        resolved = [_resolve_single_ref(p, book) for p in parts]
        if all(resolved):
            return ", ".join(r for r in resolved if r)

    return None


def format_justification(raw_just: str, book: str = "I", as_arg: bool = False) -> str:
    """Format a justification string as either a ``:just:`...``` role or a directive argument."""
    # Strip any nested <span data-ref="..."> or :g:`... <...>` inside justification text
    cleaned = re.sub(
        r"<span\b[^>]*data-ref=(['\"])(.*?)\1[^>]*>(.*?)</span>",
        r"\3",
        raw_just.strip(),
        flags=re.DOTALL,
    )
    cleaned = re.sub(r":g:`([^`<]+?)\s*<[^>]+>`", r"\1", cleaned)
    cleaned = " ".join(cleaned.split())
    target = resolve_justification_target(cleaned, book=book)
    if target:
        payload = f"{cleaned} <{target}>"
    else:
        payload = cleaned

    if as_arg:
        return payload
    return f":just:`{payload}`"


def _modernize_code_literal_html(code_str: str) -> str:
    """Modernize legacy HTML tags inside .notes.md inline code literals to RST equivalents."""
    s = code_str
    s = re.sub(r"<p\s+class=['\"]enunciation['\"]\s*>", ".. enunciation:: ", s, flags=re.IGNORECASE)
    s = re.sub(r"<p\s+class=['\"]assertion['\"]\s*>", ".. assertion:: ", s, flags=re.IGNORECASE)
    s = re.sub(r"<p\s+class=['\"]sub-clause['\"]\s*>", ".. subclause:: ", s, flags=re.IGNORECASE)
    s = re.sub(r"<p\s+class=['\"]qed['\"]\s*>", ".. qed:: ", s, flags=re.IGNORECASE)
    s = re.sub(r"<p\b[^>]*>", "", s, flags=re.IGNORECASE)
    s = re.sub(r"</p>", "", s, flags=re.IGNORECASE)
    s = re.sub(
        r"<span\s+class=['\"]justification['\"]\s*>(.*?)</span>",
        r":just:[\1]",
        s,
        flags=re.IGNORECASE | re.DOTALL,
    )
    s = re.sub(r"<span\s+class=['\"]justification['\"]\s*>", ":just:", s, flags=re.IGNORECASE)
    s = re.sub(
        r"<span\b[^>]*data-ref=(['\"])(.*?)\1[^>]*>(.*?)</span>",
        r":g:[\3 <\2>]",
        s,
        flags=re.IGNORECASE | re.DOTALL,
    )
    s = re.sub(r"<span\b[^>]*>", ":g:", s, flags=re.IGNORECASE)
    s = re.sub(r"</span>", "", s, flags=re.IGNORECASE)
    s = re.sub(r"<sup>\s*(\d+)\s*</sup>", r":line:[\1]", s, flags=re.IGNORECASE)
    s = re.sub(r"<sup>(.*?)</sup>", r":sup:[\1]", s, flags=re.IGNORECASE | re.DOTALL)
    s = re.sub(r"</?sup\b[^>]*>", ":line:", s, flags=re.IGNORECASE)
    s = re.sub(r"<sub>(.*?)</sub>", r":sub:[\1]", s, flags=re.IGNORECASE | re.DOTALL)
    s = re.sub(r"</?sub\b[^>]*>", ":sub:", s, flags=re.IGNORECASE)
    s = re.sub(r"<br\s*/?>", " | ", s, flags=re.IGNORECASE)
    s = re.sub(r"</?(?:em|i)\b[^>]*>", "*", s, flags=re.IGNORECASE)
    s = re.sub(r"</?strong\b[^>]*>", "**", s, flags=re.IGNORECASE)
    s = re.sub(r"</?pre\b[^>]*>", ".. code-block::", s, flags=re.IGNORECASE)
    s = re.sub(r"</?figure\b[^>]*/?>", ".. picture::", s, flags=re.IGNORECASE)
    s = re.sub(r"</?center\b[^>]*>", ".. container:: center", s, flags=re.IGNORECASE)
    s = re.sub(r"</?div\b[^>]*>", ".. container::", s, flags=re.IGNORECASE)
    s = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r".. picture:: \2", s)
    s = re.sub(r"\[\^([^\]]+)\]", r"[#f\1]_", s)
    s = re.sub(r"\b(\d{4}(?:\.notes)?)\.md\b", r"\1.rst", s)
    s = re.sub(r"(?<![A-Za-z0-9_/-])\.md\b", ".rst", s)
    s = s.replace("`", "'")
    s = " ".join(s.split())
    return s if s else " "


def _split_emphasis_around_roles(text: str) -> str:
    """Un-nest roles (:g:, :just:, :line:, :sup:, :sub:), inline code spans, and nested *emphasis* inside **strong** or *emphasis*."""
    # 1. Handle triple asterisks at end of bold-italic word, e.g. **on *planes*** -> **on** *planes*
    text = re.sub(
        r"\*\*(?!\s)([^*]+?)\s+\*([^*]+?)\*\*\*",
        r"**\1** *\2*",
        text,
    )

    # 2. Handle *italic* nested inside **bold**, e.g. **on *simple* surfaces**
    def _unnest_bold_italic(match: re.Match) -> str:
        inner = match.group(1)
        if "*" not in inner:
            return match.group(0)
        tokens = re.split(r"(\*[^*]+\*)", inner)
        out: List[str] = []
        for tok in tokens:
            if not tok:
                continue
            if tok.startswith("*") and tok.endswith("*") and len(tok) >= 3:
                out.append(tok)
            else:
                m_ws = re.match(r"^(\s*)(.*?)(\s*)$", tok, re.DOTALL)
                if m_ws:
                    pre_ws, core, post_ws = m_ws.group(1), m_ws.group(2), m_ws.group(3)
                    if core:
                        if not re.search(r"[A-Za-z0-9\u0370-\u03ff\u1f00-\u1fff]", core):
                            out.append(f"{pre_ws}{core}{post_ws}")
                        else:
                            m_q = re.match(r"^(.*?)([\"“”‘’()\[\]]*)$", core, re.DOTALL)
                            if m_q and m_q.group(2) and m_q.group(1).strip():
                                c_main = m_q.group(1).rstrip()
                                c_gap = m_q.group(1)[len(c_main) :]
                                c_punct = m_q.group(2)
                                out.append(f"{pre_ws}**{c_main}**{c_gap}{c_punct}{post_ws}")
                            else:
                                out.append(f"{pre_ws}**{core}**{post_ws}")
                    else:
                        out.append(tok)
        return "".join(out)

    text = re.sub(r"\*\*(?!\s)(.+?)(?<!\s)\*\*", _unnest_bold_italic, text)

    # 3. Un-nest roles (:g:`...`, :just:`...`, :line:`...`, :sup:`...`, :sub:`...`) and code spans inside **...** or *...*
    role_split_re = re.compile(r"(__RSTCODESPAN_\d+__|:(?:g|just|line|sup|sub):`[^`]+`)")

    def _unnest_roles_in_delim(delim: str, txt: str) -> str:
        esc_d = re.escape(delim)
        pat = re.compile(rf"(?<!\*){esc_d}(?!\*)(?!\s)([^*]+?)(?<!\s){esc_d}(?!\*)")

        def _repl(match: re.Match) -> str:
            inner = match.group(1)
            if not role_split_re.search(inner):
                return match.group(0)
            parts = role_split_re.split(inner)
            rebuilt: List[str] = []
            for part in parts:
                if not part:
                    continue
                if role_split_re.fullmatch(part):
                    rebuilt.append(part)
                else:
                    m_seg = re.match(
                        r"^([\s.,;:!?—–\-()\[\]{}\"'“”‘’]*)(.*?)([\s.,;:!?—–\-()\[\]{}\"'“”‘’]*)$",
                        part,
                        re.DOTALL,
                    )
                    if m_seg and m_seg.group(2):
                        lead, core, trail = m_seg.group(1), m_seg.group(2), m_seg.group(3)
                        rebuilt.append(f"{lead}{delim}{core}{delim}{trail}")
                    else:
                        rebuilt.append(part)
            return "".join(rebuilt)

        return pat.sub(_repl, txt)

    text = _unnest_roles_in_delim("**", text)
    text = _unnest_roles_in_delim("*", text)
    return text


def _ensure_role_spacing(text: str) -> str:
    """Ensure Docutils inline markup spacing rules around :g:, :just:, :line:, :sup:, :sub: roles."""
    # For :sup: and :sub:, if preceded by non-opener (like II or *), insert '\ '
    text = re.sub(
        r"([^\s([{\"“‘—–\-\/>:\\])(:(?:sup|sub):`[^`]+`)",
        r"\1\\ \2",
        text,
    )

    # For :g:, :just:, :line:, if preceded by a non-opener character, insert a space
    text = re.sub(
        r"([^\s([{\"“‘—–\-\/>:])(:(?:g|just|line):`[^`]+`)",
        r"\1 \2",
        text,
    )

    # After any role's closing backtick, if followed immediately by a non-closer character, insert a space
    text = re.sub(
        r"(:(?:g|just|line|sup|sub):`[^`]+`)(?=[^\s.,;:!?)\]}\"”’—–\-\/<])",
        r"\1 ",
        text,
    )

    return text


def convert_inline(text: str, book: str = "I", is_notes: bool = False) -> str:
    """Convert inline HTML spans, justifications, line numbers, footnotes, and entities to RST."""
    if not text:
        return ""

    # 0. Protect inline backtick code spans (`...`) first when converting .notes.md
    code_placeholders: Dict[str, str] = {}
    cc = 0
    if is_notes:

        def _save_code_span(m: re.Match) -> str:
            nonlocal cc
            cc += 1
            tok = f"__RSTCODESPAN_{cc:04d}__"
            clean_inner = _modernize_code_literal_html(m.group(1))
            code_placeholders[tok] = f"``{clean_inner}``"
            return tok

        text = re.sub(r"``([^`\n]+)``", _save_code_span, text)
        text = re.sub(r"(?<!`)`([^`\n]+)`(?!`)", _save_code_span, text)

    # 1. Convert inline <span data-ref="TARGET">DISPLAY</span> -> :g:`DISPLAY <TARGET>` FIRST
    #    (so any <span data-ref> nested inside <span class="justification"> is resolved before outer span matching)
    def _replace_g(match: re.Match) -> str:
        target = " ".join(match.group(2).strip().split())
        display = " ".join(match.group(3).strip().split())
        return f":g:`{display} <{target}>`"

    text = re.sub(
        r"<span\b[^>]*\bdata-ref=(['\"])(.*?)\1[^>]*>(.*?)</span>",
        _replace_g,
        text,
        flags=re.DOTALL,
    )

    # 2. Convert inline <span class="justification">...</span>
    text = re.sub(
        r"<span\s+class=(['\"])justification\1\s*>(.*?)</span>",
        lambda m: format_justification(m.group(2), book=book, as_arg=False),
        text,
        flags=re.DOTALL,
    )

    # 3. Convert <sup>...</sup> -> :line:`N` (if digits) or :sup:`...`
    def _replace_sup(match: re.Match) -> str:
        inner = match.group(1).strip()
        if inner.isdigit():
            return f":line:`{inner}`"
        clean_inner = inner.strip("*").strip()
        return f":sup:`{clean_inner}`"

    text = re.sub(r"<sup>(.*?)</sup>", _replace_sup, text, flags=re.DOTALL)

    # 4. Convert <sub>...</sub> -> :sub:`...`
    text = re.sub(
        r"<sub>(.*?)</sub>",
        lambda m: f":sub:`{m.group(1).strip().strip('*').strip()}`",
        text,
        flags=re.DOTALL,
    )

    # 5. Convert <em>/<i>/<strong> and small-caps/center spans if any
    text = re.sub(
        r"<(?:em|i)>(.*?)</(?:em|i)>",
        lambda m: f"*{' '.join(m.group(1).split())}*",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"<strong>(.*?)</strong>",
        lambda m: f"**{' '.join(m.group(1).split())}**",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"<span\s+(?:style|class)=(['\"])[^'\"]*(?:small-caps|text-align:\s*center)[^'\"]*\1>(.*?)</span>",
        r"\2",
        text,
        flags=re.DOTALL,
    )

    # Strip any residual <br> or <br /> tags in inline text
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)

    # 6. Convert HTML spacing entities
    text = text.replace("&emsp;", "\u2003").replace("&ensp;", "\u2002").replace("&nbsp;", "\u00a0")

    # 7. Convert inline Markdown footnote references [^label] -> [#flabel]_
    def _replace_fn_ref(match: re.Match) -> str:
        pre = match.group(1)
        label = match.group(2).strip()
        norm_label = f"f{label}" if label and label[0].isdigit() else label
        if pre and pre not in _OPENERS:
            return f"{pre}\\ [#{norm_label}]_"
        return f"{pre}[#{norm_label}]_"

    text = re.sub(r"(.?)\[\^([^\]]+)\]", _replace_fn_ref, text)

    # Convert Markdown links [label](url) and folio .md references
    if is_notes:
        def _repl_md_link(m: re.Match) -> str:
            nonlocal cc
            lbl = re.sub(r"\b(\d{4}(?:\.notes)?)\.md\b", r"\1.rst", m.group(1).strip())
            cc += 1
            tok = f"__RSTCODESPAN_{cc:04d}__"
            code_placeholders[tok] = f"``{lbl}``"
            return tok

        text = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", _repl_md_link, text)
    text = re.sub(r"\b(\d{4}(?:\.notes)?)\.md\b", r"\1.rst", text)

    # 8. Un-nest roles inside *...* or **...** and enforce Docutils role spacing
    text = _split_emphasis_around_roles(text)
    text = _ensure_role_spacing(text)

    # Restore protected inline code spans (for .notes.rst)
    if code_placeholders:
        for tok, val in code_placeholders.items():
            text = text.replace(tok, val)

    # Collapse multiple spaces around :line: at start of line or mid-line
    text = re.sub(r"(:line:`\d+`)\s{2,}", r"\1 ", text)
    return text


def _normalize_multiline_inline_tags(raw_text: str) -> str:
    """Collapse newlines inside inline <strong>, <em>, <i>, and <span class="justification"> tags
    so line-block splitting does not sever opening and closing tags across lines."""

    def _collapse_ws(match: re.Match) -> str:
        open_tag, inner, close_tag = match.group(1), match.group(2), match.group(3)
        inner_clean = re.sub(r"<br\s*/?>", " ", inner, flags=re.IGNORECASE)
        inner_clean = " ".join(inner_clean.split())
        return f"{open_tag}{inner_clean}{close_tag}"

    raw_text = re.sub(
        r"(<(?:strong|em|i)>)(.*?)(</(?:strong|em|i)>)",
        _collapse_ws,
        raw_text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    def _collapse_just(match: re.Match) -> str:
        inner_clean = re.sub(r"<br\s*/?>", " ", match.group(3), flags=re.IGNORECASE)
        inner_clean = " ".join(inner_clean.split())
        return f"{match.group(1)}{inner_clean}{match.group(4)}"

    raw_text = re.sub(
        r"(<span\s+class=(['\"])justification\2\s*>)(.*?)(</span>)",
        _collapse_just,
        raw_text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    return raw_text


def _split_explicit_lines(raw_block: str) -> Tuple[bool, List[str]]:
    """Check if raw_block has explicit line breaks (<br> or trailing two spaces) and return (is_multiline, lines)."""
    raw_block = _normalize_multiline_inline_tags(raw_block)
    has_br = bool(re.search(r"<br\s*/?>", raw_block, flags=re.IGNORECASE))
    raw_lines = raw_block.splitlines()
    has_two_space = any(l.endswith("  ") for l in raw_lines[:-1]) if len(raw_lines) > 1 else False
    has_quad_cont = (
        len(raw_lines) > 1
        and any(l.lstrip().startswith(("$\\quad$", "\u2003", "&emsp;")) for l in raw_lines[1:])
    )

    if not (has_br or has_two_space or has_quad_cont):
        return False, [" ".join(l.strip() for l in raw_lines if l.strip())]

    expanded = [
        re.sub(r"<br\s*/?>", "", p, flags=re.IGNORECASE).rstrip()
        for p in re.split(r"(?:<br\s*/?>[ \t]*\r?\n?|\r?\n)", raw_block, flags=re.IGNORECASE)
    ]

    expanded = [p for p in expanded if p.strip()]

    if len(expanded) <= 1:
        return False, [expanded[0].strip() if expanded else ""]

    return True, expanded


def _format_body_lines_for_directive(raw_inner: str, book: str, indent: str = "   ") -> List[str]:
    """Format inner content of .. assertion::, .. subclause::, .. qed::, or .. container:: center."""
    is_multi, lines = _split_explicit_lines(raw_inner)
    if not is_multi:
        conv = convert_inline(lines[0], book=book).strip()
        return [f"{indent}{conv}"] if conv else []

    out: List[str] = []
    for line in lines:
        line_clean = line.replace("&emsp;", "  ")
        lead_spaces = len(line_clean) - len(line_clean.lstrip(" "))
        conv = convert_inline(line_clean.strip(), book=book).strip()
        extra_pad = " " * lead_spaces
        out.append(f"{indent}| {extra_pad}{conv}")
    return out


def _convert_semantic_p_block(cls_name: str, raw_inner: str, book: str) -> str:
    """Convert <p class="enunciation|assertion|sub-clause|qed">...</p> to its RST directive."""
    cls_name = cls_name.strip().lower()
    raw_inner = _normalize_multiline_inline_tags(raw_inner)

    if cls_name == "enunciation":
        cleaned = re.sub(r"<br\s*/?>", " ", raw_inner, flags=re.IGNORECASE)
        cleaned = " ".join(cleaned.split())
        conv = convert_inline(cleaned, book=book).strip()
        return f".. enunciation::\n\n   {conv}"

    if cls_name == "qed":
        body_lines = _format_body_lines_for_directive(raw_inner, book=book)
        body_str = "\n".join(body_lines)
        return f".. qed::\n\n{body_str}"

    directive_name = "assertion" if cls_name == "assertion" else "subclause"
    is_multi, _ = _split_explicit_lines(raw_inner)

    just_arg = ""
    body_raw = raw_inner

    if not is_multi:
        # First convert any <span data-ref> inside raw_inner so nested spans don't confuse justification extraction
        single_line = re.sub(
            r"<span\b[^>]*\bdata-ref=(['\"])(.*?)\1[^>]*>(.*?)</span>",
            lambda m: f":g:`{' '.join(m.group(3).strip().split())} <{' '.join(m.group(2).strip().split())}>`",
            " ".join(raw_inner.split()),
            flags=re.DOTALL,
        )
        just_matches = list(
            re.finditer(
                r"<span\s+class=(['\"])justification\1\s*>(.*?)</span>",
                single_line,
                flags=re.DOTALL,
            )
        )
        if len(just_matches) == 1:
            jm = just_matches[0]
            before = single_line[: jm.start()].strip()
            after = single_line[jm.end() :].strip()
            if not before:
                just_arg = format_justification(jm.group(2), book=book, as_arg=True)
                body_raw = after
            elif not after:
                just_arg = format_justification(jm.group(2), book=book, as_arg=True)
                body_raw = before

    header = f".. {directive_name}:: {just_arg}".rstrip()
    body_lines = _format_body_lines_for_directive(body_raw, book=book)
    body_str = "\n".join(body_lines)
    return f"{header}\n\n{body_str}"


def _convert_markdown_table(table_text: str, book: str, is_notes: bool = False) -> str:
    """Convert a Markdown pipe table into a Docutils .. list-table:: directive."""
    lines = [l.strip() for l in table_text.strip().splitlines() if l.strip()]
    if len(lines) < 2:
        return table_text

    rows: List[List[str]] = []
    has_header = False
    num_cols = 0

    for idx, line in enumerate(lines):
        inner = line
        if inner.startswith("|"):
            inner = inner[1:]
        if inner.endswith("|"):
            inner = inner[:-1]
        cells = [c.strip() for c in inner.split("|")]
        # Check if separator row (| :--- | :---: |)
        if idx == 1 and all(re.fullmatch(r"[:\-\s]*", c) for c in cells) and any("-" in c for c in cells):
            has_header = True
            num_cols = max(num_cols, len(cells))
            continue
        num_cols = max(num_cols, len(cells))
        rows.append(cells)

    if not rows or num_cols == 0:
        return table_text

    out_lines = [".. list-table::"]
    if has_header and any(c.strip() for c in rows[0]):
        out_lines.append("   :header-rows: 1")
    out_lines.append("")

    for r in rows:
        padded = (r + [""] * num_cols)[:num_cols]
        for c_idx, cell in enumerate(padded):
            conv_cell = convert_inline(cell, book=book, is_notes=is_notes).strip()
            prefix = "   * -" if c_idx == 0 else "     -"
            if conv_cell:
                out_lines.append(f"{prefix} {conv_cell}")
            else:
                out_lines.append(prefix)

    return "\n".join(out_lines)


def convert_md_to_rst(md_text: str, is_notes: bool = False) -> str:
    """Convert a folio Markdown string (with YAML frontmatter and HTML spans/tags) to pure RST."""
    if not md_text:
        return ""

    frontmatter: Dict[str, Any] = {}
    body = md_text

    # 1. Extract YAML frontmatter if present
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            try:
                parsed = yaml.safe_load(parts[1])
                if isinstance(parsed, dict):
                    frontmatter = parsed
                    body = parts[2]
            except Exception:
                pass

    if "book" in frontmatter and frontmatter["book"] is not None:
        frontmatter["book"] = _normalize_roman(frontmatter["book"])
    if "volume" in frontmatter and frontmatter["volume"] is not None:
        frontmatter["volume"] = _normalize_roman(frontmatter["volume"])

    book = str(frontmatter.get("book", "I") or "I").strip()

    # Build RST field list header
    rst_header_lines: List[str] = []
    if frontmatter:
        ordered_keys = [k for k in _STANDARD_FIELD_ORDER if k in frontmatter]
        for k in frontmatter:
            if k not in ordered_keys:
                ordered_keys.append(k)
        for k in ordered_keys:
            val = frontmatter[k]
            if isinstance(val, list):
                val_str = ", ".join(str(x).strip() for x in val if str(x).strip())
            elif val is None:
                val_str = ""
            else:
                val_str = str(val).strip()
            rst_header_lines.append(f":{k}: {val_str}".rstrip())

    # 2. Protect fenced code blocks (```...```), <pre>...</pre>, and display math ($$...$$)
    block_placeholders: Dict[str, str] = {}
    bp_count = 0

    def _store_block(rst_block: str) -> str:
        nonlocal bp_count
        bp_count += 1
        token = f"__RSTBLOCKPLACEHOLDER_{bp_count:04d}__"
        block_placeholders[token] = rst_block
        return f"\n\n{token}\n\n"

    # Fenced code blocks (top-level or indented inside lists)
    def _replace_codefence(match: re.Match) -> str:
        lang = (match.group(1) or "").strip() or "text"
        code_body = match.group(2)
        if is_notes:
            code_body = re.sub(r"\b(\d{4}(?:\.notes)?)\.md\b", r"\1.rst", code_body)
        raw_lines = code_body.splitlines()
        non_empty = [l for l in raw_lines if l.strip()]
        min_indent = min((len(l) - len(l.lstrip(" ")) for l in non_empty), default=0)
        indented_lines = [f"   {line[min_indent:]}" if line.strip() else "" for line in raw_lines]
        rst_code = f".. code-block:: {lang}\n\n" + "\n".join(indented_lines)
        return _store_block(rst_code)

    body = re.sub(
        r"^[ \t]*```([a-zA-Z0-9_-]*)\s*\n([\s\S]*?)^[ \t]*```\s*$",
        _replace_codefence,
        body,
        flags=re.MULTILINE,
    )

    # <pre>...</pre> blocks
    def _replace_pre(match: re.Match) -> str:
        code_body = match.group(1).strip("\n")
        indented_lines = [f"   {line}" if line.strip() else "" for line in code_body.splitlines()]
        rst_code = ".. code-block:: text\n\n" + "\n".join(indented_lines)
        return _store_block(rst_code)

    body = re.sub(r"<pre>([\s\S]*?)</pre>", _replace_pre, body, flags=re.IGNORECASE)

    # Display math $$...$$ (unwrap any <span data-ref="...">$X$</span> inside $$...$$)
    def _replace_display_math(match: re.Match) -> str:
        math_block = match.group(0).strip()
        math_block = re.sub(
            r"<span\b[^>]*>(.*?)</span>",
            lambda m: m.group(1).strip().strip("$"),
            math_block,
            flags=re.DOTALL,
        )
        return _store_block(math_block)

    body = re.sub(r"(?<!`)\$\$[\s\S]+?\$\$(?!`)", _replace_display_math, body)

    # Markdown pipe tables
    table_re = re.compile(
        r"(?:^[ \t]*\|[^\n]+\|[ \t]*\n)+",
        re.MULTILINE,
    )

    def _replace_table_if_valid(match: re.Match) -> str:
        grp = match.group(0)
        lines = [l.strip() for l in grp.strip().splitlines() if l.strip()]
        if len(lines) >= 2 and re.search(r"^[ \t]*\|[ \t]*[:\-]+", lines[1]):
            return _store_block(_convert_markdown_table(grp, book=book, is_notes=is_notes))
        return grp

    body = table_re.sub(_replace_table_if_valid, body)

    if not is_notes:
        # Convert inline <span data-ref> first so nested spans inside <span style="display: block..."> or <p> don't collide
        body = re.sub(
            r"<span\b[^>]*\bdata-ref=(['\"])(.*?)\1[^>]*>(.*?)</span>",
            lambda m: f":g:`{' '.join(m.group(3).strip().split())} <{' '.join(m.group(2).strip().split())}>`",
            body,
            flags=re.DOTALL,
        )

        # Unwrap <span style="display: block; text-align: center;">...</span> inside <p class="sub-clause">
        body = re.sub(
            r"<span\s+style=(['\"])[^'\"]*display:\s*block;\s*text-align:\s*center;?[^'\"]*\1>(.*?)</span>",
            r"\2<br />",
            body,
            flags=re.DOTALL | re.IGNORECASE,
        )

        # 3. Consecutive centered blocks (<p style="text-align: center;">...</p>, <p align="center">, <div align="center">)
        center_tag_re = re.compile(
            r"(?:^[ \t]*<(p|div)\s+(?:style=['\"][^'\"]*text-align:\s*center;?[^'\"]*['\"]|align=['\"]center['\"])>(.*?)</\1>[ \t]*\n?)+",
            re.MULTILINE | re.DOTALL | re.IGNORECASE,
        )

        def _replace_center_group(match: re.Match) -> str:
            group_txt = match.group(0)
            items = [
                m.group(2)
                for m in re.finditer(
                    r"<(p|div)\s+(?:style=['\"][^'\"]*text-align:\s*center;?[^'\"]*['\"]|align=['\"]center['\"])>(.*?)</\1>",
                    group_txt,
                    flags=re.DOTALL | re.IGNORECASE,
                )
            ]
            joined_inner = "<br>\n".join(item.strip() for item in items if item.strip())
            body_lines = _format_body_lines_for_directive(joined_inner, book=book)
            rst_center = ".. container:: center\n\n" + "\n".join(body_lines)
            return _store_block(rst_center)

        body = center_tag_re.sub(_replace_center_group, body)

        # Also <center>...</center>
        body = re.sub(
            r"<center>(.*?)</center>",
            lambda m: _store_block(
                ".. container:: center\n\n"
                + "\n".join(_format_body_lines_for_directive(m.group(1), book=book))
            ),
            body,
            flags=re.DOTALL | re.IGNORECASE,
        )

        # Right-aligned <p align="right">...</p> -> .. qed::
        body = re.sub(
            r"<p\s+(?:style=['\"][^'\"]*text-align:\s*right;?[^'\"]*['\"]|align=['\"]right['\"])>(.*?)</p>",
            lambda m: _store_block(_convert_semantic_p_block("qed", m.group(1), book=book)),
            body,
            flags=re.DOTALL | re.IGNORECASE,
        )

        # 4. Semantic <p class="enunciation|assertion|sub-clause|qed">...</p> blocks
        body = re.sub(
            r"<p\s+class=(['\"])(enunciation|assertion|sub-clause|qed)\1\s*>(.*?)</p>",
            lambda m: _store_block(_convert_semantic_p_block(m.group(2), m.group(3), book=book)),
            body,
            flags=re.DOTALL | re.IGNORECASE,
        )

    # 5. Standalone images ![alt](filename) -> .. picture:: filename (outside inline backticks)
    def _replace_image(match: re.Match) -> str:
        alt = match.group(1).strip()
        # Strip any HTML spans inside alt text
        alt = re.sub(r"<span\b[^>]*>(.*?)</span>", r"\1", alt, flags=re.DOTALL)
        alt = " ".join(alt.split())
        src = match.group(2).strip()
        if alt:
            rst_pic = f".. picture:: {src}\n   :alt: {alt}"
        else:
            rst_pic = f".. picture:: {src}"
        return _store_block(rst_pic)

    body = re.sub(r"(?<!`)!\[([^\]]*)\]\(([^)]+)\)(?!`)", _replace_image, body)

    # Ensure Markdown headings (#, ##, ###, ...) have blank lines before and after them
    body = re.sub(r"^(#{1,6}[ \t]+[^\n]+)$", r"\n\n\1\n\n", body, flags=re.MULTILINE)

    # 6. Process remaining paragraphs/blocks in body
    raw_blocks = re.split(r"\n\s*\n", body.strip())
    out_blocks: List[str] = []

    list_item_re = re.compile(r"^(\s*)(?:[-*]|\d+\.|[IVXLCDM]+\.|\([0-9a-zA-Z]+\)|\([*][a-zA-Z]+[*]\))\s+")

    for raw_block in raw_blocks:
        stripped_block = raw_block.strip()
        if not stripped_block:
            continue

        if stripped_block in block_placeholders:
            out_blocks.append(block_placeholders[stripped_block])
            continue

        # Horizontal rule ---
        if re.fullmatch(r"-{3,}", stripped_block):
            out_blocks.append("----")
            continue

        # Footnote definition [^label]: text
        m_fndef = re.match(r"^\[\^([^\]]+)\]:\s*([\s\S]*)$", stripped_block)
        if m_fndef:
            label = m_fndef.group(1).strip()
            norm_label = f"f{label}" if label and label[0].isdigit() else label
            fn_text = convert_inline(" ".join(m_fndef.group(2).split()), book=book, is_notes=is_notes)
            out_blocks.append(f".. [#{norm_label}] {fn_text}")
            continue

        # Markdown Heading (#, ##, ###, ####, #####)
        m_head = re.match(r"^(#{1,6})\s+(.+)$", stripped_block)
        if m_head and "\n" not in stripped_block:
            level = len(m_head.group(1))
            title_raw = m_head.group(2).strip()
            title_conv = convert_inline(title_raw, book=book, is_notes=is_notes).strip()
            ch = _HEADING_CHARS.get(level, "~")
            underline = ch * _column_width(title_conv)
            out_blocks.append(f"{title_conv}\n{underline}")
            continue

        # Blockquote (> ...)
        block_lines = raw_block.splitlines()
        if all(l.strip().startswith(">") for l in block_lines if l.strip()):
            q_lines = [re.sub(r"^\s*>\s?", "", l) for l in block_lines if l.strip()]
            if len(q_lines) > 1:
                conv_q = [f"   | {convert_inline(ql.strip(), book=book, is_notes=is_notes)}" for ql in q_lines]
            else:
                conv_q = [f"   {convert_inline(q_lines[0].strip(), book=book, is_notes=is_notes)}"]
            out_blocks.append("\n".join(conv_q))
            continue

        # Check for explicit line-breaks (<br>, trailing two spaces, or \quad continuation lines)
        is_multi, split_lines = _split_explicit_lines(raw_block)
        if is_multi and not is_notes:
            lb_out: List[str] = []
            for sline in split_lines:
                sline_clean = sline.replace("&emsp;", "  ")
                lead_spaces = len(sline_clean) - len(sline_clean.lstrip(" "))
                conv_s = convert_inline(sline_clean.strip(), book=book, is_notes=is_notes).strip()
                extra_pad = " " * lead_spaces
                lb_out.append(f"| {extra_pad}{conv_s}")
            out_blocks.append("\n".join(lb_out))
            continue

        # Check if this block contains list items or mixed enumerator + unindented paragraphs
        if len(block_lines) > 1 and any(list_item_re.match(l) for l in block_lines):
            sub_lines_out: List[str] = []
            prev_indent: Optional[int] = None
            prev_was_list = False
            for l in block_lines:
                m_li = list_item_re.match(l)
                conv_l = convert_inline(l.rstrip(), book=book, is_notes=is_notes)
                if m_li:
                    curr_indent = len(m_li.group(1))
                    if prev_was_list and prev_indent is not None and curr_indent != prev_indent:
                        sub_lines_out.append("")
                    elif not prev_was_list and sub_lines_out:
                        sub_lines_out.append("")
                    sub_lines_out.append(conv_l)
                    prev_indent = curr_indent
                    prev_was_list = True
                else:
                    lead_sp = len(l) - len(l.lstrip(" "))
                    if prev_was_list and lead_sp == 0:
                        sub_lines_out.append("")
                        prev_was_list = False
                        prev_indent = None
                    sub_lines_out.append(conv_l)
            out_blocks.append("\n".join(sub_lines_out))
            continue

        # Standard paragraph
        norm_block = _normalize_multiline_inline_tags(raw_block)
        conv_lines = [
            convert_inline(l.strip(), book=book, is_notes=is_notes)
            for l in norm_block.splitlines()
            if l.strip()
        ]
        out_blocks.append("\n".join(conv_lines))

    # Assemble final RST
    pieces: List[str] = []
    if rst_header_lines:
        pieces.append("\n".join(rst_header_lines))
    if out_blocks:
        pieces.append("\n\n".join(out_blocks))

    return "\n\n".join(pieces).rstrip() + "\n"


def convert_file(md_path: Path, overwrite: bool = True) -> Path:
    """Convert a single <folio>.md (or <folio>.notes.md) file to .rst alongside it."""
    is_notes = md_path.name.endswith(".notes.md")
    rst_path = md_path.with_suffix(".rst")
    if not overwrite and rst_path.exists():
        return rst_path

    md_text = md_path.read_text(encoding="utf-8")
    rst_text = convert_md_to_rst(md_text, is_notes=is_notes)
    rst_path.write_text(rst_text, encoding="utf-8")
    return rst_path
