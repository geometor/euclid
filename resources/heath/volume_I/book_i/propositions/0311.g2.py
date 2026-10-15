"""Programmatic construction for Book I, Proposition 24 (0311.g2).

Proclus Case 2 for Book I, Proposition 24 (EG below EF).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0311_g2() -> Model:
    """Construct the figure for 0311.g2 (I.24) using geometor.model."""
    model = Model("0311.g2")

    # Points
    pt_A = model.set_point(109, -41.5, classes=["given"], label="A")
    pt_B = model.set_point(8, -123.5, classes=["given"], label="B")
    pt_C = model.set_point(127, -123.5, classes=["given"], label="C")
    pt_D = model.set_point(264, -38, classes=["given"], label="D")
    pt_E = model.set_point(163, -123.5, classes=["given"], label="E")
    pt_F = model.set_point(218.5, -105, classes=["given"], label="F")
    pt_G = model.set_point(283, -123.5, classes=["given"], label="G")

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_D, pt_F)
    model.set_segment(pt_E, pt_F)
    model.set_segment(pt_D, pt_G)
    model.set_segment(pt_E, pt_G)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_D, pt_E, pt_F])
    model.set_polygon([pt_D, pt_E, pt_G])
    model.set_polygon([pt_D, pt_F, pt_G])
    model.set_polygon([pt_E, pt_F, pt_G])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_D, pt_E, pt_E, pt_F)
    model.set_wedge(pt_D, pt_E, pt_E, pt_G)
    model.set_wedge(pt_F, pt_D, pt_D, pt_E)

    return model


if __name__ == "__main__":
    construct_0311_g2()
