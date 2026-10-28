"""Custom Docutils RST renderer for Euclid Folio Review.

Delegates to the canonical `photon_platform.publish.rst_renderer` module.
"""

from __future__ import annotations

from photon_platform.publish.rst_renderer import (
    parse_rst_frontmatter,
    parse_rst_metadata,
    render_rst_html,
    render_rst_to_html,
)


def validate_rst(rst_text: str) -> list[str]:
    """Validate RST text and return a list of warning/error strings."""
    errors: list[str] = []
    try:
        render_rst_html(rst_text)
    except Exception as exc:
        errors.append(str(exc))
    return errors


__all__ = [
    "parse_rst_frontmatter",
    "parse_rst_metadata",
    "render_rst_html",
    "render_rst_to_html",
    "validate_rst",
]
