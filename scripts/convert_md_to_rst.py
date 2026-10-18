#!/usr/bin/env python3
"""CLI tool to convert Euclid folio .md files to pure semantic .rst files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List

# Ensure local src and sibling photon-platform/publish/src are on sys.path
_REPO_ROOT = Path(__file__).resolve().parents[1]
_LOCAL_SRC = _REPO_ROOT / "src"
_VENV_SITE = _REPO_ROOT / ".venv" / "lib" / "python3.13" / "site-packages"
_PUBLISH_SRC = _REPO_ROOT.parents[1] / "photon-platform" / "publish" / "src"

for _p in (_PUBLISH_SRC, _LOCAL_SRC, _VENV_SITE):
    if _p.exists() and str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from geometor.euclid.ingest.md_to_rst import convert_file

_HTML_TAG_RE = re.compile(
    r"</?(?:p|span|div|sup|sub|br|em|strong|center|figure|pre|table|tr|td|th)(?:\s[^>]*)?>",
    re.IGNORECASE,
)


def collect_md_files(paths: List[str], include_notes: bool = False) -> List[Path]:
    """Collect .md files from the provided file or directory paths."""
    found: List[Path] = []
    for raw_p in paths:
        p = Path(raw_p)
        if p.is_file() and p.suffix == ".md":
            if not include_notes and p.name.endswith(".notes.md"):
                continue
            found.append(p)
        elif p.is_dir():
            for md_f in sorted(p.rglob("*.md")):
                base_stem = md_f.name.split(".")[0]
                if not (len(base_stem) == 4 and base_stem.isdigit()):
                    continue
                if not include_notes and md_f.name.endswith(".notes.md"):
                    continue
                found.append(md_f)
    return found


def main() -> None:
    """Parse arguments and convert folio Markdown files to reStructuredText."""
    parser = argparse.ArgumentParser(
        description="Convert Euclid folio .md files into semantic .rst files."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="File or directory paths to convert (e.g. resources/heath/volume_I/book_i/)",
    )
    parser.add_argument(
        "--include-notes",
        action="store_true",
        help="Also convert <folio>.notes.md files to <folio>.notes.rst",
    )
    parser.add_argument(
        "--no-overwrite",
        action="store_true",
        help="Skip conversion if the target .rst file already exists",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Validate converted .rst files with Docutils (report_level=2) and check for leftover HTML tags",
    )
    args = parser.parse_args()

    md_files = collect_md_files(args.paths, include_notes=args.include_notes)
    rst_files: List[Path] = []
    for md_path in md_files:
        rst_path = convert_file(md_path, overwrite=not args.no_overwrite)
        rst_files.append(rst_path)

    print(f"Converted {len(rst_files)} file(s) to .rst")

    if args.verify:
        from geometor.euclid.folio_review.rst_utils import validate_rst

        html_leftover = []
        docutils_warnings = []
        for rst_p in rst_files:
            txt = rst_p.read_text(encoding="utf-8")
            m_tag = _HTML_TAG_RE.search(txt)
            if m_tag:
                html_leftover.append((str(rst_p), m_tag.group(0)))
            warns = validate_rst(txt)
            if warns:
                docutils_warnings.append((str(rst_p), warns))

        print(f"Leftover HTML tags: {len(html_leftover)}")
        for fp, tag in html_leftover[:10]:
            print(f"  HTML tag in {fp}: {tag}")

        print(f"Files with Docutils warnings/errors: {len(docutils_warnings)}")
        for fp, wlist in docutils_warnings[:20]:
            print(f"  WARNING in {fp}:")
            for w in wlist[:5]:
                print(f"    {w}")

        if html_leftover or docutils_warnings:
            sys.exit(1)


if __name__ == "__main__":
    main()
