"""
Geometor Elements Ingestion Pipeline

This module contains the tools and logic for ingesting Euclid's Elements from
PDF sources (Heath edition), organizing them, and extracting propositions and metadata.

Pipeline Stages:
1. Ingestion (`pipeline.py`):

    - Extraction (`extraction.py`): Converts PDF pages to images and text, and extracts the Table of Contents.
    - Organization (`organization.py`): Structures the extracted files into folders based on the TOC.

2. Refinement (`refine.py`):

    - Analysis (`analysis.py`): Scans the text to identify and index propositions.
    - Cropping (`cropping.py`): Crops proposition text and extracts graphics based on manual instructions.
    - Metadata (`metadata_extraction/metadata_extraction.py`): Extracts metadata for documentation generation.

Usage:
    Run the ingestion pipeline:
    $ python -m geometor.elements.ingest.pipeline
    
    Run the refinement pipeline:
    $ python -m geometor.elements.ingest.refine
"""

from .pipeline import run_pipeline
from .refine import run_refinement
