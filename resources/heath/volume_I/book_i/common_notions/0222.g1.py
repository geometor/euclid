"""Programmatic construction for Book I, Postulate 5 Commentary: Proclus (0222.g1).

Proclus' diagram for straight lines AB, CD cut by EF with parallel KH through E.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0222_g1() -> Model:
    """Construct the figure for 0222.g1 using geometor.model."""
    model = Model("0222.g1")

    # Given / Constructed Points (y-inverted from SVG coordinates)
    pt_A = model.set_point(28.0, -21.3, classes=["given"], label="A")
    pt_E = model.set_point(115.0, -35.0, classes=["given"], label="E")
    pt_B = model.set_point(192.0, -47.1, classes=["given"], label="B")
    pt_K = model.set_point(20.0, -35.0, classes=["given"], label="K")
    pt_H = model.set_point(192.0, -35.0, classes=["given"], label="H")
    pt_C = model.set_point(20.0, -78.0, classes=["given"], label="C")
    pt_F = model.set_point(122.0, -78.0, classes=["given"], label="F")
    pt_D = model.set_point(187.0, -78.0, classes=["given"], label="D")

    # Base Construction Lines
    model.construct_line(pt_A, pt_B)
    model.construct_line(pt_K, pt_H)
    model.construct_line(pt_C, pt_D)
    model.construct_line(pt_E, pt_F)

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_E)
    model.set_segment(pt_E, pt_B)
    model.set_segment(pt_K, pt_H)
    model.set_segment(pt_K, pt_E)
    model.set_segment(pt_H, pt_E)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_C, pt_F)
    model.set_segment(pt_F, pt_D)
    model.set_segment(pt_E, pt_F)

    # Angles (Wedges)
    model.set_wedge(pt_E, pt_B, pt_B, pt_F)
    model.set_wedge(pt_E, pt_H, pt_H, pt_B)
    model.set_wedge(pt_E, pt_H, pt_H, pt_F)
    model.set_wedge(pt_F, pt_E, pt_E, pt_D)

    return model


if __name__ == "__main__":
    construct_0222_g1()
