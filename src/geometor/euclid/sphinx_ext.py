"""Runtime Sphinx & photon-platform/publish integration for ``geometor.euclid``.

Registers the ``el`` ("Greek (Menge 1896)") companion track in
``photon_platform.publish.book`` at build time (without modifying
``photon-platform/publish`` or affecting ``docsrc/heath/``'s 2-track
``Proposition`` + ``Commentary`` pages) and configures offline-safe local
intersphinx inventories when sister GEOMETOR codices are present on disk.
"""

from __future__ import annotations

import os
from pathlib import Path
import re
from typing import Any

GREEK_TRACK_LABEL = "Greek (Menge 1896)"


def register_greek_book_track(label: str = GREEK_TRACK_LABEL) -> None:
    """Extend ``photon_platform.publish.book`` to recognize ``<stem>-el`` Greek tracks.

    Pages without an ``-el`` sibling (such as all pages in ``docsrc/heath/``)
    fall through immediately to the original ``detect_companion_tracks``
    implementation without modification.

    Args:
        label: Human-readable tab label for the Greek companion track.
    """
    try:
        from photon_platform.publish import book
    except ImportError:
        return

    el_pattern = (r"^(.+)[._-]el$", "el", label)
    if not any(key == "el" for _pat, key, _lbl in book._TRACK_SUFFIX_PATTERNS):
        book._TRACK_SUFFIX_PATTERNS.append(el_pattern)

    book._AUX_TRACK_BASENAMES.add("el")
    el_aux_re = re.compile(r"^.+[._-]el$")
    if not any(p.pattern == el_aux_re.pattern for p in book._AUX_TRACK_PATTERNS):
        book._AUX_TRACK_PATTERNS.append(el_aux_re)

    if getattr(book.detect_companion_tracks, "_euclid_data_el_patched", False):
        return

    orig_detect = book.detect_companion_tracks

    def _detect_with_greek(env: object, pagename: str) -> list[dict[str, Any]]:
        found_docs: set[str] = set(getattr(env, "found_docs", set()))
        if not found_docs:
            return []

        doc_dir = os.path.dirname(pagename)
        basename = os.path.basename(pagename)
        stem = book._extract_unit_stem(basename, doc_dir)
        if basename == "el" and doc_dir:
            stem = os.path.basename(doc_dir)

        def _qual(local_name: str) -> str:
            return f"{doc_dir}/{local_name}" if doc_dir else local_name

        probe_page = pagename
        el_candidates = [
            _qual(f"{stem}.el"),
            _qual(f"{stem}_el"),
            _qual(f"{stem}-el"),
            _qual("el"),
        ]
        el_doc = next((c for c in el_candidates if c in found_docs), None)
        if el_doc and pagename == el_doc:
            en_cand = next(
                (
                    c
                    for c in (
                        _qual(f"{stem}-en"),
                        _qual(f"{stem}_en"),
                        _qual(f"{stem}.en"),
                    )
                    if c in found_docs
                ),
                None,
            )
            if en_cand:
                probe_page = en_cand

        tracks = orig_detect(env, probe_page)
        if not el_doc:
            return tracks

        updated: list[dict[str, Any]] = []
        inserted_el = False
        el_entry: dict[str, Any] = {
            "key": "el",
            "label": label,
            "docname": el_doc,
            "active": el_doc == pagename,
        }
        for tr in tracks:
            if tr.get("docname") == el_doc:
                continue
            item = dict(tr)
            item["active"] = item.get("docname") == pagename
            updated.append(item)
            if item.get("key") == "en" and not inserted_el:
                updated.append(el_entry)
                inserted_el = True

        if not inserted_el:
            updated.insert(0, el_entry)

        return updated if len(updated) >= 2 else []

    _detect_with_greek._euclid_data_el_patched = True  # type: ignore[attr-defined]
    book.detect_companion_tracks = _detect_with_greek


def configure_local_intersphinx(
    intersphinx_mapping: dict[str, Any],
    project_root: Path,
) -> None:
    """Bind local ``objects.inv`` files for sister GEOMETOR repos and drop remote-only targets.

    Args:
        intersphinx_mapping: Mutable Sphinx ``intersphinx_mapping`` dictionary.
        project_root: Root directory of the ``geometor/euclid`` repository.
    """
    geometor_dir = project_root.parent
    for sister in ("elements", "pappus", "proclus", "altshiller-court", "aristotle"):
        inv = geometor_dir / sister / "docs" / "objects.inv"
        if inv.is_file():
            key = sister.replace("-", "_")
            intersphinx_mapping[key] = (
                f"https://geometor.github.io/{sister}",
                str(inv.resolve()),
            )
    for key in list(intersphinx_mapping.keys()):
        _uri, inv_target = intersphinx_mapping[key]
        if inv_target is None:
            intersphinx_mapping.pop(key, None)


def setup(app: object) -> dict[str, Any]:
    """Register the Greek Book Codex companion track with Sphinx.

    Args:
        app: Active Sphinx application instance.

    Returns:
        Sphinx extension metadata dictionary defining version and parallel safety.
    """
    _ = app
    register_greek_book_track()
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
