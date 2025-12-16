"""Main ingestion pipeline script."""

from geometor.euclid.ingest.extraction import run_extraction
from geometor.euclid.ingest.organization import run_organization


def run_pipeline() -> None:
    """Runs the full ingestion pipeline: extraction and organization."""
    print("Starting ingestion pipeline...")
    run_extraction()
    run_organization()
    print("Ingestion pipeline completed.")


if __name__ == "__main__":
    run_pipeline()
