"""Refinement pipeline script."""

from geometor.euclid.ingest.analysis import load_analysis_data
from geometor.euclid.ingest.cropping import process_propositions
from geometor.euclid.ingest.metadata_extraction.metadata_extraction import (
    run_metadata_extraction,
)


def run_refinement() -> None:
    """Runs the refinement pipeline: analysis, cropping, and metadata extraction."""
    print("Starting refinement pipeline...")
    run_analysis()
    run_cropping()
    run_metadata_extraction()
    print("Refinement pipeline completed.")


if __name__ == "__main__":
    run_refinement()
