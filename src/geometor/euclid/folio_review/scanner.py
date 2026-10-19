"""Folio discovery, metadata parsing, and statistics aggregation for Euclid.

Thin wrapper around `photon_platform.publish.folio_review.scanner`.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from photon_platform.publish.folio_review.scanner import (
    FolioScanner as _PublishFolioScanner,
    PYGMENTS_CSS,
    PYGMENTS_STYLE,
    discover_edition_root,
    fix_relative_media_urls,
    highlight_code_html,
    infer_project_and_edition,
    parse_frontmatter,
    protect_math_for_markdown,
    render_markdown_with_math,
    render_rst_with_media,
    restore_math_placeholders,
)


class FolioScanner(_PublishFolioScanner):
    """FolioScanner defaulting to `resources/heath` in `geometor.euclid`."""

    def __init__(self, root_dir: Optional[Path] = None):
        if root_dir is None:
            workspace_root = Path(__file__).resolve().parents[4]
            root_dir = workspace_root / "resources" / "heath"
        super().__init__(root_dir=root_dir)
