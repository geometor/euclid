changelog
=========

:project: geometor.euclid

0.4.3
-----
*2026-11-14*

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.4.2
-----
*2026-11-14*

- Standardized Book Title Page, top-level Header Navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author/Translator profiles in ``People``, and English structural terminology.

0.4.1
-----
*2026-11-13*

**added**

-   **Primary-Source Folio Links**:
    -   Activated and verified 2,274 ``.. folio::`` directives and 28 ``:folio:`` frontmatter badges across Euclid's *Elements* and *Data* linking to calibrated primary facsimile scans and concordance loci.


0.4.0
-----
*2026-11-12*

**added**

-   **Euclid's** *Data* (**Δεδομένα** **4-Track Bilingual Book Codex**):
    -   Added complete 4-track synchronized Book Codex (``docsrc/data/``: *Proposition*, *Greek (Menge 1896)*, *Summary*, *Notes*) spanning Marinus of Neapolis's *Protheoria* (§§ 1–18), Definitions ``D.def.1``–``D.def.15``, and all 94 Propositions ``D.1``–``D.94`` across Units 0–6.
    -   Added ``resources/data/concordance.json`` (109-node functional dependency DAG reconciling Menge 1896, Simson 1762/1806, Heath's *Elements*, ``geometor.elements`` G-Index, Pappus *Synagoge* VII, Petersen 1879, and Altshiller-Court 1952), ``enunciations.json``, ``citations.json``, ``persons.json``, and ``glossary.json``.
    -   Added 8 interactive ``.euclid-graphic`` SVGs (``data_01_taxonomy.svg``–``data_08_functional_dag.svg``), ``src/geometor/euclid/data_codex.py``, ``src/geometor/euclid/sphinx_ext.py``, and ``tests/test_euclid_data.py``.

0.3.7
-----
*2026-11-12*

**refactored**

-   **Strict Content / Code Separation**:
    -   Decoupled legacy executable Python construction vestiges from the diplomatic Heath edition so ``geometor.euclid`` preserves pure scholarly text, calibrated ``.euclid-graphic`` SVGs, and citation apparatus while executable symbolic models live downstream in ``geometor.elements``.
    -   Added ``tests/test_decouple_code.py`` verification suite and updated GitHub Actions deployment permissions.

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

