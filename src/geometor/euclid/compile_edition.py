"""De-Pagination Compiler for GEOMETOR Euclid.

Reads sequential ``<folio>.rst`` files within each book (e.g. ``resources/heath/volume_I/book_i``),
detects logical unit headers (``DEFINITIONS.``, ``POSTULATES.``, ``COMMON NOTIONS.``,
``PROPOSITION N.``, ``LEMMA.``), stitches blocks across folio boundaries with ``.. folio::``
milestones, heals mid-sentence page-break splits, separates Heath's commentary into companion
``commentary.rst`` files linked via ``:ref:``, and writes the canonical Book Edition under
``docsrc/heath/``.
"""

from __future__ import annotations

import re
import shutil
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from geometor.euclid.folio_review.rst_utils import parse_rst_metadata, validate_rst


_ADORNMENT_RE = re.compile(r"^([=!~^\"'`#*+\-_])\1{3,}\s*$")
_TERMINAL_PUNCT = (".", "!", "?", ":", ";", "”", '"', "'", "’", ")", "]")
_PICTURE_RE = re.compile(r"^\.\.\s+picture::\s+(\S+)", re.MULTILINE)
_JUST_ROLE_TARGET_RE = re.compile(r":just:`[^`<]*<([^>]+)>`")
_DIR_JUST_TARGET_RE = re.compile(
    r"^\.\.\s+(?:assertion|subclause|sub-clause)::[ \t]+[^\n<]*<([^>\n]+)>",
    re.MULTILINE,
)


@dataclass
class TaggedBlock:
    """A single RST block tagged with its originating folio and page number."""

    text: str
    folio: str
    page: str
    source_dir: Path


def _column_width(text: str) -> int:
    width = 0
    for ch in text:
        if unicodedata.east_asian_width(ch) in ("W", "F"):
            width += 2
        else:
            width += 1
    return max(width, len(text), 4)


def _make_heading(title: str, char: str = "=") -> str:
    return f"{title}\n{char * _column_width(title)}"


def _is_heading_block(block_text: str) -> Optional[Tuple[str, str]]:
    """Return (title, underline_char) if block_text is a 2-line RST section heading."""
    lines = [l.rstrip() for l in block_text.strip().splitlines()]
    if len(lines) == 2 and lines[0].strip() and _ADORNMENT_RE.match(lines[1].strip()):
        if not lines[0].lstrip().startswith(("..", ":")):
            return lines[0].strip(), lines[1].strip()[0]
    return None


def _is_plain_paragraph(block_text: str) -> bool:
    """Return True if block_text is a standard flowing text paragraph (not a directive, heading, list, or line-block)."""
    s = block_text.strip()
    if not s:
        return False
    if _is_heading_block(s):
        return False
    if s.startswith(("..", "|", ":folio:", "----", "$$")):
        return False
    first_line = s.splitlines()[0].lstrip()
    if re.match(r"^(?:[-*]|\d+\.|[IVXLCDM]+\.|\([0-9a-zA-Z*]+\))\s+", first_line):
        return False
    if s.startswith("   "):
        return False
    return True


def _should_heal_paragraphs(prev_text: str, next_text: str) -> bool:
    """Return True if prev_text and next_text form a single paragraph split mid-sentence across a folio break."""
    if not (_is_plain_paragraph(prev_text) and _is_plain_paragraph(next_text)):
        return False
    p_strip = prev_text.rstrip()
    n_strip = next_text.lstrip()
    if not p_strip or not n_strip:
        return False
    if p_strip.endswith(_TERMINAL_PUNCT):
        return False
    return True


def _merge_split_paragraphs(prev_text: str, next_text: str) -> str:
    """Heal a mid-sentence paragraph split across a folio boundary."""
    p_strip = prev_text.rstrip()
    n_strip = next_text.lstrip()
    # De-hyphenate word split across page break (e.g. 'correspond-' + 'ing')
    if (
        p_strip.endswith("-")
        and not p_strip.endswith("--")
        and n_strip
        and n_strip[0].islower()
    ):
        return p_strip[:-1] + n_strip
    return f"{p_strip}\n{n_strip}"


