# GEOMETOR Euclid

A digital reconstruction of Euclid's Elements for semantic discovery and dependency mapping.

## Overview

`geometor.euclid` focuses on the "semantic discovery" of the original text of Euclid's *Elements*. It parses the classical Heath edition to create a structured knowledge base, enabling:

-   **Text Analysis**: Extracting and normalizing text from the source.
-   **Structure Identification**: Identifying definitions, postulates, axioms, and propositions.
-   **Dependency Mapping**: Tracing the logical prerequisites between elements.
-   **Semantic Tagging**: Identifying key concepts and relationships within the text.
-   **Keyword Discovery**: Extracting terms from the original index and performing manual analysis of definitions to build a comprehensive keyword vocabulary.

## Key Repos

-   **euclid**: This repository. Code for parsing, reviewing, and compiling the Heath Edition (`resources/heath/` -> `docsrc/heath/`).
-   **elements**: The project that builds upon this structure to create the G index and symbolic models.

## Key Modules

-   `compile_edition.py`: De-pagination and edition compiler transforming folio-reviewed RST sources (`resources/heath/`) into the 3-volume Heath Edition (`docsrc/heath/`) with proposition collections, companion commentary tracks, and scholarly apparatus (`bibliography.rst`, `persons.rst`, `glossary.rst`).
-   `scripts/recalibrate_svgs.py`: Tight bounding-box (`viewBox`, `width`, `height`) recalibrator and light/dark mode CSS normalizer across all 831 geometric SVGs in `resources/heath/`.
-   `folio_review/`: Flask web UI for side-by-side folio image and semantic RST transcription review.
