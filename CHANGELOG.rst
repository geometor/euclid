changelog
=========

:project: geometor.euclid

0.3.2
-----
*2026-10-28*

**added**

-   **Equality Assertion Highlighting**:
    -   Curated 2,904 inline ``:eq:`` equality annotations across 569 folios spanning all 13 Books of Euclid's *Elements*.
    -   Recalibrated all 831 geometric SVGs with ``<defs>`` center tick markers (``#geom-tick-1/2/3``), 3-vertex midpoint segment paths, and 3-vertex midpoint angle arcs (``.geom-ang-arc``).
    -   Recompiled ``docsrc/heath/`` and rebuilt ``docs/`` HTML edition.

0.2.3
-----
*2025-12-16*

**added**

-   **Keyword Analysis**:
    -   Created ``src/geometor/euclid/scripts/extract_index.py`` to parse Heath's OCR index files.
    -   Extracted ``people.yaml`` and ``topics.yaml`` in ``resources/heath/index/``.
    -   Created ``resources/heath/keywords.md`` with manually curated keywords from Books I-XIII.

**changed**

-   Updated ``GEMINI.md`` to reflect new analysis tools.

0.2.2
-----
*2025-12-15*

**changed**

-   Reparse Heath with book subtitles
-   cleaned up sphinx build errors

0.2.1
-----
*2025-12-15*

**changed**

-   Standardized docstrings (Google style) and type hints across the codebase.
-   Resolved all `ruff` linting errors (D and ANN rules).

0.2.0
-----
*2025-12-12*

**changed**

-   Reset git repository to start fresh with semantic discovery scope.
-   Added `GEMINI.md`.
-   Updated `intro.rst`.

0.1.4 
-----

:init: 2025.346
:merge:
:pub: 

  creating semantic structure around the classic work

- initalize project

