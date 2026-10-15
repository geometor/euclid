"""Programmatic construction for Book I, Proposition 21 (0303.g1).

If on one of the sides of a triangle, from its extremities, there be constructed two straight lines meeting within the triangle, the straight lines so constructed will be less than the remaining two sides of the triangle, but will contain a greater angle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0303_g1() -> Model:
    """Construct the figure for 0303.g1 (I.21) using geometor.model."""
    model = Model("0303.g1")

    # Points
    pt_A = model.set_point(63.5, -21.5, classes=["given"], label="A")
    pt_B = model.set_point(14.5, -118.5, classes=["given"], label="B")
    pt_C = model.set_point(188, -118.5, classes=["given"], label="C")
    pt_D = model.set_point(76.5, -64, classes=["given"], label="D")
    pt_E = model.set_point(96, -46.5, classes=["given"], label="E")

    # Base Constructions (Lines and Circles)
    model.construct_line(pt_B, pt_D)

    # Segments
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_A, pt_E)
    model.set_segment(pt_E, pt_C)
    model.set_segment(pt_B, pt_E)
    model.set_segment(pt_B, pt_D)
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_C, pt_D)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_A, pt_B, pt_E])
    model.set_polygon([pt_B, pt_D, pt_C])
    model.set_polygon([pt_C, pt_D, pt_E])

    # Angles (Wedges)
    model.set_wedge(pt_D, pt_B, pt_B, pt_C)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_E, pt_C, pt_C, pt_D)

    return model


if __name__ == "__main__":
    construct_0303_g1()
