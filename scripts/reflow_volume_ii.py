#!/usr/bin/env python3
"""Remove :line: roles, rejoin hyphenated line wraps, and reflow forced | line-blocks across Volume II."""

from __future__ import annotations

import re
from pathlib import Path
from typing import List, Tuple

_REPO_ROOT = Path(__file__).resolve().parents[1]
_VOL2_DIR = _REPO_ROOT / "resources" / "heath" / "volume_II"

_KEEP_HYPHENS = {
    "one-third",
    "one-fifth",
    "two-fifths",
    "three-fifths",
    "fifteen-angled",
    "five-angled",
    "three-angled",
    "four-angled",
    "six-angled",
    "even-times",
    "odd-times",
    "non-corresponding",
    "falling-short",
    "right-angled",
    "obtuse-angled",
    "acute-angled",
}

_INTRA_LINE_HYPHENS = {
    "circum- ference": "circumference",
    "circum- ferences": "circumferences",
    "rect- angle": "rectangle",
    "equi- angular": "equiangular",
    "propor- tional": "proportional",
    "pro- portional": "proportional",
    "even- times": "even-times",
    "odd- times": "odd-times",
    "equi- multiples": "equimultiples",
    "corre- sponding": "corresponding",
    "con- tained": "contained",
    "parallelo- gram": "parallelogram",
    "multi- plying": "multiplying",
    "con- tinued": "continued",
}


def is_field_or_directive(line: str) -> bool:
    s = line.lstrip()
    if s.startswith(("..", "|", "* ", "- ")):
        return True
    if re.match(r"^:(?:folio|page|volume|book|section|title|propositions|alt):", s):
        return True
    return False


def strip_line_roles(line: str) -> str:
    """Remove :line:`N` tags and normalize spacing."""
    for old_h, new_h in _INTRA_LINE_HYPHENS.items():
        if old_h in line:
            line = line.replace(old_h, new_h)
    if ":line:" in line:
        m_orig = re.match(r"^(\s*)", line)
        orig_indent = m_orig.group(1) if m_orig else ""
        res = re.sub(r":line:`\d+`\s*", "", line)
        m = re.match(r"^(\s*\|\s*|\s*)(.*)$", res)
        if m:
            prefix, body = m.group(1), m.group(2)
            body = re.sub(r"  +", " ", body).strip()
            if prefix.strip() == "|":
                return f"{orig_indent}| {body}" if body else f"{orig_indent}|"
            return f"{orig_indent}{body}" if body else ""
    # Fix residual 1-space or 4-space indents left by previous :line: stripping
    m_ind = re.match(r"^( +)(\S.*)$", line)
    if m_ind:
        spaces, rest = m_ind.group(1), m_ind.group(2)
        if len(spaces) == 1:
            return rest
        if len(spaces) == 4:
            return "   " + rest
    return line


def join_two_lines(prev: str, curr: str) -> str:
    """Join two consecutive lines, removing end-of-line word-wrap hyphens."""
    m1 = re.search(r"([A-Za-z]+)-(\*{0,2})$", prev)
    m2 = re.match(r"^(\*{0,2})([A-Za-z]+)(.*)$", curr)
    if m1 and m2:
        w1, s1 = m1.group(1), m1.group(2)
        s2, w2, rest = m2.group(1), m2.group(2), m2.group(3)
        compound = f"{w1}-{w2}".lower()
        if compound in _KEEP_HYPHENS:
            return prev + curr
        if s1 == s2:
            return prev[: m1.start()] + w1 + w2 + rest
    return prev + " " + curr


def visible_len(s: str) -> int:
    s2 = re.sub(r":[a-z]+:`([^`<]+?)\s*<[^>]+>`", r"\1", s)
    return len(s2)


def should_break_paragraph(prev: str, curr: str, indent: str) -> bool:
    if indent:
        return False
    # New numbered item or note
    if re.match(r"^(?:\*{0,2}\d+(?:\s*,\s*\d+)*\.|\([a-z0-9]+\)\s)", curr):
        return True
    # Previous line ends with :just:`...`
    if re.search(r":just:`[^`]+`\s*$", prev):
        return True
    # Previous line ends with sentence/clause punctuation and curr starts a new proposition step
    if re.search(r"[.;:?!][\"”’\x27)]*\s*$", prev):
        if re.match(
            r"^(?:I say that\b|thus it is required\b|Thus it is required\b|Therefore\b|For let\b|Let\b|"
            r"Again,\s*let\b|Next,\s*let\b|First,\s*let\b|Similarly\b|And,\s*since\b|Now,\s*since\b|"
            r"But,\s*since\b|For,\s*since\b|Since\s+then\b|Since,\s*then\b)",
            curr,
        ):
            return True
        if visible_len(prev) < 52 and re.match(r"^[A-Z\"“‘$(\[]", curr):
            return True
    return False


