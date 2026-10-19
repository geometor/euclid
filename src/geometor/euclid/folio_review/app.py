"""Flask web application for Euclid Folio Review & Vetting.

Thin wrapper around `photon_platform.publish.folio_review.app` defaulting to
`resources/heath` in the `geometor.euclid` workspace.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from photon_platform.publish.folio_review.app import create_app as _publish_create_app, main as _publish_main


def _default_heath_root() -> Path:
    workspace_root = Path(__file__).resolve().parents[4]
    return workspace_root / "resources" / "heath"


def create_app(
    root_dir: Optional[Path] = None,
    project_title: Optional[str] = "GEOMETOR Euclid",
    edition_label: Optional[str] = "Heath",
):
    """Create and configure the Flask review application for Euclid."""
    return _publish_create_app(
        root_dir=root_dir or _default_heath_root(),
        project_title=project_title,
        edition_label=edition_label,
    )


def main() -> None:
    """CLI entry point for `euclid-review`."""
    _publish_main()


if __name__ == "__main__":
    main()
