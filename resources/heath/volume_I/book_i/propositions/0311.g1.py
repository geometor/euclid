"""Programmatic construction for Book I, Proposition 24 (0311.g1).

Proclus Case 1 for Book I, Proposition 24 (G on EF produced).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0311_g1() -> Model:
    """Construct the figure for 0311.g1 (I.24) using geometor.model."""
    model = Model("0311.g1")

    # Points
    pt_A = model.set_point(97.5, -31.5, classes=["given"], label="A")
    pt_B = model.set_point(10, -111, classes=["given"], label="B")
    pt_C = model.set_point(127.5, -111, classes=["given"], label="C")
    pt_D = model.set_point(251.5, -31.5, classes=["given"], label="D")
    pt_E = model.set_point(161, -111, classes=["given"], label="E")
    pt_F = model.set_point(224.5, -111, classes=["given"], label="F")
    pt_G = model.set_point(280, -111, classes=["given"], label="G")

    # Base Constructions (Lines and Circles)
    model.construct_line(pt_E, pt_F)

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_D, pt_F)
    model.set_segment(pt_D, pt_G)
    model.set_segment(pt_E, pt_G)
    model.set_segment(pt_E, pt_F)
    model.set_segment(pt_F, pt_G)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_D, pt_E, pt_F])
    model.set_polygon([pt_D, pt_E, pt_G])
    model.set_polygon([pt_D, pt_F, pt_G])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_D, pt_E, pt_E, pt_F)
    model.set_wedge(pt_D, pt_E, pt_E, pt_G)
    model.set_wedge(pt_D, pt_F, pt_F, pt_G)

    return model


if __name__ == "__main__":
    construct_0311_g1()
