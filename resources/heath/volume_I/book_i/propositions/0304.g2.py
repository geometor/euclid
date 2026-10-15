"""Programmatic construction for Book I, Proposition 21 (0304.g2).

Pappus Proof of Erycinus Paradox (Isosceles Case) on Book I, Proposition 21.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0304_g2() -> Model:
    """Construct the figure for 0304.g2 (I.21) using geometor.model."""
    model = Model("0304.g2")

    # Points
    pt_A = model.set_point(49, -134.5, classes=["given"], label="A")
    pt_B = model.set_point(200.5, -12, classes=["given"], label="B")
    pt_C = model.set_point(352, -134.5, classes=["given"], label="C")
    pt_D = model.set_point(243.8, -134.5, classes=["given"], label="D")
    pt_E = model.set_point(236, -85, classes=["given"], label="E")
    pt_F = model.set_point(286, -72, classes=["given"], label="F")
    pt_G = model.set_point(253, -83, classes=["given"], label="G")
    pt_H = model.set_point(307, -83, classes=["given"], label="H")
    pt_K = model.set_point(278, -83, classes=["given"], label="K")
    pt_L = model.set_point(104, -134.5, classes=["given"], label="L")
    pt_N = model.set_point(227, -31, classes=["given"], label="N")
    pt_O = model.set_point(101, -134.5, classes=["given"], label="O")
    pt_M = model.set_point(436, -178, classes=["given"], label="M")

    # Base Constructions (Lines and Circles)
    model.construct_circle(pt_A, pt_B)
    model.construct_circle(pt_K, pt_M)
    model.construct_line(pt_K, pt_C)

    # Segments
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_C, pt_L)
    model.set_segment(pt_A, pt_L)
    model.set_segment(pt_A, pt_D)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_B, pt_N)
    model.set_segment(pt_N, pt_C)
    model.set_segment(pt_F, pt_C)
    model.set_segment(pt_F, pt_H)
    model.set_segment(pt_C, pt_H)
    model.set_segment(pt_A, pt_F)
    model.set_segment(pt_A, pt_E)
    model.set_segment(pt_E, pt_F)
    model.set_segment(pt_E, pt_G)
    model.set_segment(pt_G, pt_F)
    model.set_segment(pt_A, pt_G)
    model.set_segment(pt_G, pt_H)
    model.set_segment(pt_G, pt_K)
    model.set_segment(pt_H, pt_K)
    model.set_segment(pt_K, pt_L)
    model.set_segment(pt_K, pt_M)
    model.set_segment(pt_K, pt_C)
    model.set_segment(pt_C, pt_M)
    model.set_segment(pt_K, pt_O)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_A, pt_F, pt_C])
    model.set_polygon([pt_G, pt_F, pt_H])
    model.set_polygon([pt_C, pt_H, pt_K])

    # Angles (Wedges)
    model.set_wedge(pt_B, pt_A, pt_A, pt_C)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_C, pt_A, pt_A, pt_B)

    return model


if __name__ == "__main__":
    construct_0304_g2()
