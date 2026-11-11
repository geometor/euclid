# GEOMETOR • euclid

Authoritative digital reconstruction, semantic discovery, and critical Book Codex edition of Sir Thomas L. Heath's *The Thirteen Books of Euclid's Elements*.

## Architectural Boundary (`euclid` vs. `elements`)

- **`geometor/euclid` (This Repository — Zero Construction Code)**:
  - Strictly the diplomatic and scholarly edition of Heath's three volumes (`resources/heath/` $\rightarrow$ `docsrc/heath/`), apparatus registries (`citations.json`, `persons.json`, `glossary.json`, `enunciations.json`), and **832 calibrated historical semantic SVGs** (`<NNNN>.g*.svg` paired with `"geometry"` calibration schemas in `<NNNN>.json`).
  - Contains **no executable Python construction scripts** (`<NNNN>.g*.py` or `geometor.model` code).
- **`geometor/elements` (Downstream Constructive & Demonstrative Canon)**:
  - Consumes `euclid`'s compiled `docsrc/heath/` RST, dependency graph, and `docs/objects.inv` to build the **G-Index** (`G.1`–`G.525`), formal pseudocode, and executable **`geometor.model` + `geometor.explorer`** constructions and demonstrations.

## Key Modules & Scripts

- `src/geometor/euclid/compile_edition.py`: De-pagination and edition compiler transforming folio-reviewed RST sources (`resources/heath/`) into the 3-volume Heath Edition (`docsrc/heath/`) with proposition collections, companion commentary tracks (`commentary.rst`), and scholarly apparatus (`bibliography.rst`, `persons.rst`, `glossary.rst`).
- `src/geometor/euclid/graph.py`: Logical and definitional dependency graph extractor across Books I–XIII.
- `src/geometor/euclid/scripts/graphic_tool.py`: CLI utility (`uv run graphic_tool`) for bounding-box calibration and raster figure crop extraction from `<NNNN>.png` / `<NNNN>.json`.
- `scripts/recalibrate_svgs.py`: Tight bounding-box (`viewBox`, `width`, `height`) recalibrator and light/dark mode CSS normalizer across all geometric SVGs in `resources/heath/`.
- `src/geometor/euclid/folio_review/`: Thin workspace wrapper around `photon_platform.publish.folio_review` (`publish folio` / `uv run folio_review`) for side-by-side folio scan, RST transcription, and diplomatic SVG review.
