"""Programmatic construction for Book I, Proposition 23 (0308.g1).

On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0308_g1() -> Model:
    """Construct the figure for 0308.g1 (I.23) using geometor.model."""
    model = Model("0308.g1")

    # Points
    pt_A = model.set_point(24, -128.5, classes=["given"], label="A")
    pt_B = model.set_point(201, -128.5, classes=["given"], label="B")
    pt_F = model.set_point(109, -35, classes=["given"], label="F")
    pt_G = model.set_point(143, -128.5, classes=["given"], label="G")
    pt_C = model.set_point(258, -52, classes=["given"], label="C")
    pt_D = model.set_point(379, -23, classes=["given"], label="D")
    pt_E = model.set_point(357, -118, classes=["given"], label="E")

    # Base Constructions (Lines and Circles)
    model.construct_line(pt_C, pt_D)
    model.construct_line(pt_C, pt_E)

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_G)
    model.set_segment(pt_G, pt_B)
    model.set_segment(pt_A, pt_F)
    model.set_segment(pt_F, pt_G)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_C, pt_E)
    model.set_segment(pt_D, pt_E)

    # Polygons
    model.set_polygon([pt_A, pt_F, pt_G])
    model.set_polygon([pt_C, pt_D, pt_E])

    # Angles (Wedges)
    model.set_wedge(pt_C, pt_D, pt_D, pt_E)
    model.set_wedge(pt_A, pt_F, pt_F, pt_G)

    return model


if __name__ == "__main__":
    construct_0308_g1()
