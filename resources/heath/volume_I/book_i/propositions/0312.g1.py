"""Programmatic construction for Book I, Proposition 24 (0312.g1).

Proof that F falls below EG in Book I, Proposition 24 (Pfleiderer, Lardner, Todhunter).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0312_g1() -> Model:
    """Construct the figure for 0312.g1 (I.24) using geometor.model."""
    model = Model("0312.g1")

    # Points
    pt_D = model.set_point(50.5, -33.5, classes=["given"], label="D")
    pt_E = model.set_point(18, -147, classes=["given"], label="E")
    pt_G = model.set_point(98, -90, classes=["given"], label="G")
    pt_H = model.set_point(51, -123.5, classes=["given"], label="H")
    pt_F = model.set_point(51.5, -148, classes=["given"], label="F")

    # Base Constructions (Lines and Circles)
    model.construct_line(pt_D, pt_F)

    # Segments
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_D, pt_G)
    model.set_segment(pt_E, pt_G)
    model.set_segment(pt_E, pt_H)
    model.set_segment(pt_H, pt_G)
    model.set_segment(pt_D, pt_F)
    model.set_segment(pt_D, pt_H)
    model.set_segment(pt_H, pt_F)

    # Polygons
    model.set_polygon([pt_D, pt_E, pt_G])
    model.set_polygon([pt_D, pt_E, pt_H])
    model.set_polygon([pt_D, pt_G, pt_H])

    # Angles (Wedges)
    model.set_wedge(pt_H, pt_D, pt_D, pt_G)
    model.set_wedge(pt_E, pt_D, pt_D, pt_G)
    model.set_wedge(pt_G, pt_D, pt_D, pt_E)
    model.set_wedge(pt_D, pt_E, pt_E, pt_G)

    return model


if __name__ == "__main__":
    construct_0312_g1()
