"""Scholarly edition compiler, semantic parser, and dependency graph tools for Euclid.

``geometor.euclid`` unites the diplomatic/scholarly digital edition of
Sir Thomas L. Heath's *The Thirteen Books of Euclid's Elements* with the 4-track
bilingual Book Codex of Euclid's *Data* (*Δεδομένα*, Menge 1896 Greek & English),
accompanied by calibrated semantic SVGs and concordance registries. It contains
zero executable Python construction scripts in its treatise tracks; all symbolic
constructions (``geometor.model``) live downstream in ``geometor.elements``.
"""

from __future__ import annotations


__version__ = "0.4.3"

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