def _parse_folio_blocks(rst_path: Path) -> Tuple[Dict[str, Any], List[TaggedBlock]]:
    """Parse a <folio>.rst file into (metadata, list of TaggedBlock)."""
    raw = rst_path.read_text(encoding="utf-8")
    meta, body = parse_rst_metadata(raw)
    folio = str(meta.get("folio", rst_path.stem)).strip()
    page = str(meta.get("page", "")).strip()

    raw_blocks = re.split(r"\n\s*\n", body.strip())
    blocks: List[TaggedBlock] = []
    idx = 0
    n = len(raw_blocks)

    while idx < n:
        blk = raw_blocks[idx].strip("\n")
        if not blk.strip():
            idx += 1
            continue

        # Keep a directive header (`.. name::`) and its indented body together as a single logical block
        first_line = blk.splitlines()[0].strip()
        if re.match(r"^\.\.\s+[a-zA-Z0-9_-]+::", first_line):
            combined = [blk]
            while idx + 1 < n and (
                raw_blocks[idx + 1].startswith("   ") or raw_blocks[idx + 1].startswith("\t")
            ):
                idx += 1
                combined.append(raw_blocks[idx].strip("\n"))
            blk = "\n\n".join(combined)

        blocks.append(
            TaggedBlock(
                text=blk.strip(),
                folio=folio,
                page=page,
                source_dir=rst_path.parent,
            )
        )
        idx += 1

    return meta, blocks


def _render_blocks_with_milestones(
    blocks: List[TaggedBlock],
) -> Tuple[str, List[str], List[str], Set[Tuple[Path, str]]]:
    """Assemble tagged blocks into RST text, inserting .. folio:: milestones and healing page breaks.

    Returns (rst_body, ordered_folios, ordered_pages, referenced_media_files).
    """
    out_blocks: List[str] = []
    folios_seen: List[str] = []
    pages_seen: List[str] = []
    media_files: Set[Tuple[Path, str]] = set()

    current_folio: Optional[str] = None

    for b in blocks:
        # Record media references
        for m_pic in _PICTURE_RE.finditer(b.text):
            fname = m_pic.group(1).strip()
            media_files.add((b.source_dir, fname))

        if b.folio and b.folio not in folios_seen:
            folios_seen.append(b.folio)
        if b.page and b.page not in pages_seen:
            pages_seen.append(b.page)

        is_new_folio = b.folio != current_folio
        if is_new_folio:
            milestone = f".. folio:: {b.folio}"
            if b.page:
                milestone += f"\n   :page: {b.page}"

            # Check if this first block of the new folio heals into the last block of the previous folio
            if out_blocks and _should_heal_paragraphs(out_blocks[-1], b.text):
                out_blocks[-1] = _merge_split_paragraphs(out_blocks[-1], b.text)
                out_blocks.append(milestone)
            else:
                out_blocks.append(milestone)
                out_blocks.append(b.text)
            current_folio = b.folio
        else:
            out_blocks.append(b.text)

    return "\n\n".join(out_blocks), folios_seen, pages_seen, media_files


def _extract_dependencies(rst_body: str) -> List[str]:
    """Extract sorted unique canonical dependency IDs from :just: roles and directive arguments."""
    deps: Set[str] = set()
    for m in _JUST_ROLE_TARGET_RE.finditer(rst_body):
        for part in m.group(1).split(","):
            p = part.strip()
            if p:
                deps.add(p)
    for m in _DIR_JUST_TARGET_RE.finditer(rst_body):
        for part in m.group(1).split(","):
            p = part.strip()
            if p:
                deps.add(p)
    return sorted(deps)


def _copy_media_files(media_files: Set[Tuple[Path, str]], target_dir: Path) -> int:
    """Copy referenced SVG/PNG diagram files into target_dir so .. picture:: resolves locally."""
    copied = 0
    for src_dir, filename in media_files:
        src_path = src_dir / filename
        if not src_path.exists():
            # Search parent book directory if needed
            candidates = list(src_dir.parent.rglob(filename))
            if candidates:
                src_path = candidates[0]
        if src_path.exists():
            dst_path = target_dir / filename
            if not dst_path.exists() or src_path.stat().st_mtime > dst_path.stat().st_mtime:
                shutil.copy2(src_path, dst_path)
            copied += 1
    return copied