def reflow_non_pipe_hyphens(lines: List[str]) -> List[str]:
    """Rejoin hyphenated word wraps across consecutive non-pipe prose lines."""
    out: List[str] = []
    i = 0
    n = len(lines)
    while i < n:
        curr = lines[i]
        # Strip leaked running page headers (e.g. "VII. 31—33] PROPOSITIONS 30—33 333" or "334 BOOK VII [VII. 33")
        if re.match(r"^(?:VII\.\s*\d+.*?\d{3}|\d{3}\s+BOOK\s+VII\s+\[VII\.\s*\d+)$", curr.strip()):
            i += 1
            if i < n and not lines[i].strip() and (not out or not out[-1].strip()):
                i += 1
            continue
        if (
            i + 1 < n
            and curr.strip()
            and lines[i + 1].strip()
            and not is_field_or_directive(curr)
            and not is_field_or_directive(lines[i + 1])
        ):
            m1 = re.search(r"([A-Za-z]+)-(\*{0,2})$", curr.rstrip())
            m2 = re.match(r"^(\s*)(\*{0,2})([A-Za-z]+)\b(.*)$", lines[i + 1])
            if m1 and m2:
                w1, s1 = m1.group(1), m1.group(2)
                ind2, s2, w2, rest2 = m2.group(1), m2.group(2), m2.group(3), m2.group(4)
                compound = f"{w1}-{w2}".lower()
                if s1 == s2:
                    if compound in _KEEP_HYPHENS:
                        curr_joined = curr.rstrip()[: m1.start()] + f"{w1}-{w2}" + s1
                    else:
                        curr_joined = curr.rstrip()[: m1.start()] + w1 + w2 + s1
                    rem = rest2.lstrip()
                    out.append(curr_joined)
                    if rem:
                        lines[i + 1] = f"{ind2}{rem}"
                        i += 1
                    else:
                        i += 2
                    continue
        out.append(curr)
        i += 1
    return out


def reflow_folio_lines(lines: List[str]) -> List[str]:
    cleaned = [strip_line_roles(l) for l in lines]
    out: List[str] = []
    i = 0
    n = len(cleaned)
    while i < n:
        line = cleaned[i]
        m = re.match(r"^(\s*)\|(?:\s+(.*))?$", line)
        if not m:
            out.append(line)
            i += 1
            continue
        block_indent = m.group(1)
        paragraphs: List[Tuple[str, str]] = []
        curr_p = ""
        while i < n:
            m_i = re.match(r"^(\s*)\|(?:\s+(.*))?$", cleaned[i])
            if not m_i:
                break
            ind_i = m_i.group(1)
            body_i = (m_i.group(2) or "").strip()
            if not body_i:
                if curr_p:
                    paragraphs.append((block_indent, curr_p))
                    curr_p = ""
                i += 1
                continue
            if not curr_p:
                block_indent = ind_i
                curr_p = body_i
            else:
                if ind_i != block_indent or should_break_paragraph(curr_p, body_i, block_indent):
                    paragraphs.append((block_indent, curr_p))
                    block_indent = ind_i
                    curr_p = body_i
                else:
                    curr_p = join_two_lines(curr_p, body_i)
            i += 1
        if curr_p:
            paragraphs.append((block_indent, curr_p))
        for idx_p, (ind_p, text_p) in enumerate(paragraphs):
            if idx_p > 0:
                out.append("")
            out.append(f"{ind_p}{text_p}")

    return reflow_non_pipe_hyphens(out)


def main() -> None:
    files = sorted(f for f in _VOL2_DIR.rglob("*.rst") if not f.name.endswith(".notes.rst"))
    modified = 0
    for f in files:
        orig = f.read_text(encoding="utf-8")
        new_lines = reflow_folio_lines(orig.splitlines())
        new_text = "\n".join(new_lines) + "\n"
        if new_text != orig:
            f.write_text(new_text, encoding="utf-8")
            modified += 1
    print(f"Reflowed and cleaned {modified} / {len(files)} folios in Volume II.")


if __name__ == "__main__":
    main()
