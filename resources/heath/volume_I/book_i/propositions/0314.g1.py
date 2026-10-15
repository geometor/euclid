"""Programmatic construction for Book I, Proposition 25 (0314.g1).

Menelaus of Alexandria Direct Proof of Book I, Proposition 25.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0314_g1() -> Model:
    """Construct the figure for 0314.g1 (I.25) using geometor.model."""
    model = Model("0314.g1")

    # Points
    pt_A = model.set_point(103, -19, classes=["given"], label="A")
    pt_B = model.set_point(79.5, -89.5, classes=["given"], label="B")
    pt_C = model.set_point(223.5, -89.5, classes=["given"], label="C")
    pt_G = model.set_point(168, -89.5, classes=["given"], label="G")
    pt_H = model.set_point(53.5, -166, classes=["given"], label="H")
    pt_K = model.set_point(193, -71.5, classes=["given"], label="K")
    pt_D = model.set_point(268.5, -15, classes=["given"], label="D")
    pt_E = model.set_point(284.5, -89.5, classes=["given"], label="E")
    pt_F = model.set_point(383.5, -89.5, classes=["given"], label="F")

    # Base Constructions (Lines and Circles)
    model.construct_line(pt_B, pt_C)
    model.construct_line(pt_H, pt_G)

    # Segments
    model.set_segment(pt_A, pt_H)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_A, pt_K)
    model.set_segment(pt_K, pt_C)
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_B, pt_G)
    model.set_segment(pt_G, pt_C)
    model.set_segment(pt_B, pt_H)
    model.set_segment(pt_H, pt_K)
    model.set_segment(pt_H, pt_G)
    model.set_segment(pt_G, pt_K)
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_D, pt_F)
    model.set_segment(pt_E, pt_F)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_A, pt_B, pt_H])
    model.set_polygon([pt_B, pt_H, pt_G])
    model.set_polygon([pt_A, pt_H, pt_K])
    model.set_polygon([pt_K, pt_G, pt_C])
    model.set_polygon([pt_D, pt_E, pt_F])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_D, pt_E, pt_E, pt_F)
    model.set_wedge(pt_B, pt_G, pt_G, pt_H)
    model.set_wedge(pt_E, pt_F, pt_F, pt_D)
    model.set_wedge(pt_H, pt_B, pt_B, pt_G)
    model.set_wedge(pt_A, pt_K, pt_K, pt_H)
    model.set_wedge(pt_H, pt_K, pt_K, pt_A)
    model.set_wedge(pt_A, pt_B, pt_B, pt_H)
    model.set_wedge(pt_H, pt_B, pt_B, pt_A)

    return model


if __name__ == "__main__":
    construct_0314_g1()