def _split_proposition_proof_and_commentary(
    blocks: List[TaggedBlock],
) -> Tuple[List[TaggedBlock], List[TaggedBlock]]:
    """Split a proposition's blocks into (proof_blocks, commentary_blocks)."""
    # Strip trailing '----' transition dividers at the very end of the unit
    cleaned = list(blocks)
    while cleaned and cleaned[-1].text == "----":
        cleaned.pop()

    # Find the last .. qed:: block in the proposition's main proof
    qed_idx = -1
    for i, b in enumerate(cleaned):
        if b.text.startswith(".. qed::"):
            qed_idx = i
            break

    if qed_idx == -1:
        return cleaned, []

    split_idx = qed_idx + 1
    # Include any immediate PORISM / Corollary block before '----'
    while split_idx < len(cleaned):
        cand = cleaned[split_idx].text
        if cand == "----":
            break
        if "PORISM" in cand.upper() or cand.startswith(".. porism::"):
            # Convert [PORISM. ...] to .. porism:: directive if plain paragraph
            if not cand.startswith(".. porism::"):
                inner_p = re.sub(r"^(:line:`\d+`\s*)?\[?PORISM\.?\s*", r"\1", cand, flags=re.I)
                inner_p = inner_p.rstrip("]")
                cleaned[split_idx] = TaggedBlock(
                    text=f".. porism::\n\n   {inner_p.strip()}",
                    folio=cleaned[split_idx].folio,
                    page=cleaned[split_idx].page,
                    source_dir=cleaned[split_idx].source_dir,
                )
            split_idx += 1
        else:
            break

    proof_blocks = cleaned[:split_idx]
    rem = cleaned[split_idx:]
    while rem and rem[0].text == "----":
        rem.pop(0)
    while rem and rem[-1].text == "----":
        rem.pop()

    return proof_blocks, rem


