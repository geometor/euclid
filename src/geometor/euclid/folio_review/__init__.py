"""Euclid Folio Review & Vetting Web Application.

Delegates to the canonical `photon_platform.publish.folio_review` package,
defaulting to `resources/heath` when invoked from `geometor.euclid`.
"""

from .app import create_app, main
from .reviews import ReviewManager
from .scanner import FolioScanner

__all__ = ["create_app", "main", "FolioScanner", "ReviewManager"]
