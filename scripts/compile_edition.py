#!/usr/bin/env python3
"""CLI tool to compile sequential Euclid folio .rst files into the de-paginated Heath Edition."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_LOCAL_SRC = _REPO_ROOT / "src"
_VENV_SITE = _REPO_ROOT / ".venv" / "lib" / "python3.13" / "site-packages"
_PUBLISH_SRC = _REPO_ROOT.parents[1] / "photon-platform" / "publish" / "src"

for _p in (_PUBLISH_SRC, _LOCAL_SRC, _VENV_SITE):
    if _p.exists() and str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from geometor.euclid.compile_edition import compile_book, compile_edition


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compile sequential <folio>.rst files into the de-paginated Heath Edition under docsrc/heath/."
    )
    parser.add_argument(
        "src_dir",
        nargs="?",
        default="resources/heath",
        help="Source directory (default: resources/heath for full edition, or a specific book directory)",
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        help="Target output directory (default: docsrc/heath or docsrc/heath/<volume>/<book>)",
    )
    args = parser.parse_args()

    src_path = Path(args.src_dir)
    if not src_path.exists():
        print(f"Error: source directory {src_path} does not exist.", file=sys.stderr)
        sys.exit(1)

    if (src_path / "volume_I").exists():
        out_path = Path(args.out_dir) if args.out_dir else Path("docsrc/heath")
        stats = compile_edition(src_path, out_path)
        print(f"Compiled full Heath Edition ({src_path} -> {out_path}):")
        print(f"  Books compiled:               {stats['books_compiled']}")
        print(f"  Propositions compiled:        {stats['propositions_compiled']}")
        print(f"  Propositions with commentary: {stats['propositions_with_commentary']}")
        print(f"  Folio anchors emitted:        {stats['folio_anchors_emitted']}")
        print(f"  Total .rst files written:     {stats['total_rst_files_written']}")
        print(f"  Files with RST warnings:      {len(stats['warnings_by_file'])}")
        if stats["warnings_by_file"]:
            for fp, wlist in list(stats["warnings_by_file"].items())[:10]:
                print(f"  WARNING in {fp}:")
                for w in wlist[:5]:
                    print(f"    {w}")
            sys.exit(1)
        return

    if args.out_dir:
        out_path = Path(args.out_dir)
    else:
        parts = src_path.parts
        if "heath" in parts:
            idx = parts.index("heath")
            rel_after_heath = Path(*parts[idx + 1 :])
            out_path = Path("docsrc/heath") / rel_after_heath
        else:
            out_path = Path("docsrc/heath") / src_path.name

    stats = compile_book(src_path, out_path)
    print(f"Compiled Book {stats['book']} ({src_path} -> {out_path}):")
    print(f"  Input folios processed:       {stats['input_folios']}")
    print(f"  Propositions compiled:        {stats['propositions_compiled']}")
    print(f"  Propositions with commentary: {stats['propositions_with_commentary']}")
    print(f"  Output .rst files written:    {stats['rst_files_written']}")
    print(f"  Files with RST warnings:      {len(stats['warnings_by_file'])}")

    if stats["warnings_by_file"]:
        for fp, wlist in list(stats["warnings_by_file"].items())[:10]:
            print(f"  WARNING in {fp}:")
            for w in wlist[:5]:
                print(f"    {w}")
        sys.exit(1)


if __name__ == "__main__":
    main()