def _write_unit_files(
    out_dir: Path,
    canonical_id: str,
    book_roman: str,
    unit_type: str,
    title: str,
    main_blocks: List[TaggedBlock],
    comm_blocks: List[TaggedBlock],
    prop_num: Optional[int] = None,
) -> List[Path]:
    """Write index.rst (and commentary.rst if comm_blocks is non-empty) into out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    written: List[Path] = []

    main_body, main_folios, main_pages, main_media = _render_blocks_with_milestones(main_blocks)
    deps = _extract_dependencies(main_body)

    header_lines = [
        f":canonical_id: {canonical_id}",
        f":book: {book_roman}",
    ]
    if prop_num is not None:
        header_lines.append(f":proposition: {prop_num}")
    header_lines.extend(
        [
            f":type: {unit_type}",
            f":title: {title}",
            f":folios: {', '.join(main_folios)}",
            f":pages: {', '.join(main_pages)}",
        ]
    )
    if deps:
        header_lines.append(f":dependencies: {', '.join(deps)}")

    has_comm = len(comm_blocks) > 0
    comm_id = f"{canonical_id}.commentary"

    parts = [
        "\n".join(header_lines),
        f".. _{canonical_id}:",
        main_body,
    ]
    if has_comm:
        parts.append("----")
        parts.append(f"See :ref:`Commentary on {title} <{comm_id}>`.")
        parts.append(".. toctree::\n   :hidden:\n\n   commentary")

    index_path = out_dir / "index.rst"
    index_path.write_text("\n\n".join(parts).rstrip() + "\n", encoding="utf-8")
    written.append(index_path)
    _copy_media_files(main_media, out_dir)

    if has_comm:
        comm_body, comm_folios, comm_pages, comm_media = _render_blocks_with_milestones(comm_blocks)
        comm_header = [
            f":canonical_id: {comm_id}",
            f":book: {book_roman}",
        ]
        if prop_num is not None:
            comm_header.append(f":proposition: {prop_num}")
        comm_header.extend(
            [
                ":type: commentary",
                f":title: Commentary on {title}",
                f":folios: {', '.join(comm_folios)}",
                f":pages: {', '.join(comm_pages)}",
            ]
        )
        comm_parts = [
            "\n".join(comm_header),
            f".. _{comm_id}:",
            _make_heading(f"Commentary on {title}", "="),
            f"Back to :ref:`{title} <{canonical_id}>`.",
            comm_body,
        ]
        comm_path = out_dir / "commentary.rst"
        comm_path.write_text("\n\n".join(comm_parts).rstrip() + "\n", encoding="utf-8")
        written.append(comm_path)
        _copy_media_files(comm_media, out_dir)

    return written


def compile_book(book_src_dir: Path, book_out_dir: Path) -> Dict[str, Any]:
    """Compile all sequential <folio>.rst files in a book directory into canonical docsrc units."""
    folio_files = sorted(
        [f for f in book_src_dir.rglob("*.rst") if not f.name.endswith(".notes.rst")],
        key=lambda p: (int(p.stem) if p.stem.isdigit() else 999999, p.stem),
    )

    all_blocks: List[TaggedBlock] = []
    book_roman = "I"
    for fp in folio_files:
        meta, f_blocks = _parse_folio_blocks(fp)
        if meta.get("book"):
            book_roman = str(meta["book"]).strip()
        all_blocks.extend(f_blocks)

    # Partition stream into First Principles vs Propositions
    # First Principles units in Book I:
    # - DEFINITIONS.
    # - POSTULATES.
    # - COMMON NOTIONS.
    # - DEFINITION 1. (start of Definitions Commentary)
    # - POSTULATE 1. (start of Postulates Commentary)
    # - AXIOMS OR *COMMON NOTIONS*. / COMMON NOTION 1. (start of Common Notions Commentary)
    # Propositions:
    # - PROPOSITION N.
    fp_sections: Dict[str, List[TaggedBlock]] = {
        "def_main": [],
        "post_main": [],
        "cn_main": [],
        "def_comm": [],
        "post_comm": [],
        "cn_comm": [],
    }
    propositions: Dict[int, List[TaggedBlock]] = {}

    current_bucket: Optional[str] = None
    current_prop: Optional[int] = None

    for b in all_blocks:
        h = _is_heading_block(b.text)
        if h:
            htitle = h[0].upper().strip()
            # Skip top-level BOOK I. / BOOK I. PROPOSITIONS. banner headings
            if re.match(r"^BOOK\s+[IVXLCDM]+\b", htitle):
                continue

            m_prop = re.match(r"^PROPOSITION\s+(\d+)\.?$", htitle)
            if m_prop:
                current_prop = int(m_prop.group(1))
                current_bucket = None
                propositions.setdefault(current_prop, []).append(
                    TaggedBlock(
                        text=_make_heading(f"PROPOSITION {current_prop}.", "="),
                        folio=b.folio,
                        page=b.page,
                        source_dir=b.source_dir,
                    )
                )
                continue

            if current_prop is None:
                if htitle == "DEFINITIONS.":
                    current_bucket = "def_main"
                elif htitle == "POSTULATES.":
                    current_bucket = "post_main"
                elif htitle == "COMMON NOTIONS.":
                    current_bucket = "cn_main"
                elif re.match(r"^DEFINITIONS?\s+\d+", htitle) and current_bucket in (
                    "cn_main",
                    "def_main",
                    "post_main",
                ):
                    current_bucket = "def_comm"
                elif re.match(r"^POSTULATES?\s+\d+", htitle) and current_bucket in (
                    "def_comm",
                    "post_main",
                    "cn_main",
                ):
                    current_bucket = "post_comm"
                elif (
                    "AXIOMS" in htitle or re.match(r"^COMMON\s+NOTIONS?\s+\d+", htitle)
                ) and current_bucket in ("post_comm", "def_comm", "cn_main"):
                    current_bucket = "cn_comm"

        if current_prop is not None:
            propositions[current_prop].append(b)
        elif current_bucket is not None:
            fp_sections[current_bucket].append(b)

    written_files: List[Path] = []
    book_out_dir.mkdir(parents=True, exist_ok=True)
    toc_entries: List[str] = []

    # 1. Write Definitions
    if fp_sections["def_main"]:
        # Normalize first heading to '='
        h0 = _is_heading_block(fp_sections["def_main"][0].text)
        if h0:
            fp_sections["def_main"][0].text = _make_heading(h0[0], "=")
        written_files.extend(
            _write_unit_files(
                out_dir=book_out_dir / "definitions",
                canonical_id=f"{book_roman}.def",
                book_roman=book_roman,
                unit_type="definitions",
                title=f"Book {book_roman} Definitions",
                main_blocks=fp_sections["def_main"],
                comm_blocks=fp_sections["def_comm"],
            )
        )
        toc_entries.append("definitions/index")

    # 2. Write Postulates
    if fp_sections["post_main"]:
        h0 = _is_heading_block(fp_sections["post_main"][0].text)
        if h0:
            fp_sections["post_main"][0].text = _make_heading(h0[0], "=")
        written_files.extend(
            _write_unit_files(
                out_dir=book_out_dir / "postulates",
                canonical_id=f"{book_roman}.post",
                book_roman=book_roman,
                unit_type="postulates",
                title=f"Book {book_roman} Postulates",
                main_blocks=fp_sections["post_main"],
                comm_blocks=fp_sections["post_comm"],
            )
        )
        toc_entries.append("postulates/index")

    # 3. Write Common Notions
    if fp_sections["cn_main"]:
        h0 = _is_heading_block(fp_sections["cn_main"][0].text)
        if h0:
            fp_sections["cn_main"][0].text = _make_heading(h0[0], "=")
        written_files.extend(
            _write_unit_files(
                out_dir=book_out_dir / "common_notions",
                canonical_id=f"{book_roman}.cn",
                book_roman=book_roman,
                unit_type="common_notions",
                title=f"Book {book_roman} Common Notions",
                main_blocks=fp_sections["cn_main"],
                comm_blocks=fp_sections["cn_comm"],
            )
        )
        toc_entries.append("common_notions/index")

    # 4. Write Propositions
    prop_toc_entries: List[str] = []
    props_with_comm = 0
    for pnum in sorted(propositions.keys()):
        p_blocks = propositions[pnum]
        proof_blocks, comm_blocks = _split_proposition_proof_and_commentary(p_blocks)
        if comm_blocks:
            props_with_comm += 1
        p_dir_name = f"{pnum:02d}"
        p_out_dir = book_out_dir / "propositions" / p_dir_name
        written_files.extend(
            _write_unit_files(
                out_dir=p_out_dir,
                canonical_id=f"{book_roman}.{pnum}",
                book_roman=book_roman,
                unit_type="proposition",
                title=f"Proposition {pnum}",
                main_blocks=proof_blocks,
                comm_blocks=comm_blocks,
                prop_num=pnum,
            )
        )
        prop_toc_entries.append(f"{p_dir_name}/index")

    if prop_toc_entries:
        props_index_path = book_out_dir / "propositions" / "index.rst"
        props_index_lines = [
            f":canonical_id: {book_roman}.propositions",
            f":book: {book_roman}",
            ":type: section",
            f":title: Book {book_roman} Propositions",
            "",
            _make_heading(f"BOOK {book_roman}. PROPOSITIONS.", "="),
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "",
        ] + [f"   {entry}" for entry in prop_toc_entries]
        props_index_path.write_text("\n".join(props_index_lines) + "\n", encoding="utf-8")
        written_files.append(props_index_path)
        toc_entries.append("propositions/index")

    # 5. Write Book index.rst
    book_index_path = book_out_dir / "index.rst"
    book_index_lines = [
        f":canonical_id: {book_roman}",
        f":book: {book_roman}",
        ":type: book",
        f":title: Book {book_roman}",
        "",
        _make_heading(f"BOOK {book_roman}.", "="),
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "",
    ] + [f"   {entry}" for entry in toc_entries]
    book_index_path.write_text("\n".join(book_index_lines) + "\n", encoding="utf-8")
    written_files.append(book_index_path)

    # Validate all generated .rst files
    warnings_by_file: Dict[str, List[str]] = {}
    for wf in written_files:
        warns = validate_rst(wf.read_text(encoding="utf-8"))
        if warns:
            warnings_by_file[str(wf)] = warns

    return {
        "book": book_roman,
        "input_folios": len(folio_files),
        "propositions_compiled": len(propositions),
        "propositions_with_commentary": props_with_comm,
        "rst_files_written": len(written_files),
        "warnings_by_file": warnings_by_file,
    }
