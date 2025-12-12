from geometor.elements.ingest.extraction import run_extraction
from geometor.elements.ingest.organization import run_organization

def run_pipeline():
    print("Starting ingestion pipeline...")
    run_extraction()
    run_organization()
    print("Ingestion pipeline completed.")

if __name__ == "__main__":
    run_pipeline()
