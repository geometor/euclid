"""Programmatic construction for Book I, Postulate 5 Commentary: Wallis (0224.g1).

Wallis's first diagram showing translation of AB along AF to position alpha-beta at C.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0224_g1() -> Model:
    """Construct the figure for 0224.g1 using geometor.model."""
    model = Model("0224.g1")

    # Given / Constructed Points (y-inverted from SVG coordinates)
    pt_F = model.set_point(40.0, -92.0, classes=["given"], label="F")
    pt_gamma = model.set_point(78.0, -92.0, classes=["given"], label="γ")
    pt_C = model.set_point(135.0, -92.0, classes=["given"], label="C")
    pt_alpha = model.set_point(135.0, -92.0, classes=["given"], label="α")
    pt_A = model.set_point(192.0, -92.0, classes=["given"], label="A")
    pt_E = model.set_point(218.0, -92.0, classes=["given"], label="E")

    pt_B = model.set_point(162.0, -34.0, classes=["given"], label="B")
    pt_D = model.set_point(123.0, -36.0, classes=["given"], label="D")
    pt_beta = model.set_point(105.0, -34.0, classes=["given"], label="β")

    # Base Construction Lines
    model.construct_line(pt_F, pt_E)
    model.construct_line(pt_A, pt_B)
    model.construct_line(pt_C, pt_D)
    model.construct_line(pt_alpha, pt_beta)

    # Segments
    model.set_segment(pt_A, pt_F)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_alpha, pt_gamma)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_alpha, pt_beta)

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_C, pt_C, pt_B)
    model.set_wedge(pt_C, pt_D, pt_D, pt_A)
    model.set_wedge(pt_C, pt_gamma, pt_gamma, pt_beta)

    return model


if __name__ == "__main__":
    construct_0224_g1()
