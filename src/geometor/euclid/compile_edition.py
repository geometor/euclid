"""De-Pagination and Edition Compiler for GEOMETOR Euclid (Heath Edition).

Reads sequential ``<folio>.rst`` files across Volumes I, II, and III of
``resources/heath/``, detects logical unit headers (chapters, introductions,
definitions, postulates, common notions, propositions, lemmas, excursuses,
appendices, indices), stitches blocks across folio boundaries with
``.. folio::`` milestones, heals mid-sentence page-break splits, separates
Heath's commentary into companion ``commentary.rst`` files linked via
``:ref:``, generates the scholarly apparatus pages (``bibliography.rst``,
``persons.rst``, ``glossary.rst``), and writes the canonical Heath Edition
under ``docsrc/heath/``.
"""

from __future__ import annotations

import json
import re
import shutil
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from photon_platform.publish.rst_renderer import parse_rst_metadata

from geometor.euclid.folio_review.rst_utils import validate_rst


_ADORNMENT_RE = re.compile(r"^([=!~^\"'`#*+\-_])\1{2,}\s*$")
_TERMINAL_PUNCT = (".", "!", "?", ":", ";", "”", '"', "'", "’", ")", "]")
_PICTURE_RE = re.compile(r"^\.\.\s+picture::\s+(\S+)", re.MULTILINE)
_JUST_ROLE_TARGET_RE = re.compile(r":just:`[^`<]*<([^>]+)>`")
_DIR_JUST_TARGET_RE = re.compile(
    r"^\.\.\s+(?:assertion|subclause|sub-clause)::[ \t]+[^\n<]*<([^>\n]+)>",
    re.MULTILINE,
)
_FN_DEF_RE = re.compile(r"^\.\.\s+\[#([^\]]+)\]\s*(.*)", re.DOTALL)
_FN_REF_RE = re.compile(r"\[#([^\]]+)\]_")

_BOOK_SLUGS_BY_VOLUME: Dict[str, List[Tuple[str, str]]] = {
    "volume_I": [
        ("book_i", "I"),
        ("book_ii", "II"),
    ],
    "volume_II": [
        ("book_iii", "III"),
        ("book_iv", "IV"),
        ("book_v", "V"),
        ("book_vi", "VI"),
        ("book_vii", "VII"),
        ("book_viii", "VIII"),
        ("book_ix", "IX"),
    ],
    "volume_III": [
        ("book_x", "X"),
        ("book_xi", "XI"),
        ("book_xii", "XII"),
        ("book_xiii", "XIII"),
    ],
}

_VOLUME_ROMAN: Dict[str, str] = {
    "volume_I": "I",
    "volume_II": "II",
    "volume_III": "III",
}

_INTRO_CHAPTERS: List[Tuple[str, str, str]] = [
    ("chapter_i", "I", "Chapter I: Euclid and the Traditions About Him"),
    ("chapter_ii", "II", "Chapter II: Euclid's Other Works"),
    ("chapter_iii", "III", "Chapter III: Greek Commentators Other Than Proclus"),
    ("chapter_iv", "IV", "Chapter IV: Proclus and His Sources"),
    ("chapter_v", "V", "Chapter V: The Text"),
    ("chapter_vi", "VI", "Chapter VI: The Scholia"),
    ("chapter_vii", "VII", "Chapter VII: Euclid in Arabia"),
    ("chapter_viii", "VIII", "Chapter VIII: Principal Translations and Editions"),
    ("chapter_ix", "IX", "Chapter IX: The Nature of Elements"),
]


@dataclass
class TaggedBlock:
    """A single RST block tagged with its originating folio and page number."""

    text: str
    folio: str
    page: str
    source_dir: Path


def _apparatus_slug(key: str) -> str:
    """Create a deterministic anchor slug matching photon_platform.publish.roles.geometry."""
    return re.sub(r"[^a-z0-9]+", "-", (key or "").lower()).strip("-")


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
    if (
        p_strip.endswith("-")
        and not p_strip.endswith("--")
        and n_strip
        and n_strip[0].islower()
    ):
        return p_strip[:-1] + n_strip
    return f"{p_strip}\n{n_strip}"


def _parse_folio_blocks(
    rst_path: Path,
    namespace_footnotes: bool = False,
) -> Tuple[Dict[str, Any], List[TaggedBlock]]:
    """Parse a <folio>.rst file into (metadata, list of TaggedBlock)."""
    raw = rst_path.read_text(encoding="utf-8")
    meta, body = parse_rst_metadata(raw)
    folio = str(meta.get("folio", rst_path.stem)).strip()
    page = str(meta.get("page", "")).strip()

    if namespace_footnotes:
        # Namespace per-page #f1, #f2 footnotes by folio ID so multi-folio sections never collide
        body = re.sub(r"\[#(f\d+)\](_?)", rf"[#f{folio}_\1]\2", body)

    raw_blocks = re.split(r"\n\s*\n", body.strip())
    blocks: List[TaggedBlock] = []
    idx = 0
    n = len(raw_blocks)

    while idx < n:
        blk = raw_blocks[idx].strip("\n")
        if not blk.strip():
            idx += 1
            continue

        # Keep a directive header (`.. name::`) or footnote (`.. [#...]`) and its indented body together
        first_line = blk.splitlines()[0].strip()
        if re.match(r"^\.\.\s+(?:[a-zA-Z0-9_-]+::|\[#[^\]]+\])", first_line):
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
    vol_roman: str = "I",
    seen_folio_anchors: Optional[Set[Tuple[str, str]]] = None,
) -> Tuple[str, List[str], List[str], Set[Tuple[Path, str]]]:
    """Assemble tagged blocks into RST text, inserting .. folio:: milestones and healing page breaks.

    Separates footnote definitions (`.. [#...]`) from body blocks before healing so that
    bottom-of-page footnotes never block mid-sentence paragraph healing across folio breaks,
    and places all footnote definitions cleanly at the bottom of the compiled unit.
    """
    out_blocks: List[str] = []
    folios_seen: List[str] = []
    pages_seen: List[str] = []
    media_files: Set[Tuple[Path, str]] = set()

    body_blocks: List[TaggedBlock] = []
    footnotes_by_label: Dict[str, str] = {}

    for b in blocks:
        for m_pic in _PICTURE_RE.finditer(b.text):
            fname = m_pic.group(1).strip()
            media_files.add((b.source_dir, fname))

        if b.folio and b.folio not in folios_seen:
            folios_seen.append(b.folio)
        if b.page and b.page not in pages_seen:
            pages_seen.append(b.page)

        m_fn = _FN_DEF_RE.match(b.text)
        if m_fn:
            fn_label = m_fn.group(1).strip()
            fn_rest = m_fn.group(2).strip()
            if fn_label in footnotes_by_label:
                # Continuation footnote (e.g. `(*Continued from p. 294*)` on 0301.rst)
                cont_body = re.sub(
                    r"^\(\*Continued from p\.[^*]+\*\)\s*",
                    "",
                    fn_rest,
                    flags=re.IGNORECASE,
                ).strip()
                if cont_body:
                    indented = "\n".join(
                        f"   {line}" if line.strip() else ""
                        for line in cont_body.splitlines()
                    )
                    footnotes_by_label[fn_label] = (
                        f"{footnotes_by_label[fn_label]}\n\n{indented}"
                    )
            else:
                footnotes_by_label[fn_label] = b.text
        else:
            body_blocks.append(b)

    current_folio: Optional[str] = None

    for b in body_blocks:
        is_new_folio = b.folio != current_folio
        if is_new_folio:
            milestone_lines: List[str] = []
            if seen_folio_anchors is not None and b.folio:
                anchor_key = (vol_roman.lower(), b.folio)
                if anchor_key not in seen_folio_anchors:
                    seen_folio_anchors.add(anchor_key)
                    milestone_lines.append(f".. _folio-{vol_roman.lower()}-{b.folio}:")
                    milestone_lines.append("")
            milestone_lines.append(f".. folio:: {b.folio}")
            if b.page:
                milestone_lines.append(f"   :page: {b.page}")
            milestone = "\n".join(milestone_lines)

            if out_blocks and _should_heal_paragraphs(out_blocks[-1], b.text):
                out_blocks[-1] = _merge_split_paragraphs(out_blocks[-1], b.text)
                out_blocks.append(milestone)
            else:
                out_blocks.append(milestone)
                out_blocks.append(b.text)
            current_folio = b.folio
        else:
            out_blocks.append(b.text)

    for fn_text in footnotes_by_label.values():
        out_blocks.append(fn_text)

    return "\n\n".join(out_blocks), folios_seen, pages_seen, media_files


