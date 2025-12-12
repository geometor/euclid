# GEOMETOR Euclid

A digital reconstruction of Euclid's Elements for semantic discovery and dependency mapping.

## Overview

`geometor.euclid` focuses on the "semantic discovery" of the original text of Euclid's *Elements*. It parses the classical Heath edition to create a structured knowledge base, enabling:

-   **Text Analysis**: Extracting and normalizing text from the source.
-   **Structure Identification**: Identifying definitions, postulates, axioms, and propositions.
-   **Dependency Mapping**: Tracing the logical prerequisites between elements.
-   **Semantic Tagging**: Identifying key concepts and relationships within the text.

## Key Repos

-   **euclid**: This repository. Code for parsing and structuring the text.
-   **elements**: The project that builds upon this structure to create the G index and symbolic models.

## Development Plan

-   Refine text extraction algorithms.
-   Enhance semantic tagging capabilities.
-   Ensure clean API for downstream consumers (like `geometor.elements`).

## Workflows

### Create Branch

1.  **Navigate to Repository**: `cd /home/phi/PROJECTS/geometor/euclid`
2.  **Checkout Main**: `git checkout main`
3.  **Pull Latest**: `git pull origin main`
4.  **Create Branch**: `git checkout -b <branch_name>`
