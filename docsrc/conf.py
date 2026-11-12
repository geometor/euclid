from pathlib import Path
import sys

_SRC_DIR = str(Path(__file__).resolve().parents[1] / "src")
if _SRC_DIR not in sys.path:
    sys.path.insert(0, _SRC_DIR)

from photon_platform.publish.global_conf import *
import geometor.euclid as module
from geometor.euclid.sphinx_ext import (
    configure_local_intersphinx,
    register_greek_book_track,
)

version = module.__version__

org = "geometor"
org_name = "geometor"

repo = "euclid"
repo_name = "euclid"

setup_globals(org, org_name, repo, repo_name)

if "geometor.euclid.sphinx_ext" not in extensions:
    extensions.append("geometor.euclid.sphinx_ext")
register_greek_book_track()
configure_local_intersphinx(intersphinx_mapping, Path(__file__).resolve().parents[1])

