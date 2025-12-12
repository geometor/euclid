import os
from pathlib import Path

# Base paths
PROJECT_ROOT = Path(os.getenv("GEOMETOR_PROJECT_ROOT", "/home/phi/PROJECTS/geometor/elements"))

RESOURCES_DIR = PROJECT_ROOT / "resources"

# Input paths
# Default to the path found in original scripts, but allow env var override
DEFAULT_PDF_DIR = "/home/phi/PROJECTS/geometor/heath_pdf_2nd_ed"
PDF_BASE_DIR = Path(os.getenv("GEOMETOR_PDF_DIR", DEFAULT_PDF_DIR))

# Output paths
EXTRACTED_DIR = RESOURCES_DIR / "heath"

# JSON Data Files
PROPOSITION_INDEX_PATH = EXTRACTED_DIR / "proposition_index.json"
METADATA_PATH = RESOURCES_DIR / "metadata.json"

# Global Settings (from manual cropping instructions)
PAGE_WIDTH = 755
PAGE_HEADER_END = 125
PAGE_FOOTER_START = 1115
CROP_WIDTH = 640

# Volume Definitions
VOLUMES = {
    "I": "The Thirteen Books of Euclid's Elements _ Volume I _ Second Edition (35)/The Thirteen Books of Euclid's Elements _ - Euclid.pdf",
    "II": "The Thirteen Books of Euclid's Elements _ Volume II _ Second Edition (36)/The Thirteen Books of Euclid's Elements _ - Euclid.pdf",
    "III": "The Thirteen Books of Euclid's Elements _ Volume III _ Second Edition (37)/The Thirteen Books of Euclid's Elements _ - Euclid.pdf"
}
