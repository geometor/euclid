"""Tools for modeling and rendering geometric constructions from Euclid's Elements.

Key Components:
---------------
- **XML Parsing**: Tools (:func:`parse_element_xml`) to parse the XML source of Euclid's Elements.
- **RST Generation**: Tools (:func:`generate_rst_from_xml`) to convert XML to ReStructuredText.
- **Graphing**: Tools (:func:`build_graph`, :func:`generate_g_index`) to build dependency graphs and indexes.

Usage:
------
Use the provided functions to parse XML files and generate documentation.
"""

from __future__ import annotations


__version__ = "0.2.3"

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
