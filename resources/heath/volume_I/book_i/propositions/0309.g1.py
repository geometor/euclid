"""Programmatic construction for Book I, Proposition 23 (0309.g1).

Modified Construction of Book I, Proposition 23 on Given Finite Base (Proclus).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0309_g1() -> Model:
    """Construct the figure for 0309.g1 (I.23) using geometor.model."""
    model = Model("0309.g1")

    # Points
    pt_F = model.set_point(33, -63.5, classes=["given"], label="F")
    pt_A = model.set_point(76, -63.5, classes=["given"], label="A")
    pt_G = model.set_point(152, -63.5, classes=["given"], label="G")
    pt_H = model.set_point(213, -63.5, classes=["given"], label="H")
    pt_B = model.set_point(236, -63.5, classes=["given"], label="B")
    pt_K = model.set_point(101.7, -29, classes=["given"], label="K")
    pt_C = model.set_point(281, -62.5, classes=["given"], label="C")
    pt_D = model.set_point(307, -28, classes=["given"], label="D")
    pt_E = model.set_point(357, -62.5, classes=["given"], label="E")

    # Base Constructions (Lines and Circles)
    model.construct_line(pt_B, pt_A)
    model.construct_circle(pt_A, pt_F)
    model.construct_circle(pt_G, pt_H)
    model.construct_line(pt_C, pt_D)
    model.construct_line(pt_C, pt_E)

    # Segments
    model.set_segment(pt_F, pt_B)
    model.set_segment(pt_A, pt_F)
    model.set_segment(pt_A, pt_G)
    model.set_segment(pt_G, pt_H)
    model.set_segment(pt_H, pt_B)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_G, pt_B)
    model.set_segment(pt_K, pt_A)
    model.set_segment(pt_K, pt_G)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_C, pt_E)
    model.set_segment(pt_D, pt_E)

    # Polygons
    model.set_polygon([pt_K, pt_A, pt_G])
    model.set_polygon([pt_D, pt_C, pt_E])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_K, pt_K, pt_G)
    model.set_wedge(pt_C, pt_D, pt_D, pt_E)

    return model


if __name__ == "__main__":
    construct_0309_g1()
