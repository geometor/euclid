"""Programmatic construction for Book I, Postulate 5 Commentary: Proclus (0221.g1).

Proclus' diagram for a straight line EFG cutting parallel lines AB and CD.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0221_g1() -> Model:
    """Construct the figure for 0221.g1 using geometor.model."""
    model = Model("0221.g1")

    # Given Points (y-inverted from SVG coordinates)
    pt_A = model.set_point(28.0, -46.0, classes=["given"], label="A")
    pt_F = model.set_point(96.0, -46.0, classes=["given"], label="F")
    pt_B = model.set_point(162.0, -46.0, classes=["given"], label="B")
    pt_C = model.set_point(28.0, -90.0, classes=["given"], label="C")
    pt_D = model.set_point(162.0, -90.0, classes=["given"], label="D")
    pt_E = model.set_point(75.0, -25.0, classes=["given"], label="E")
    pt_G = model.set_point(121.0, -71.0, classes=["given"], label="G")

    # Base Construction Lines
    model.construct_line(pt_A, pt_B)
    model.construct_line(pt_C, pt_D)
    model.construct_line(pt_E, pt_G)

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_F)
    model.set_segment(pt_B, pt_F)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_E, pt_G)
    model.set_segment(pt_E, pt_F)
    model.set_segment(pt_F, pt_G)

    # Angles (Wedges)
    model.set_wedge(pt_F, pt_B, pt_B, pt_G)

    return model


if __name__ == "__main__":
    construct_0221_g1()
