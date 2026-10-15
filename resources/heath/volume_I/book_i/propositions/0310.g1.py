"""Programmatic construction for Book I, Proposition 23 (0310.g1).

Apollonius Construction of Equal Angle by Circular Arcs (Book I, Proposition 23).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0310_g1() -> Model:
    """Construct the figure for 0310.g1 (I.23) using geometor.model."""
    model = Model("0310.g1")

    # Points
    pt_D = model.set_point(26, -64.5, classes=["given"], label="D")
    pt_C = model.set_point(152.5, -25, classes=["given"], label="C")
    pt_E = model.set_point(154.2, -98, classes=["given"], label="E")
    pt_A = model.set_point(33, -168.5, classes=["given"], label="A")
    pt_F = model.set_point(159.8, -130, classes=["given"], label="F")
    pt_B = model.set_point(160.9, -203, classes=["given"], label="B")

    # Base Constructions (Lines and Circles)
    model.construct_circle(pt_D, pt_C)
    model.construct_circle(pt_A, pt_B)

    # Segments
    model.set_segment(pt_D, pt_C)
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_C, pt_E)
    model.set_segment(pt_A, pt_F)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_B, pt_F)

    # Polygons
    model.set_polygon([pt_C, pt_D, pt_E])
    model.set_polygon([pt_B, pt_A, pt_F])

    # Angles (Wedges)
    model.set_wedge(pt_D, pt_C, pt_C, pt_E)
    model.set_wedge(pt_A, pt_F, pt_F, pt_B)

    return model


if __name__ == "__main__":
    construct_0310_g1()
