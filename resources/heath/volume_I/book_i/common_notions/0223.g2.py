"""Programmatic construction for Book I, Postulate 5 Commentary: Nasiraddin (0223.g2).

Nasiraddin at-Tusi's proof of Postulate 5 with step-like perpendiculars.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0223_g2() -> Model:
    """Construct the figure for 0223.g2 using geometor.model."""
    model = Model("0223.g2")

    # Given / Constructed Points (y-inverted from SVG coordinates)
    pt_F = model.set_point(22.0, -122.0, classes=["given"], label="F")
    pt_M = model.set_point(60.0, -122.0, classes=["given"], label="M")
    pt_C = model.set_point(67.0, -122.0, classes=["given"], label="C")
    pt_L = model.set_point(98.0, -122.0, classes=["given"], label="L")
    pt_K = model.set_point(136.0, -122.0, classes=["given"], label="K")
    pt_S = model.set_point(136.0, -122.0, classes=["given"], label="S")
    pt_H = model.set_point(174.0, -122.0, classes=["given"], label="H")
    pt_E = model.set_point(212.0, -122.0, classes=["given"], label="E")

    pt_D = model.set_point(67.0, -56.0, classes=["given"], label="D")
    pt_A = model.set_point(246.5, -142.0, classes=["given"], label="A")
    pt_G = model.set_point(174.0, -100.0, classes=["given"], label="G")
    pt_N = model.set_point(136.0, -78.0, classes=["given"], label="N")
    pt_B = model.set_point(117.0, -67.0, classes=["given"], label="B")
    pt_O = model.set_point(98.0, -56.0, classes=["given"], label="O")
    pt_P = model.set_point(60.0, -34.0, classes=["given"], label="P")

    pt_Q = model.set_point(212.0, -100.0, classes=["given"], label="Q")
    pt_R = model.set_point(136.0, -100.0, classes=["given"], label="R")

    # Base Construction Lines
    model.construct_line(pt_F, pt_E)
    model.construct_line(pt_A, pt_P)
    model.construct_line(pt_C, pt_D)

    # Segments
    model.set_segment(pt_F, pt_E)
    model.set_segment(pt_C, pt_E)
    model.set_segment(pt_E, pt_H)
    model.set_segment(pt_H, pt_C)
    model.set_segment(pt_H, pt_K)
    model.set_segment(pt_S, pt_H)
    model.set_segment(pt_K, pt_L)
    model.set_segment(pt_E, pt_M)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_E, pt_B)
    model.set_segment(pt_G, pt_B)
    model.set_segment(pt_E, pt_G)
    model.set_segment(pt_G, pt_N)
    model.set_segment(pt_N, pt_O)
    model.set_segment(pt_E, pt_P)
    model.set_segment(pt_G, pt_H)
    model.set_segment(pt_N, pt_S)
    model.set_segment(pt_S, pt_R)
    model.set_segment(pt_O, pt_L)
    model.set_segment(pt_P, pt_M)
    model.set_segment(pt_E, pt_Q)
    model.set_segment(pt_Q, pt_G)
    model.set_segment(pt_G, pt_R)
    model.set_segment(pt_R, pt_Q)

    # Polygons
    model.set_polygon([pt_P, pt_M, pt_E])
    model.set_polygon([pt_G, pt_H, pt_E])
    model.set_polygon([pt_N, pt_R, pt_G])
    model.set_polygon([pt_E, pt_Q, pt_G])

    # Angles (Wedges)
    model.set_wedge(pt_C, pt_D, pt_D, pt_E)
    model.set_wedge(pt_E, pt_C, pt_C, pt_B)
    model.set_wedge(pt_Q, pt_E, pt_E, pt_G)
    model.set_wedge(pt_G, pt_Q, pt_Q, pt_H)
    model.set_wedge(pt_R, pt_G, pt_G, pt_S)
    model.set_wedge(pt_G, pt_H, pt_H, pt_R)
    model.set_wedge(pt_G, pt_R, pt_R, pt_N)
    model.set_wedge(pt_G, pt_Q, pt_Q, pt_E)
    model.set_wedge(pt_R, pt_N, pt_N, pt_G)

    return model


if __name__ == "__main__":
    construct_0223_g2()
