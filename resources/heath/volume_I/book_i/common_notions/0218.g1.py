"""Programmatic construction for Book I, Postulate 5 Commentary: Ptolemy (0218.g1).

Ptolemy's proof of Euclid I. 28.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0218_g1() -> Model:
    """Construct the figure for 0218.g1 using geometor.model."""
    model = Model("0218.g1")

    # Given / Constructed Points (y-inverted from SVG coordinates)
    pt_A = model.set_point(52.0, -49.0, classes=["given"], label="A")
    pt_B = model.set_point(185.0, -49.0, classes=["given"], label="B")
    pt_C = model.set_point(52.0, -95.0, classes=["given"], label="C")
    pt_D = model.set_point(185.0, -95.0, classes=["given"], label="D")
    pt_F = model.set_point(110.0, -49.0, classes=["given"], label="F")
    pt_G = model.set_point(93.0, -95.0, classes=["given"], label="G")
    pt_E = model.set_point(121.1, -19.0, classes=["given"], label="E")
    pt_H = model.set_point(81.9, -125.0, classes=["given"], label="H")
    pt_L = model.set_point(25.0, -72.0, classes=["given"], label="L")
    pt_K = model.set_point(212.0, -72.0, classes=["given"], label="K")

    # Auxiliary points from Heath's commentary note
    pt_O = model.set_point(101.5, -72.0, classes=["auxiliary"], label="O")
    pt_M = model.set_point(101.5, -49.0, classes=["auxiliary"], label="M")
    pt_N = model.set_point(101.5, -95.0, classes=["auxiliary"], label="N")

    # Base Construction Lines
    model.construct_line(pt_A, pt_B)
    model.construct_line(pt_C, pt_D)
    model.construct_line(pt_E, pt_H)

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_E, pt_H)
    model.set_segment(pt_E, pt_F)
    model.set_segment(pt_F, pt_G)
    model.set_segment(pt_G, pt_H)
    model.set_segment(pt_F, pt_A)
    model.set_segment(pt_F, pt_B)
    model.set_segment(pt_G, pt_C)
    model.set_segment(pt_G, pt_D)
    model.set_segment(pt_A, pt_L)
    model.set_segment(pt_C, pt_L)
    model.set_segment(pt_B, pt_K)
    model.set_segment(pt_D, pt_K)
    model.set_segment(pt_O, pt_F)
    model.set_segment(pt_O, pt_G)
    model.set_segment(pt_M, pt_N)
    model.set_segment(pt_M, pt_A)
    model.set_segment(pt_N, pt_C)

    # Polygons
    model.set_polygon([pt_K, pt_F, pt_G])
    model.set_polygon([pt_O, pt_M, pt_F])
    model.set_polygon([pt_O, pt_N, pt_G])
    model.set_polygon([pt_M, pt_A, pt_L, pt_C, pt_N])
    model.set_polygon([pt_N, pt_D, pt_K, pt_B, pt_M])

    # Angles (Wedges)
    model.set_wedge(pt_F, pt_B, pt_B, pt_G)
    model.set_wedge(pt_G, pt_F, pt_F, pt_D)
    model.set_wedge(pt_F, pt_G, pt_G, pt_A)
    model.set_wedge(pt_G, pt_C, pt_C, pt_F)
    model.set_wedge(pt_O, pt_M, pt_M, pt_F)
    model.set_wedge(pt_O, pt_N, pt_N, pt_G)
    model.set_wedge(pt_N, pt_G, pt_G, pt_O)

    return model


if __name__ == "__main__":
    construct_0218_g1()
