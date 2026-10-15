"""Programmatic construction for Book I, Proposition 19 (0299.g1).

Heron and an-Nairizi Lemma for Direct Proof of Book I, Proposition 19.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0299_g1() -> Model:
    """Construct the figure for 0299.g1 (I.19) using geometor.model."""
    model = Model("0299.g1")

    # Points
    pt_A = model.set_point(69, -23.5, classes=["given"], label="A")
    pt_B = model.set_point(15, -98, classes=["given"], label="B")
    pt_D = model.set_point(79, -98, classes=["given"], label="D")
    pt_F = model.set_point(137, -98, classes=["given"], label="F")
    pt_C = model.set_point(200, -98, classes=["given"], label="C")
    pt_G = model.set_point(152, -72, classes=["given"], label="G")
    pt_E = model.set_point(90, -167, classes=["given"], label="E")

    # Base Constructions (Lines and Circles)
    model.construct_line(pt_A, pt_D)
    model.construct_line(pt_E, pt_F)

    # Segments
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_B, pt_D)
    model.set_segment(pt_D, pt_F)
    model.set_segment(pt_F, pt_C)
    model.set_segment(pt_D, pt_C)
    model.set_segment(pt_B, pt_F)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_A, pt_G)
    model.set_segment(pt_G, pt_C)
    model.set_segment(pt_A, pt_E)
    model.set_segment(pt_A, pt_D)
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_E, pt_G)
    model.set_segment(pt_E, pt_F)
    model.set_segment(pt_F, pt_G)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_A, pt_B, pt_D])
    model.set_polygon([pt_E, pt_F, pt_D])
    model.set_polygon([pt_A, pt_E, pt_G])
    model.set_polygon([pt_A, pt_D, pt_C])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_A, pt_B, pt_B, pt_D)
    model.set_wedge(pt_A, pt_D, pt_D, pt_G)
    model.set_wedge(pt_D, pt_A, pt_A, pt_B)
    model.set_wedge(pt_D, pt_E, pt_E, pt_F)
    model.set_wedge(pt_E, pt_D, pt_D, pt_F)

    return model


if __name__ == "__main__":
    construct_0299_g1()
