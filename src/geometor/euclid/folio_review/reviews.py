"""Persistent review and vetting status tracker for Euclid folios.

Thin wrapper around `photon_platform.publish.folio_review.reviews`.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from photon_platform.publish.folio_review.reviews import ReviewManager as _PublishReviewManager


class ReviewManager(_PublishReviewManager):
    """ReviewManager defaulting to `resources/heath/folio_reviews.json` in `geometor.euclid`."""

    def __init__(self, storage_path: Optional[Path] = None):
        if storage_path is None:
            workspace_root = Path(__file__).resolve().parents[4]
            storage_path = workspace_root / "resources" / "heath" / "folio_reviews.json"
        super().__init__(storage_path=storage_path)
