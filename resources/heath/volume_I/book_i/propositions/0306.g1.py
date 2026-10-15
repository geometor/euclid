"""Programmatic construction for Book I, Proposition 22 (0306.g1).

Out of three straight lines, which are equal to three given straight lines, to construct a triangle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0306_g1() -> Model:
    """Construct the figure for 0306.g1 (I.22) using geometor.model."""
    model = Model("0306.g1")

    # Points
    pt_D = model.set_point(51, -107, classes=["given"], label="D")
    pt_F = model.set_point(147, -107, classes=["given"], label="F")
    pt_G = model.set_point(221, -107, classes=["given"], label="G")
    pt_H = model.set_point(278, -107, classes=["given"], label="H")
    pt_K = model.set_point(224.3, -50.1, classes=["given"], label="K")
    pt_L = model.set_point(224.3, -163.9, classes=["given"], label="L")
    pt_E = model.set_point(343, -107, classes=["given"], label="E")
    pt_A1 = model.set_point(391, -88.5, classes=["given"])
    pt_A2 = model.set_point(487, -88.5, classes=["given"], label="A")
    pt_B1 = model.set_point(391, -107, classes=["given"])
    pt_B2 = model.set_point(465, -107, classes=["given"], label="B")
    pt_C1 = model.set_point(391, -124.5, classes=["given"])
    pt_C2 = model.set_point(449, -124.5, classes=["given"], label="C")

    # Base Constructions (Lines and Circles)
    model.construct_line(pt_D, pt_E)
    model.construct_circle(pt_F, pt_D)
    model.construct_circle(pt_G, pt_H)

    # Segments
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_D, pt_F)
    model.set_segment(pt_F, pt_G)
    model.set_segment(pt_G, pt_H)
    model.set_segment(pt_F, pt_H)
    model.set_segment(pt_D, pt_G)
    model.set_segment(pt_D, pt_H)
    model.set_segment(pt_K, pt_F)
    model.set_segment(pt_K, pt_G)
    model.set_segment(pt_A1, pt_A2)
    model.set_segment(pt_B1, pt_B2)
    model.set_segment(pt_C1, pt_C2)

    # Polygons
    model.set_polygon([pt_K, pt_F, pt_G])

    # Angles (Wedges)
    model.set_wedge(pt_K, pt_F, pt_F, pt_G)
    model.set_wedge(pt_F, pt_K, pt_K, pt_G)
    model.set_wedge(pt_G, pt_K, pt_K, pt_F)

    return model


if __name__ == "__main__":
    construct_0306_g1()
