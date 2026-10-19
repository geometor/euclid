"""Custom Docutils RST renderer for Euclid Folio Review.

Delegates to the canonical `photon_platform.publish.rst_renderer` module.
"""

from __future__ import annotations

from photon_platform.publish.rst_renderer import parse_rst_frontmatter, render_rst_to_html

__all__ = ["parse_rst_frontmatter", "render_rst_to_html"]
