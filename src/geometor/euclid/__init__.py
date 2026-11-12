"""Scholarly edition compiler, semantic parser, and dependency graph tools for Heath's Euclid.

``geometor.euclid`` is strictly the diplomatic/scholarly digital edition of
Sir Thomas L. Heath's *The Thirteen Books of Euclid's Elements*, accompanied by
calibrated historical semantic SVGs. It contains zero executable Python
construction scripts; all symbolic constructions (``geometor.model``) and
rendered demonstrations (``geometor.explorer``) live downstream in
``geometor.elements``.
"""

from __future__ import annotations


__version__ = "0.3.7"

__all__ = [
    "parse_element_xml",
    "generate_rst_from_xml",
    "build_rst_docs",
    "generate_g_index",
    "build_graph",
]

try:
    from .xml_parser import parse_element_xml
except ImportError:
    parse_element_xml = None

try:
    from .rst_generator import generate_rst_from_xml
except ImportError:
    generate_rst_from_xml = None

try:
    from .rst_builder import build_rst_docs
except ImportError:
    build_rst_docs = None

try:
    from .graph import build_graph
except ImportError:
    build_graph = None
