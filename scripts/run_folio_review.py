#!/usr/bin/env python3
"""Run the Euclid Folio Review Flask web application."""

import sys
from pathlib import Path

# Add src to python path
src_dir = Path(__file__).resolve().parents[1] / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

from geometor.euclid.folio_review.app import main

if __name__ == "__main__":
    main()
