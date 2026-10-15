"""Programmatic construction for Book I, Proposition 21 (0305.g1).

De Morgan Proposition on Perpendicular and Obliques from a Point to a Line.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0305_g1() -> Model:
    """Construct the figure for 0305.g1 (I.21) using geometor.model."""
    model = Model("0305.g1")

    # Points
    pt_A = model.set_point(131.5, -21.5, classes=["given"], label="A")
    pt_Aprime = model.set_point(131.5, -143.5, classes=["given"], label="A'")
    pt_D = model.set_point(131.5, -82.5, classes=["given"], label="D")
    pt_G = model.set_point(38.8, -82.5, classes=["given"], label="G")
    pt_E = model.set_point(172.5, -82.5, classes=["given"], label="E")
    pt_F = model.set_point(224.2, -82.5, classes=["given"], label="F")
    pt_B = model.set_point(12, -82.5, classes=["given"], label="B")
    pt_C = model.set_point(286, -82.5, classes=["given"], label="C")

    # Base Constructions (Lines and Circles)
    model.construct_line(pt_B, pt_C)
    model.construct_line(pt_A, pt_D)

    # Segments
    model.set_segment(pt_A, pt_Aprime)
    model.set_segment(pt_A, pt_D)
    model.set_segment(pt_Aprime, pt_D)
    model.set_segment(pt_D, pt_B)
    model.set_segment(pt_D, pt_G)
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_D, pt_F)
    model.set_segment(pt_A, pt_G)
    model.set_segment(pt_A, pt_E)
    model.set_segment(pt_A, pt_F)
    model.set_segment(pt_Aprime, pt_E)
    model.set_segment(pt_Aprime, pt_F)

    # Polygons
    model.set_polygon([pt_A, pt_G, pt_D])
    model.set_polygon([pt_A, pt_D, pt_E])
    model.set_polygon([pt_A, pt_D, pt_F])
    model.set_polygon([pt_Aprime, pt_D, pt_E])
    model.set_polygon([pt_Aprime, pt_D, pt_F])
    model.set_polygon([pt_A, pt_E, pt_Aprime])
    model.set_polygon([pt_A, pt_F, pt_Aprime])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_G, pt_G, pt_D)
    model.set_wedge(pt_A, pt_F, pt_F, pt_D)
    model.set_wedge(pt_A, pt_E, pt_E, pt_D)

    return model


if __name__ == "__main__":
    construct_0305_g1()