def _normalize_unit_headings(
    blocks: List[TaggedBlock],
    merge_subtitle: bool = False,
) -> List[TaggedBlock]:
    """Ensure a compiled unit has a single top-level '=' heading and clean subsection levels."""
    cleaned = list(blocks)
    while cleaned and cleaned[0].text == "----":
        cleaned.pop(0)
    while cleaned and cleaned[-1].text == "----":
        cleaned.pop()

    if not cleaned:
        return cleaned

    # Strip redundant 'INTRODUCTION.' banner at the start of chapter_i
    h0 = _is_heading_block(cleaned[0].text)
    if h0 and h0[0].upper().strip() == "INTRODUCTION." and len(cleaned) > 1:
        cleaned.pop(0)

    if merge_subtitle and len(cleaned) >= 2:
        h_first = _is_heading_block(cleaned[0].text)
        h_second = _is_heading_block(cleaned[1].text)
        if h_first and h_second:
            merged_title = f"{h_first[0].rstrip('.')} — {h_second[0]}"
            cleaned[0] = TaggedBlock(
                text=_make_heading(merged_title, "="),
                folio=cleaned[0].folio,
                page=cleaned[0].page,
                source_dir=cleaned[0].source_dir,
            )
            cleaned.pop(1)

    seen_first_heading = False
    for i, b in enumerate(cleaned):
        h = _is_heading_block(b.text)
        if h:
            htitle, hchar = h
            if not seen_first_heading:
                cleaned[i] = TaggedBlock(
                    text=_make_heading(htitle, "="),
                    folio=b.folio,
                    page=b.page,
                    source_dir=b.source_dir,
                )
                seen_first_heading = True
            elif hchar == "=":
                cleaned[i] = TaggedBlock(
                    text=_make_heading(htitle, "-"),
                    folio=b.folio,
                    page=b.page,
                    source_dir=b.source_dir,
                )

    return cleaned


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
    """Split a proposition's blocks into (proof_blocks, commentary_blocks) and route footnotes."""
    cleaned = list(blocks)
    while cleaned and cleaned[0].text == "----":
        cleaned.pop(0)
    while cleaned and cleaned[-1].text == "----":
        cleaned.pop()

    # Extract footnote definition blocks so we can route them to whichever half references them
    fn_defs: List[Tuple[str, TaggedBlock]] = []
    non_fn_blocks: List[TaggedBlock] = []
    for b in cleaned:
        m_fn = _FN_DEF_RE.match(b.text)
        if m_fn:
            fn_defs.append((m_fn.group(1).strip(), b))
        else:
            non_fn_blocks.append(b)

    while non_fn_blocks and non_fn_blocks[-1].text == "----":
        non_fn_blocks.pop()

    # Convert any plain-paragraph [PORISM. ...] into .. porism:: directive
    for i, b in enumerate(non_fn_blocks):
        cand = b.text
        if (
            cand.lstrip().upper().startswith(("[PORISM", "PORISM."))
            and not cand.startswith(".. porism::")
            and not _is_heading_block(cand)
        ):
            inner_p = re.sub(r"^(:line:`\d+`\s*)?\[?PORISM\.?\s*", r"\1", cand, flags=re.I)
            inner_p = inner_p.rstrip("]")
            indented_p = "\n".join(
                f"   {line}" if line.strip() else ""
                for line in inner_p.strip().splitlines()
            )
            non_fn_blocks[i] = TaggedBlock(
                text=f".. porism::\n\n{indented_p}",
                folio=b.folio,
                page=b.page,
                source_dir=b.source_dir,
            )

    divs = [i for i, b in enumerate(non_fn_blocks) if b.text == "----"]
    qeds = [i for i, b in enumerate(non_fn_blocks) if b.text.startswith(".. qed::")]

    if divs:
        # The first horizontal divider separates Euclid's text (proof + any immediate Porism/Lemma) from Heath's commentary
        split_idx = divs[0]
    elif qeds:
        split_idx = qeds[-1] + 1
        while split_idx < len(non_fn_blocks) and non_fn_blocks[split_idx].text.startswith(
            ".. porism::"
        ):
            split_idx += 1
    else:
        # Check if commentary starts at the top of a second folio (e.g. III.17, IV.1, IV.8, VIII.13, X.109)
        folios_in_prop = []
        for b in non_fn_blocks:
            if b.folio not in folios_in_prop:
                folios_in_prop.append(b.folio)
        last_txt = non_fn_blocks[-1].text if non_fn_blocks else ""
        if (
            len(folios_in_prop) > 1
            and _is_plain_paragraph(last_txt)
            and not last_txt.lstrip().startswith("Therefore")
            and "which is impossible" not in last_txt
            and "which was proved absurd" not in last_txt
        ):
            first_folio = non_fn_blocks[0].folio
            split_idx = next(
                (i for i, b in enumerate(non_fn_blocks) if b.folio != first_folio),
                len(non_fn_blocks),
            )
        else:
            split_idx = len(non_fn_blocks)

    proof_blocks = list(non_fn_blocks[:split_idx])
    comm_blocks = list(non_fn_blocks[split_idx:])

    while comm_blocks and comm_blocks[0].text == "----":
        comm_blocks.pop(0)
    while comm_blocks and comm_blocks[-1].text == "----":
        comm_blocks.pop()

    # Route footnote definitions to proof_blocks and/or comm_blocks based on where they are referenced
    proof_text = "\n\n".join(b.text for b in proof_blocks)
    comm_text = "\n\n".join(b.text for b in comm_blocks)
    proof_refs = set(_FN_REF_RE.findall(proof_text))
    comm_refs = set(_FN_REF_RE.findall(comm_text))

    for fn_label, fn_blk in fn_defs:
        in_proof = fn_label in proof_refs
        in_comm = fn_label in comm_refs
        if in_proof:
            proof_blocks.append(fn_blk)
        if in_comm or (not in_proof and comm_blocks):
            comm_blocks.append(fn_blk)
        elif not in_proof and not comm_blocks:
            proof_blocks.append(fn_blk)

    return proof_blocks, comm_blocks


