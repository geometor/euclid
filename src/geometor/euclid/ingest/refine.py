from geometor.elements.ingest.analysis import run_analysis
from geometor.elements.ingest.cropping import run_cropping
from geometor.elements.ingest.metadata_extraction.metadata_extraction import run_metadata_extraction

def run_refinement():
    print("Starting refinement pipeline...")
    run_analysis()
    run_cropping()
    run_metadata_extraction()
    print("Refinement pipeline completed.")

if __name__ == "__main__":
    run_refinement()
