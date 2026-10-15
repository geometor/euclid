"""Programmatic construction for Book I, Postulate 5 Commentary: Ptolemy (0220.g1).

Ptolemy's diagram showing lines AB, CD meeting towards B, D at K.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0220_g1() -> Model:
    """Construct the figure for 0220.g1 using geometor.model."""
    model = Model("0220.g1")

    # Given / Constructed Points (y-inverted from SVG coordinates)
    pt_A = model.set_point(26.0, -72.0, classes=["given"], label="A")
    pt_F = model.set_point(85.0, -60.0, classes=["given"], label="F")
    pt_B = model.set_point(141.0, -48.6, classes=["given"], label="B")
    pt_C = model.set_point(20.0, -126.0, classes=["given"], label="C")
    pt_G = model.set_point(73.0, -126.0, classes=["given"], label="G")
    pt_D = model.set_point(166.0, -126.0, classes=["given"], label="D")
    pt_E = model.set_point(91.0, -27.0, classes=["given"], label="E")
    pt_H = model.set_point(65.0, -170.0, classes=["given"], label="H")
    pt_K = model.set_point(173.0, -80.0, classes=["given"], label="K")

    # Base Construction Lines
    model.construct_line(pt_A, pt_B)
    model.construct_line(pt_C, pt_D)
    model.construct_line(pt_E, pt_H)

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_F, pt_A)
    model.set_segment(pt_F, pt_B)
    model.set_segment(pt_B, pt_K)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_G, pt_C)
    model.set_segment(pt_G, pt_D)
    model.set_segment(pt_D, pt_K)
    model.set_segment(pt_E, pt_H)
    model.set_segment(pt_E, pt_F)
    model.set_segment(pt_F, pt_G)
    model.set_segment(pt_G, pt_H)

    # Polygons
    model.set_polygon([pt_K, pt_F, pt_G])

    # Angles (Wedges)
    model.set_wedge(pt_F, pt_G, pt_G, pt_A)
    model.set_wedge(pt_F, pt_B, pt_B, pt_G)
    model.set_wedge(pt_G, pt_C, pt_C, pt_F)
    model.set_wedge(pt_G, pt_F, pt_F, pt_D)

    return model


if __name__ == "__main__":
    construct_0220_g1()