def _write_unit_files(
    out_dir: Path,
    canonical_id: str,
    vol_roman: str,
    unit_type: str,
    title: str,
    main_blocks: List[TaggedBlock],
    comm_blocks: Optional[List[TaggedBlock]] = None,
    book_roman: Optional[str] = None,
    prop_num: Optional[int] = None,
    order: Optional[int] = None,
    seen_folio_anchors: Optional[Set[Tuple[str, str]]] = None,
    extra_lead_text: Optional[str] = None,
    extra_hidden_toctree: Optional[List[str]] = None,
) -> List[Path]:
    """Write index.rst (and commentary.rst if comm_blocks is non-empty) into out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    written: List[Path] = []
    comm_blocks = comm_blocks or []

    main_body, main_folios, main_pages, main_media = _render_blocks_with_milestones(
        main_blocks,
        vol_roman=vol_roman,
        seen_folio_anchors=seen_folio_anchors,
    )
    deps = _extract_dependencies(main_body)

    header_lines = [
        f":canonical_id: {canonical_id}",
        f":volume: {vol_roman}",
    ]
    if book_roman:
        header_lines.append(f":book: {book_roman}")
    if prop_num is not None:
        header_lines.append(f":proposition: {prop_num}")
    if order is not None:
        header_lines.append(f":order: {order}")
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
    ]
    if extra_lead_text:
        parts.append(extra_lead_text)
    parts.append(main_body)

    hidden_entries: List[str] = list(extra_hidden_toctree or [])
    if has_comm:
        parts.append("----")
        parts.append(f"See :ref:`Commentary on {title} <{comm_id}>`.")
        hidden_entries.append("commentary")

    if hidden_entries:
        toc_block = ".. toctree::\n   :hidden:\n\n" + "\n".join(
            f"   {e}" for e in hidden_entries
        )
        parts.append(toc_block)

    index_path = out_dir / "index.rst"
    index_path.write_text("\n\n".join(parts).rstrip() + "\n", encoding="utf-8")
    written.append(index_path)
    _copy_media_files(main_media, out_dir)

    if has_comm:
        norm_comm = list(comm_blocks)
        for i, b in enumerate(norm_comm):
            h = _is_heading_block(b.text)
            if h and h[1] == "=":
                norm_comm[i] = TaggedBlock(
                    text=_make_heading(h[0], "-"),
                    folio=b.folio,
                    page=b.page,
                    source_dir=b.source_dir,
                )
        comm_body, comm_folios, comm_pages, comm_media = _render_blocks_with_milestones(
            norm_comm,
            vol_roman=vol_roman,
            seen_folio_anchors=seen_folio_anchors,
        )
        comm_header = [
            f":canonical_id: {comm_id}",
            f":volume: {vol_roman}",
        ]
        if book_roman:
            comm_header.append(f":book: {book_roman}")
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
    else:
        stale_comm = out_dir / "commentary.rst"
        if stale_comm.exists():
            stale_comm.unlink()

    return written


def compile_section(
    section_src_dir: Path,
    section_out_dir: Path,
    canonical_id: str,
    vol_roman: str,
    section_type: str,
    title: str,
    merge_subtitle: bool = False,
    order: Optional[int] = None,
    seen_folio_anchors: Optional[Set[Tuple[str, str]]] = None,
) -> List[Path]:
    """Compile a sequential non-book section directory into section_out_dir/index.rst."""
    folio_files = sorted(
        [f for f in section_src_dir.glob("*.rst") if not f.name.endswith(".notes.rst")],
        key=lambda p: (int(p.stem) if p.stem.isdigit() else 999999, p.stem),
    )
    all_blocks: List[TaggedBlock] = []
    for fp in folio_files:
        _, f_blocks = _parse_folio_blocks(fp, namespace_footnotes=True)
        all_blocks.extend(f_blocks)

    norm_blocks = _normalize_unit_headings(all_blocks, merge_subtitle=merge_subtitle)

    extra_lead = None
    extra_toc: List[str] = []
    summary_md = section_src_dir / "summary.md"
    if summary_md.exists():
        section_out_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(summary_md, section_out_dir / "summary.md")
        extra_lead = f".. note::\n\n   See also the :doc:`Executive Summary and Outline <summary>` for {title}."
        extra_toc.append("summary")

    return _write_unit_files(
        out_dir=section_out_dir,
        canonical_id=canonical_id,
        vol_roman=vol_roman,
        unit_type=section_type,
        title=title,
        main_blocks=norm_blocks,
        order=order,
        seen_folio_anchors=seen_folio_anchors,
        extra_lead_text=extra_lead,
        extra_hidden_toctree=extra_toc,
    )

def _inject_numbered_item_anchors(
    blocks: List[TaggedBlock], prefix: str
) -> List[TaggedBlock]:
    """Prepend explicit Sphinx reference anchors (.. _<prefix>.<num>:) to numbered definition/postulate/CN blocks."""
    out: List[TaggedBlock] = []
    seen_nums: Set[str] = set()
    item_pat = re.compile(r"^(?:\[\d+\]\s*)?\[?(?:\*\*)?(\d+)\.(?:\*\*)?\s+")
    for b in blocks:
        m = item_pat.match(b.text.strip())
        if m:
            num = m.group(1)
            if num not in seen_nums:
                seen_nums.add(num)
                out.append(
                    TaggedBlock(
                        text=f".. _{prefix}.{num}:",
                        folio=b.folio,
                        page=b.page,
                        source_dir=b.source_dir,
                    )
                )
        out.append(b)
    return out


def compile_book(
    book_src_dir: Path,
    book_out_dir: Path,
    seen_folio_anchors: Optional[Set[Tuple[str, str]]] = None,
) -> Dict[str, Any]:
    """Compile all sequential <folio>.rst files in a book directory into canonical docsrc units."""
    folio_files = sorted(
        [f for f in book_src_dir.rglob("*.rst") if not f.name.endswith(".notes.rst")],
        key=lambda p: (int(p.stem) if p.stem.isdigit() else 999999, p.stem),
    )

    all_blocks: List[TaggedBlock] = []
    book_roman = "I"
    vol_roman = "I"
    for fp in folio_files:
        is_prop_dir = fp.parent.name == "propositions"
        meta, f_blocks = _parse_folio_blocks(fp, namespace_footnotes=not is_prop_dir)
        if meta.get("book"):
            book_roman = str(meta["book"]).strip()
        if meta.get("volume"):
            vol_roman = str(meta["volume"]).strip()
        all_blocks.extend(f_blocks)

    fp_sections: Dict[str, List[TaggedBlock]] = {
        "intro_note": [],
        "hist_note": [],
        "def_main": [],
        "post_main": [],
        "cn_main": [],
        "def_comm": [],
        "post_comm": [],
        "cn_comm": [],
        "def_ii": [],
        "def_iii": [],
        "ancient_extensions": [],
    }
    propositions: Dict[int, List[TaggedBlock]] = {}

    current_bucket: Optional[str] = None
    current_prop: Optional[int] = None

    for b in all_blocks:
        h = _is_heading_block(b.text)
        if h:
            htitle = h[0].upper().strip()
            # Skip top-level BOOK I. / BOOK I. PROPOSITIONS. banner headings
            if re.match(r"^BOOK\s+[IVXLCDM]+\.?(?:\s+PROPOSITIONS\.?)?$", htitle):
                continue

            m_prop = re.match(r"^\[?PROPOSITION\s+(\d+)\.?\]?$", htitle)
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

            # Special Book X sections inside propositions directory
            if htitle == "DEFINITIONS II.":
                current_prop = None
                current_bucket = "def_ii"
            elif htitle == "DEFINITIONS III.":
                current_prop = None
                current_bucket = "def_iii"
            elif htitle.startswith("ANCIENT EXTENSIONS OF THE THEORY OF BOOK X"):
                current_prop = None
                current_bucket = "ancient_extensions"
            elif current_prop is None:
                if htitle == "INTRODUCTORY NOTE.":
                    current_bucket = "intro_note"
                elif htitle == "HISTORICAL NOTE." and current_bucket is None:
                    current_bucket = "hist_note"
                elif htitle == "DEFINITIONS.":
                    current_bucket = "def_main"
                elif htitle == "POSTULATES.":
                    current_bucket = "post_main"
                elif htitle == "COMMON NOTIONS.":
                    current_bucket = "cn_main"
                elif re.match(r"^\[?DEFINITIONS?\s+\d+", htitle) and current_bucket in (
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

    # 0. Introductory Note / Historical Note
    if fp_sections["intro_note"]:
        norm_intro = _normalize_unit_headings(fp_sections["intro_note"])
        written_files.extend(
            _write_unit_files(
                out_dir=book_out_dir / "introductory_note",
                canonical_id=f"{book_roman}.intro",
                vol_roman=vol_roman,
                book_roman=book_roman,
                unit_type="introductory_note",
                title=f"Book {book_roman} Introductory Note",
                main_blocks=norm_intro,
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        toc_entries.append("introductory_note/index")

    if fp_sections["hist_note"]:
        norm_hist = _normalize_unit_headings(fp_sections["hist_note"])
        written_files.extend(
            _write_unit_files(
                out_dir=book_out_dir / "historical_note",
                canonical_id=f"{book_roman}.intro",
                vol_roman=vol_roman,
                book_roman=book_roman,
                unit_type="historical_note",
                title=f"Book {book_roman} Historical Note",
                main_blocks=norm_hist,
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        toc_entries.append("historical_note/index")

    # 1. Write Definitions
    if fp_sections["def_main"]:
        norm_def = _inject_numbered_item_anchors(
            _normalize_unit_headings(fp_sections["def_main"]),
            f"{book_roman}.def",
        )
        norm_def_comm = list(fp_sections["def_comm"])
        while norm_def_comm and norm_def_comm[0].text == "----":
            norm_def_comm.pop(0)
        while norm_def_comm and norm_def_comm[-1].text == "----":
            norm_def_comm.pop()
        written_files.extend(
            _write_unit_files(
                out_dir=book_out_dir / "definitions",
                canonical_id=f"{book_roman}.def",
                vol_roman=vol_roman,
                book_roman=book_roman,
                unit_type="definitions",
                title=f"Book {book_roman} Definitions",
                main_blocks=norm_def,
                comm_blocks=norm_def_comm,
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        toc_entries.append("definitions/index")

    # 2. Write Postulates
    if fp_sections["post_main"]:
        norm_post = _inject_numbered_item_anchors(
            _normalize_unit_headings(fp_sections["post_main"]),
            f"{book_roman}.post",
        )
        norm_post_comm = list(fp_sections["post_comm"])
        while norm_post_comm and norm_post_comm[0].text == "----":
            norm_post_comm.pop(0)
        while norm_post_comm and norm_post_comm[-1].text == "----":
            norm_post_comm.pop()
        written_files.extend(
            _write_unit_files(
                out_dir=book_out_dir / "postulates",
                canonical_id=f"{book_roman}.post",
                vol_roman=vol_roman,
                book_roman=book_roman,
                unit_type="postulates",
                title=f"Book {book_roman} Postulates",
                main_blocks=norm_post,
                comm_blocks=norm_post_comm,
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        toc_entries.append("postulates/index")

    # 3. Write Common Notions
    if fp_sections["cn_main"]:
        norm_cn = _inject_numbered_item_anchors(
            _normalize_unit_headings(fp_sections["cn_main"]),
            f"{book_roman}.cn",
        )
        norm_cn_comm = list(fp_sections["cn_comm"])
        while norm_cn_comm and norm_cn_comm[0].text == "----":
            norm_cn_comm.pop(0)
        while norm_cn_comm and norm_cn_comm[-1].text == "----":
            norm_cn_comm.pop()
        written_files.extend(
            _write_unit_files(
                out_dir=book_out_dir / "common_notions",
                canonical_id=f"{book_roman}.cn",
                vol_roman=vol_roman,
                book_roman=book_roman,
                unit_type="common_notions",
                title=f"Book {book_roman} Common Notions",
                main_blocks=norm_cn,
                comm_blocks=norm_cn_comm,
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        toc_entries.append("common_notions/index")

    # 3b. Book X Definitions II & III
    if fp_sections["def_ii"]:
        norm_def_ii = _inject_numbered_item_anchors(
            _normalize_unit_headings(fp_sections["def_ii"]),
            f"{book_roman}.def.ii",
        )
        written_files.extend(
            _write_unit_files(
                out_dir=book_out_dir / "definitions_ii",
                canonical_id=f"{book_roman}.def.ii",
                vol_roman=vol_roman,
                book_roman=book_roman,
                unit_type="definitions",
                title=f"Book {book_roman} Definitions II",
                main_blocks=norm_def_ii,
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        toc_entries.append("definitions_ii/index")

    if fp_sections["def_iii"]:
        norm_def_iii = _inject_numbered_item_anchors(
            _normalize_unit_headings(fp_sections["def_iii"]),
            f"{book_roman}.def.iii",
        )
        written_files.extend(
            _write_unit_files(
                out_dir=book_out_dir / "definitions_iii",
                canonical_id=f"{book_roman}.def.iii",
                vol_roman=vol_roman,
                book_roman=book_roman,
                unit_type="definitions",
                title=f"Book {book_roman} Definitions III",
                main_blocks=norm_def_iii,
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        toc_entries.append("definitions_iii/index")

    # 4. Write Propositions
    prop_toc_entries: List[str] = []
    props_with_comm = 0
    max_prop = max(propositions.keys()) if propositions else 0
    pad_width = 3 if max_prop >= 100 else 2

    for pnum in sorted(propositions.keys()):
        p_blocks = propositions[pnum]
        proof_blocks, comm_blocks = _split_proposition_proof_and_commentary(p_blocks)
        proof_blocks = _normalize_unit_headings(proof_blocks)
        has_pic = any(_PICTURE_RE.search(b.text) for b in proof_blocks)
        if not has_pic and proof_blocks:
            for b in proof_blocks:
                m_g = re.search(r"<(\d{4}\.g\d+):", b.text)
                if m_g:
                    gid = m_g.group(1)
                    svg_name = f"{gid}.svg"
                    if (b.source_dir / svg_name).exists():
                        insert_idx = 1
                        for idx_b, pb in enumerate(proof_blocks):
                            if pb.text.strip().startswith(".. enunciation::"):
                                insert_idx = idx_b + 1
                                break
                        proof_blocks.insert(
                            insert_idx,
                            TaggedBlock(
                                text=f".. picture:: {svg_name}\n   :alt: Proposition {pnum} figure",
                                folio=b.folio,
                                page=b.page,
                                source_dir=b.source_dir,
                            ),
                        )
                        break
        if comm_blocks:
            props_with_comm += 1
        p_dir_name = f"{pnum:0{pad_width}d}"
        p_out_dir = book_out_dir / "propositions" / p_dir_name
        written_files.extend(
            _write_unit_files(
                out_dir=p_out_dir,
                canonical_id=f"{book_roman}.{pnum}",
                vol_roman=vol_roman,
                book_roman=book_roman,
                unit_type="proposition",
                title=f"Proposition {book_roman}.{pnum}",
                main_blocks=proof_blocks,
                comm_blocks=comm_blocks,
                prop_num=pnum,
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        prop_toc_entries.append(f"{p_dir_name}/index")

    if prop_toc_entries:
        props_index_path = book_out_dir / "propositions" / "index.rst"
        props_index_lines = [
            f":canonical_id: {book_roman}.propositions",
            f":volume: {vol_roman}",
            f":book: {book_roman}",
            ":type: section",
            f":title: Book {book_roman} Propositions",
            "",
            _make_heading(f"BOOK {book_roman}. PROPOSITIONS.", "="),
            "",
            ".. collection::",
            "   :type: proposition",
            "   :sort: proposition",
        ]
        props_index_path.write_text("\n".join(props_index_lines) + "\n", encoding="utf-8")
        written_files.append(props_index_path)
        toc_entries.append("propositions/index")

    # 4b. Book X Ancient Extensions
    if fp_sections["ancient_extensions"]:
        norm_ext = _normalize_unit_headings(fp_sections["ancient_extensions"])
        written_files.extend(
            _write_unit_files(
                out_dir=book_out_dir / "ancient_extensions",
                canonical_id=f"{book_roman}.ancient_extensions",
                vol_roman=vol_roman,
                book_roman=book_roman,
                unit_type="section",
                title="Ancient Extensions of the Theory of Book X",
                main_blocks=norm_ext,
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        toc_entries.append("ancient_extensions/index")

    # 5. Write Book index.rst
    book_index_path = book_out_dir / "index.rst"
    book_index_lines = [
        f":canonical_id: {book_roman}",
        f":volume: {vol_roman}",
        f":book: {book_roman}",
        ":type: book",
        f":title: Book {book_roman}",
        "",
        f".. _Book-{book_roman}:",
        "",
        _make_heading(f"BOOK {book_roman}.", "="),
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "",
    ] + [f"   {entry}" for entry in toc_entries]
    book_index_path.write_text("\n".join(book_index_lines) + "\n", encoding="utf-8")
    written_files.append(book_index_path)

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


def _format_folio_occurrence_links(
    occurrences: List[Dict[str, Any]],
    seen_folio_anchors: Set[Tuple[str, str]],
    max_links: int = 25,
) -> List[str]:
    """Format deduplicated :ref: links to folio milestones for apparatus entries."""
    seen: Set[Tuple[str, str]] = set()
    links: List[str] = []
    for occ in occurrences:
        vol_dir = str(occ.get("volume", "")).strip()
        vol_roman = _VOLUME_ROMAN.get(vol_dir, vol_dir.replace("volume_", ""))
        folio = str(occ.get("folio", "")).strip()
        page = str(occ.get("page", "")).strip()
        if not folio or (vol_roman.lower(), folio) in seen:
            continue
        seen.add((vol_roman.lower(), folio))
        label = f"Vol. {vol_roman}, p. {page}" if page else f"Vol. {vol_roman}, [{folio}]"
        if (vol_roman.lower(), folio) in seen_folio_anchors:
            links.append(f":ref:`{label} <folio-{vol_roman.lower()}-{folio}>`")
        else:
            links.append(label)
    if len(links) > max_links:
        extra = len(links) - max_links
        links = links[:max_links] + [f"*...and {extra} more*"]
    return links


def build_apparatus_pages(
    heath_src_dir: Path,
    heath_out_dir: Path,
    seen_folio_anchors: Set[Tuple[str, str]],
) -> List[Path]:
    """Generate bibliography.rst, persons.rst, and glossary.rst from JSON registries."""
    written: List[Path] = []
    citations_path = heath_src_dir / "citations.json"
    persons_path = heath_src_dir / "persons.json"
    glossary_path = heath_src_dir / "glossary.json"

    citations: Dict[str, Any] = (
        json.loads(citations_path.read_text(encoding="utf-8"))
        if citations_path.exists()
        else {}
    )
    persons: Dict[str, Any] = (
        json.loads(persons_path.read_text(encoding="utf-8"))
        if persons_path.exists()
        else {}
    )
    glossary: Dict[str, Any] = (
        json.loads(glossary_path.read_text(encoding="utf-8"))
        if glossary_path.exists()
        else {}
    )

    # 1. Bibliography
    works_by_author: Dict[str, Dict[str, List[Dict[str, Any]]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for ckey, cdata in citations.items():
        author_key = cdata.get("author_key") or "unknown"
        work_key = cdata.get("work_key") or ckey
        works_by_author[author_key][work_key].append(cdata)

    def _author_sort_key(akey: str) -> str:
        if akey in persons:
            return persons[akey].get("name", akey).lower()
        sample_work = next(iter(works_by_author[akey].values()))[0]
        return (sample_work.get("author") or akey).lower()

    bib_lines: List[str] = [
        ":order: 90",
        ":type: apparatus",
        ":title: Bibliography & Cited Works",
        "",
        ".. _bibliography:",
        "",
        "===========================",
        "Bibliography & Cited Works",
        "===========================",
        "",
        "Classical, medieval, and modern works cited in Sir Thomas L. Heath's",
        "*The Thirteen Books of Euclid's Elements*, grouped by author and work",
        "with direct links to cited loci and folio milestones.",
        "",
    ]

    emitted_cite_slugs: Set[str] = set()
    emitted_work_slugs: Dict[str, str] = {}
    work_title_to_slug: Dict[str, str] = {}
    author_work_title_to_slug: Dict[Tuple[str, str], str] = {}

    for akey in sorted(works_by_author.keys(), key=_author_sort_key):
        pinfo = persons.get(akey)
        author_name = (
            pinfo["name"]
            if pinfo
            else (
                next(iter(works_by_author[akey].values()))[0].get("author")
                or akey.replace("-", " ").title()
            )
        )
        dates = pinfo.get("dates", "") if pinfo else ""
        heading_text = f"{author_name} ({dates})" if dates else author_name
        bib_lines.append(_make_heading(heading_text, "-"))
        bib_lines.append("")
        if akey in persons:
            bib_lines.append(f"See bio in :person:`{author_name} <{akey}>`.")
            bib_lines.append("")

        for wkey, loci_entries in sorted(works_by_author[akey].items()):
            wtitle = loci_entries[0].get("work") or wkey
            w_slug = _apparatus_slug(wkey)
            emitted_work_slugs[w_slug] = wtitle
            work_title_to_slug.setdefault(wtitle.lower(), w_slug)
            author_work_title_to_slug[(akey, wtitle.lower())] = w_slug

            bib_lines.append(f".. _work-{w_slug}:")
            if w_slug not in emitted_cite_slugs:
                bib_lines.append(f".. _cite-{w_slug}:")
                emitted_cite_slugs.add(w_slug)
            bib_lines.append("")
            bib_lines.append(f"**{wtitle}** (``{wkey}``)")
            bib_lines.append("")

            for entry in sorted(loci_entries, key=lambda x: x.get("locus", "")):
                ckey = entry["key"]
                c_slug = _apparatus_slug(ckey)
                locus = entry.get("locus") or ""
                occs = entry.get("occurrences", [])
                folio_links = _format_folio_occurrence_links(occs, seen_folio_anchors)
                if not folio_links:
                    continue
                if c_slug not in emitted_cite_slugs:
                    bib_lines.append(f".. _cite-{c_slug}:")
                    bib_lines.append("")
                    emitted_cite_slugs.add(c_slug)
                if locus:
                    bib_lines.append(
                        f"- ``{locus}`` — Cited on {', '.join(folio_links)}"
                    )
                else:
                    bib_lines.append(
                        f"- *General reference* — Cited on {', '.join(folio_links)}"
                    )
                bib_lines.append("")

    bib_path = heath_out_dir / "bibliography.rst"
    bib_path.write_text("\n".join(bib_lines).rstrip() + "\n", encoding="utf-8")
    written.append(bib_path)

    # 2. Persons
    persons_lines: List[str] = [
        ":order: 91",
        ":type: apparatus",
        ":title: Index of Persons",
        "",
        ".. _persons:",
        "",
        "================",
        "Index of Persons",
        "================",
        "",
        "Biographical and scholarly index of geometers, philosophers, commentators,",
        "translators, and historians cited across Volumes I–III of Heath's edition.",
        "",
    ]

    for pkey, pdata in sorted(
        persons.items(), key=lambda kv: kv[1].get("name", kv[0]).lower()
    ):
        p_slug = _apparatus_slug(pkey)
        pname = pdata.get("name", pkey)
        pdates = pdata.get("dates", "")
        prole = pdata.get("role", "")
        pbio = pdata.get("bio", "")
        pworks = pdata.get("works", [])
        occs = pdata.get("occurrences", [])

        persons_lines.append(f".. _person-{p_slug}:")
        persons_lines.append("")
        h_text = f"{pname} ({pdates})" if pdates else pname
        persons_lines.append(_make_heading(h_text, "-"))
        persons_lines.append("")
        if prole:
            persons_lines.append(f"*{prole}*")
            persons_lines.append("")
        if pbio:
            persons_lines.append(pbio)
            persons_lines.append("")
        if pworks:
            work_refs = []
            for wk in pworks:
                cand_slug = _apparatus_slug(wk)
                author_cand_slug = _apparatus_slug(f"{pkey}:{wk}")
                resolved_slug = None
                if cand_slug in emitted_work_slugs:
                    resolved_slug = cand_slug
                elif author_cand_slug in emitted_work_slugs:
                    resolved_slug = author_cand_slug
                elif (pkey, wk.lower()) in author_work_title_to_slug:
                    resolved_slug = author_work_title_to_slug[(pkey, wk.lower())]
                elif wk.lower() in work_title_to_slug:
                    resolved_slug = work_title_to_slug[wk.lower()]

                if resolved_slug:
                    w_title = emitted_work_slugs.get(resolved_slug, wk)
                    work_refs.append(f":ref:`{w_title} <work-{resolved_slug}>`")
                else:
                    work_refs.append(f"*{wk}*")
            persons_lines.append(f"**Cited Works:** {', '.join(work_refs)}")
            persons_lines.append("")
        folio_links = _format_folio_occurrence_links(occs, seen_folio_anchors)
        if folio_links:
            persons_lines.append(f"**Mentions:** {', '.join(folio_links)}")
            persons_lines.append("")

    persons_path = heath_out_dir / "persons.rst"
    persons_path.write_text("\n".join(persons_lines).rstrip() + "\n", encoding="utf-8")
    written.append(persons_path)

    # 3. Glossary
    glossary_lines: List[str] = [
        ":order: 92",
        ":type: apparatus",
        ":title: Glossary of Terms",
        "",
        ".. _glossary:",
        "",
        "============================================",
        "Glossary of Greek, Latin & Technical Terms",
        "============================================",
        "",
        "Greek, Latin, Arabic, and technical mathematical terms tagged across",
        "Heath's *Elements*, with translations and folio occurrences.",
        "",
    ]

    for tkey, tdata in sorted(glossary.items(), key=lambda kv: kv[0].lower()):
        t_slug = _apparatus_slug(tkey)
        headword = tdata.get("headword", tkey)
        lang = tdata.get("language", "")
        trans = tdata.get("translation", "")
        defn = tdata.get("definition", "")
        occs = tdata.get("occurrences", [])

        glossary_lines.append(f".. _term-{t_slug}:")
        glossary_lines.append("")
        h_text = f"{headword} ({tkey})" if headword != tkey else headword
        glossary_lines.append(_make_heading(h_text, "-"))
        glossary_lines.append("")
        meta_bits = []
        if lang:
            meta_bits.append(f"**Language:** {lang}")
        if trans:
            meta_bits.append(f"**Translation:** *{trans}*")
        if meta_bits:
            glossary_lines.append(" | ".join(meta_bits))
            glossary_lines.append("")
        if defn:
            glossary_lines.append(defn)
            glossary_lines.append("")
        folio_links = _format_folio_occurrence_links(occs, seen_folio_anchors)
        if folio_links:
            glossary_lines.append(f"**Occurrences:** {', '.join(folio_links)}")
            glossary_lines.append("")

    glossary_path = heath_out_dir / "glossary.rst"
    glossary_path.write_text("\n".join(glossary_lines).rstrip() + "\n", encoding="utf-8")
    written.append(glossary_path)

    return written


def compile_edition(
    heath_src_dir: Path = Path("resources/heath"),
    heath_out_dir: Path = Path("docsrc/heath"),
) -> Dict[str, Any]:
    """Compile the entire 3-volume Heath Edition and scholarly apparatus into docsrc/heath/."""
    heath_out_dir.mkdir(parents=True, exist_ok=True)

    # Clean legacy directories in docsrc/heath/
    legacy_names = [
        "I",
        "II",
        "III",
        "IV",
        "V",
        "VI",
        "VII",
        "VIII",
        "IX",
        "X",
        "XI",
        "XII",
        "XIII",
        "intro",
        "transcription",
        "_static",
        "TRANSCRIPTION_GUIDE.md",
    ]
    for name in legacy_names:
        cand = heath_out_dir / name
        if cand.is_dir():
            shutil.rmtree(cand)
        elif cand.is_file():
            cand.unlink()

    seen_folio_anchors: Set[Tuple[str, str]] = set()
    written_files: List[Path] = []
    book_stats: List[Dict[str, Any]] = []

    # =========================================================================
    # VOLUME I
    # =========================================================================
    v1_src = heath_src_dir / "volume_I"
    v1_out = heath_out_dir / "volume_I"
    v1_toc: List[str] = []

    if (v1_src / "euclids_elements").exists():
        written_files.extend(
            compile_section(
                v1_src / "euclids_elements",
                v1_out / "euclids_elements",
                canonical_id="VolI.frontmatter",
                vol_roman="I",
                section_type="frontmatter",
                title="Title Page & Frontispiece (Vol. I)",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v1_toc.append("euclids_elements/index")

    if (v1_src / "preface").exists():
        written_files.extend(
            compile_section(
                v1_src / "preface",
                v1_out / "preface",
                canonical_id="VolI.preface",
                vol_roman="I",
                section_type="preface",
                title="Preface",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v1_toc.append("preface/index")

    if (v1_src / "contents").exists():
        written_files.extend(
            compile_section(
                v1_src / "contents",
                v1_out / "contents",
                canonical_id="VolI.contents",
                vol_roman="I",
                section_type="contents",
                title="Contents of Volume I",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v1_toc.append("contents/index")

    if (v1_src / "introduction").exists():
        intro_out = v1_out / "introduction"
        for ch_idx, (ch_slug, ch_roman, ch_title) in enumerate(_INTRO_CHAPTERS, start=1):
            ch_src = v1_src / "introduction" / ch_slug
            if ch_src.exists():
                written_files.extend(
                    compile_section(
                        ch_src,
                        intro_out / ch_slug,
                        canonical_id=f"Intro.{ch_roman}",
                        vol_roman="I",
                        section_type="chapter",
                        title=ch_title,
                        merge_subtitle=True,
                        order=ch_idx,
                        seen_folio_anchors=seen_folio_anchors,
                    )
                )

        intro_index = intro_out / "index.rst"
        intro_index_lines = [
            ":canonical_id: Intro",
            ":volume: I",
            ":type: introduction",
            ":title: Introduction",
            "",
            ".. _Heath-Introduction:",
            "",
            _make_heading("INTRODUCTION.", "="),
            "",
            ".. collection::",
            "   :type: chapter",
            "   :sort: order",
        ]
        intro_index.write_text("\n".join(intro_index_lines) + "\n", encoding="utf-8")
        written_files.append(intro_index)
        v1_toc.append("introduction/index")

    for b_slug, _ in _BOOK_SLUGS_BY_VOLUME["volume_I"]:
        b_src = v1_src / b_slug
        if b_src.exists():
            st = compile_book(b_src, v1_out / b_slug, seen_folio_anchors=seen_folio_anchors)
            book_stats.append(st)
            v1_toc.append(f"{b_slug}/index")

    if (v1_src / "excursus_i").exists():
        written_files.extend(
            compile_section(
                v1_src / "excursus_i",
                v1_out / "excursus_i",
                canonical_id="VolI.excursus.I",
                vol_roman="I",
                section_type="excursus",
                title="Excursus I: Pythagoras and the Pythagoreans",
                merge_subtitle=True,
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v1_toc.append("excursus_i/index")

    if (v1_src / "excursus_ii").exists():
        written_files.extend(
            compile_section(
                v1_src / "excursus_ii",
                v1_out / "excursus_ii",
                canonical_id="VolI.excursus.II",
                vol_roman="I",
                section_type="excursus",
                title="Excursus II: Popular Names for Euclidean Propositions",
                merge_subtitle=True,
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v1_toc.append("excursus_ii/index")

    if (v1_src / "index_of_greek_words_and_forms").exists():
        written_files.extend(
            compile_section(
                v1_src / "index_of_greek_words_and_forms",
                v1_out / "index_of_greek_words_and_forms",
                canonical_id="VolI.index.greek",
                vol_roman="I",
                section_type="index",
                title="Index of Greek Words and Forms (Vol. I)",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v1_toc.append("index_of_greek_words_and_forms/index")

    if (v1_src / "english_index").exists():
        written_files.extend(
            compile_section(
                v1_src / "english_index",
                v1_out / "english_index",
                canonical_id="VolI.index.english",
                vol_roman="I",
                section_type="index",
                title="English Index (Vol. I)",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v1_toc.append("english_index/index")

    v1_index = v1_out / "index.rst"
    v1_index_lines = [
        ":canonical_id: Volume.I",
        ":volume: I",
        ":type: volume",
        ":title: Volume I: Introduction and Books I, II",
        "",
        ".. _Volume-I:",
        "",
        _make_heading("VOLUME I: INTRODUCTION AND BOOKS I, II", "="),
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "",
    ] + [f"   {e}" for e in v1_toc]
    v1_index.write_text("\n".join(v1_index_lines) + "\n", encoding="utf-8")
    written_files.append(v1_index)

    # =========================================================================
    # VOLUME II
    # =========================================================================
    v2_src = heath_src_dir / "volume_II"
    v2_out = heath_out_dir / "volume_II"
    v2_toc: List[str] = []

    if (v2_src / "euclids_elements").exists():
        written_files.extend(
            compile_section(
                v2_src / "euclids_elements",
                v2_out / "euclids_elements",
                canonical_id="VolII.frontmatter",
                vol_roman="II",
                section_type="frontmatter",
                title="Title Page (Vol. II)",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v2_toc.append("euclids_elements/index")

    if (v2_src / "contents_of_volu_me_ii").exists():
        written_files.extend(
            compile_section(
                v2_src / "contents_of_volu_me_ii",
                v2_out / "contents",
                canonical_id="VolII.contents",
                vol_roman="II",
                section_type="contents",
                title="Contents of Volume II",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v2_toc.append("contents/index")

    for b_slug, _ in _BOOK_SLUGS_BY_VOLUME["volume_II"]:
        b_src = v2_src / b_slug
        if b_src.exists():
            st = compile_book(b_src, v2_out / b_slug, seen_folio_anchors=seen_folio_anchors)
            book_stats.append(st)
            v2_toc.append(f"{b_slug}/index")

    if (v2_src / "indexofgreekwordsandforms").exists():
        written_files.extend(
            compile_section(
                v2_src / "indexofgreekwordsandforms",
                v2_out / "index_of_greek_words_and_forms",
                canonical_id="VolII.index.greek",
                vol_roman="II",
                section_type="index",
                title="Index of Greek Words and Forms (Vol. II)",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v2_toc.append("index_of_greek_words_and_forms/index")

    if (v2_src / "englishindex").exists():
        written_files.extend(
            compile_section(
                v2_src / "englishindex",
                v2_out / "english_index",
                canonical_id="VolII.index.english",
                vol_roman="II",
                section_type="index",
                title="English Index (Vol. II)",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v2_toc.append("english_index/index")

    v2_index = v2_out / "index.rst"
    v2_index_lines = [
        ":canonical_id: Volume.II",
        ":volume: II",
        ":type: volume",
        ":title: Volume II: Books III–IX",
        "",
        ".. _Volume-II:",
        "",
        _make_heading("VOLUME II: BOOKS III–IX", "="),
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "",
    ] + [f"   {e}" for e in v2_toc]
    v2_index.write_text("\n".join(v2_index_lines) + "\n", encoding="utf-8")
    written_files.append(v2_index)

    # =========================================================================
    # VOLUME III
    # =========================================================================
    v3_src = heath_src_dir / "volume_III"
    v3_out = heath_out_dir / "volume_III"
    v3_toc: List[str] = []

    if (v3_src / "euclids_elements").exists():
        written_files.extend(
            compile_section(
                v3_src / "euclids_elements",
                v3_out / "euclids_elements",
                canonical_id="VolIII.frontmatter",
                vol_roman="III",
                section_type="frontmatter",
                title="Title Page (Vol. III)",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v3_toc.append("euclids_elements/index")

    if (v3_src / "contentsofvolumeiii").exists():
        written_files.extend(
            compile_section(
                v3_src / "contentsofvolumeiii",
                v3_out / "contents",
                canonical_id="VolIII.contents",
                vol_roman="III",
                section_type="contents",
                title="Contents of Volume III",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v3_toc.append("contents/index")

    for b_slug, _ in _BOOK_SLUGS_BY_VOLUME["volume_III"]:
        b_src = v3_src / b_slug
        if b_src.exists():
            st = compile_book(b_src, v3_out / b_slug, seen_folio_anchors=seen_folio_anchors)
            book_stats.append(st)
            v3_toc.append(f"{b_slug}/index")

    if (v3_src / "appendix").exists():
        written_files.extend(
            compile_section(
                v3_src / "appendix",
                v3_out / "appendix",
                canonical_id="VolIII.appendix",
                vol_roman="III",
                section_type="appendix",
                title="Appendix: Book XIV (by Hypsicles) & Note on Book XV",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v3_toc.append("appendix/index")

    if (v3_src / "general_index_of_greek_words").exists():
        written_files.extend(
            compile_section(
                v3_src / "general_index_of_greek_words",
                v3_out / "general_index_of_greek_words",
                canonical_id="VolIII.index.greek",
                vol_roman="III",
                section_type="index",
                title="General Index of Greek Words and Forms",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v3_toc.append("general_index_of_greek_words/index")

    if (v3_src / "general_index").exists():
        written_files.extend(
            compile_section(
                v3_src / "general_index",
                v3_out / "general_index",
                canonical_id="VolIII.index.general",
                vol_roman="III",
                section_type="index",
                title="General Index",
                seen_folio_anchors=seen_folio_anchors,
            )
        )
        v3_toc.append("general_index/index")

    v3_index = v3_out / "index.rst"
    v3_index_lines = [
        ":canonical_id: Volume.III",
        ":volume: III",
        ":type: volume",
        ":title: Volume III: Books X–XIII and Appendix",
        "",
        ".. _Volume-III:",
        "",
        _make_heading("VOLUME III: BOOKS X–XIII AND APPENDIX", "="),
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "",
    ] + [f"   {e}" for e in v3_toc]
    v3_index.write_text("\n".join(v3_index_lines) + "\n", encoding="utf-8")
    written_files.append(v3_index)

    # =========================================================================
    # APPARATUS PAGES (bibliography.rst, persons.rst, glossary.rst)
    # =========================================================================
    written_files.extend(
        build_apparatus_pages(heath_src_dir, heath_out_dir, seen_folio_anchors)
    )

    # =========================================================================
    # MASTER HEATH INDEX (docsrc/heath/index.rst)
    # =========================================================================
    heath_index = heath_out_dir / "index.rst"
    heath_index_lines = [
        ":navigation: header",
        ":order: 1",
        ":layout: book",
        ":book_title: The Thirteen Books of Euclid's Elements",
        ":book_subtitle: Translated from the Text of Heiberg with Introduction and Commentary",
        ":author: Sir Thomas L. Heath",
        ":publisher: Cambridge University Press / Dover Publications",
        ":year: 1926",
        "",
        "=============",
        "Heath Edition",
        "=============",
        "",
        "Sir Thomas L. Heath's *The Thirteen Books of Euclid's Elements* (Second Edition,",
        "revised with additions), reconstructed from the folio-reviewed diplomatic",
        "transcriptions with interactive geometric diagrams, symbolic justifications,",
        "and cross-referenced scholarly apparatus.",
        "",
        "Volumes",
        "-------",
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "",
        "   volume_I/index",
        "   volume_II/index",
        "   volume_III/index",
        "",
        "Scholarly Apparatus",
        "-------------------",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "",
        "   bibliography",
        "   persons",
        "   glossary",
    ]
    heath_index.write_text("\n".join(heath_index_lines) + "\n", encoding="utf-8")
    written_files.append(heath_index)

    # =========================================================================
    # DEPENDENCY GRAPHS (built from composed RST files in docsrc/heath/)
    # =========================================================================
    from geometor.euclid.graph import build_graph

    _, graph_stats = build_graph(heath_out_dir=heath_out_dir, inject_rst=True)

    total_props = sum(s["propositions_compiled"] for s in book_stats)
    total_comm = sum(s["propositions_with_commentary"] for s in book_stats)
    total_book_files = sum(s["rst_files_written"] for s in book_stats)
    all_warnings: Dict[str, List[str]] = {}
    for s in book_stats:
        all_warnings.update(s["warnings_by_file"])

    return {
        "books_compiled": len(book_stats),
        "propositions_compiled": total_props,
        "propositions_with_commentary": total_comm,
        "total_rst_files_written": len(written_files) + total_book_files,
        "folio_anchors_emitted": len(seen_folio_anchors),
        "dependency_graphs_injected": graph_stats["graphs_injected"],
        "required_for_injected": graph_stats["required_for_injected"],
        "warnings_by_file": all_warnings,
    }
