"""Programmatic construction for Book I, Postulate 5 Commentary: Ptolemy (0219.g1).

Ptolemy's diagram for parallel lines AB, CD cut by transversal FG (Euclid I. 29).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0219_g1() -> Model:
    """Construct the figure for 0219.g1 using geometor.model."""
    model = Model("0219.g1")

    # Given Points (y-inverted from SVG coordinates)
    pt_A = model.set_point(25.0, -30.0, classes=["given"], label="A")
    pt_B = model.set_point(200.0, -30.0, classes=["given"], label="B")
    pt_F = model.set_point(136.0, -30.0, classes=["given"], label="F")
    pt_C = model.set_point(25.0, -78.0, classes=["given"], label="C")
    pt_D = model.set_point(200.0, -78.0, classes=["given"], label="D")
    pt_G = model.set_point(111.0, -78.0, classes=["given"], label="G")

    # Base Construction Lines
    model.construct_line(pt_A, pt_B)
    model.construct_line(pt_C, pt_D)
    model.construct_line(pt_F, pt_G)

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_F)
    model.set_segment(pt_F, pt_B)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_C, pt_G)
    model.set_segment(pt_G, pt_D)
    model.set_segment(pt_F, pt_G)

    # Angles (Wedges)
    model.set_wedge(pt_F, pt_G, pt_G, pt_A)
    model.set_wedge(pt_F, pt_B, pt_B, pt_G)
    model.set_wedge(pt_G, pt_C, pt_C, pt_F)
    model.set_wedge(pt_G, pt_F, pt_F, pt_D)

    return model


if __name__ == "__main__":
    construct_0219_g1()
