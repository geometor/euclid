"""Programmatic construction for Book I, Proposition 20 (0300.g2).

In any triangle two sides taken together in any manner are greater than the remaining one.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0300_g2() -> Model:
    """Construct the figure for 0300.g2 (I.20) using geometor.model."""
    model = Model("0300.g2")

    # Points
    pt_B = model.set_point(20, -133, classes=["given"], label="B")
    pt_C = model.set_point(125, -133, classes=["given"], label="C")
    pt_A = model.set_point(56.5, -92.5, classes=["given"], label="A")
    pt_D = model.set_point(109, -31, classes=["given"], label="D")

    # Base Constructions (Lines and Circles)
    model.construct_line(pt_B, pt_A)

    # Segments
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_B, pt_D)
    model.set_segment(pt_B, pt_A)
    model.set_segment(pt_A, pt_D)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_D, pt_C)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_A, pt_D, pt_C])
    model.set_polygon([pt_D, pt_B, pt_C])

    # Angles (Wedges)
    model.set_wedge(pt_D, pt_A, pt_A, pt_C)
    model.set_wedge(pt_C, pt_A, pt_A, pt_D)
    model.set_wedge(pt_C, pt_B, pt_B, pt_D)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_B, pt_A, pt_A, pt_C)
    model.set_wedge(pt_C, pt_A, pt_A, pt_B)

    return model


if __name__ == "__main__":
    construct_0300_g2()
