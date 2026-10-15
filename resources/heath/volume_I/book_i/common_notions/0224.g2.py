"""Programmatic construction for Book I, Postulate 5 Commentary: Wallis (0224.g2).

Wallis's second diagram showing similar triangles alpha-C-pi and ACP.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0224_g2() -> Model:
    """Construct the figure for 0224.g2 using geometor.model."""
    model = Model("0224.g2")

    # Given / Constructed Points (y-inverted from SVG coordinates)
    pt_F = model.set_point(44.0, -115.0, classes=["given"], label="F")
    pt_gamma = model.set_point(137.0, -115.0, classes=["given"], label="γ")
    pt_C = model.set_point(172.0, -115.0, classes=["given"], label="C")
    pt_alpha = model.set_point(186.0, -115.0, classes=["given"], label="α")
    pt_A = model.set_point(218.0, -115.0, classes=["given"], label="A")

    pt_B = model.set_point(188.0, -56.0, classes=["given"], label="B")
    pt_D = model.set_point(168.0, -58.1, classes=["given"], label="D")
    pt_beta = model.set_point(155.0, -54.0, classes=["given"], label="β")
    pt_pi = model.set_point(169.75, -83.04, classes=["given"], label="π")
    pt_P = model.set_point(164.61, -10.0, classes=["given"], label="P")

    # Base Construction Lines
    model.construct_line(pt_F, pt_A)
    model.construct_line(pt_A, pt_P)
    model.construct_line(pt_C, pt_P)
    model.construct_line(pt_alpha, pt_beta)

    # Segments
    model.set_segment(pt_A, pt_F)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_alpha, pt_C)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_P)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_C, pt_pi)
    model.set_segment(pt_C, pt_P)
    model.set_segment(pt_alpha, pt_beta)
    model.set_segment(pt_alpha, pt_pi)

    # Polygons
    model.set_polygon([pt_alpha, pt_C, pt_pi])
    model.set_polygon([pt_A, pt_C, pt_P])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_C, pt_C, pt_B)
    model.set_wedge(pt_C, pt_D, pt_D, pt_A)

    return model


if __name__ == "__main__":
    construct_0224_g2()
