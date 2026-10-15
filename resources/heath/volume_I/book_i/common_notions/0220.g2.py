"""Programmatic construction for Book I, Postulate 5 Commentary: Proclus (0220.g2).

Diagram of Zeno-like bisection argument examined by Proclus.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0220_g2() -> Model:
    """Construct the figure for 0220.g2 using geometor.model."""
    model = Model("0220.g2")

    # Given / Constructed Points (y-inverted from SVG coordinates)
    pt_A = model.set_point(28.0, -30.0, classes=["given"], label="A")
    pt_B = model.set_point(240.0, -38.0, classes=["given"], label="B")
    pt_C = model.set_point(28.0, -96.0, classes=["given"], label="C")
    pt_D = model.set_point(240.0, -88.0, classes=["given"], label="D")
    pt_E = model.set_point(28.0, -63.0, classes=["given"], label="E")
    pt_F = model.set_point(61.0, -31.25, classes=["given"], label="F")
    pt_G = model.set_point(61.0, -94.75, classes=["given"], label="G")
    pt_H = model.set_point(61.0, -63.0, classes=["given"], label="H")
    pt_K = model.set_point(93.0, -32.45, classes=["given"], label="K")
    pt_L = model.set_point(93.0, -93.55, classes=["given"], label="L")

    # Base Construction Lines
    model.construct_line(pt_A, pt_B)
    model.construct_line(pt_C, pt_D)
    model.construct_line(pt_A, pt_C)

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_F)
    model.set_segment(pt_F, pt_K)
    model.set_segment(pt_K, pt_B)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_C, pt_G)
    model.set_segment(pt_G, pt_L)
    model.set_segment(pt_L, pt_D)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_A, pt_E)
    model.set_segment(pt_E, pt_C)
    model.set_segment(pt_F, pt_G)
    model.set_segment(pt_F, pt_H)
    model.set_segment(pt_H, pt_G)
    model.set_segment(pt_K, pt_L)
    model.set_segment(pt_A, pt_G)

    # Polygons
    model.set_polygon([pt_A, pt_C, pt_G])
    model.set_polygon([pt_A, pt_F, pt_G])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_C, pt_A, pt_A, pt_D)

    return model


if __name__ == "__main__":
    construct_0220_g2()
