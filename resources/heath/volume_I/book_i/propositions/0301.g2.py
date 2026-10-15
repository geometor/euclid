"""Programmatic construction for Book I, Proposition 20 (0301.g2).

Second Alternative Proof of Book I, Proposition 20.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0301_g2() -> Model:
    """Construct the figure for 0301.g2 (I.20) using geometor.model."""
    model = Model("0301.g2")

    # Points
    pt_A = model.set_point(94.5, -17.5, classes=["given"], label="A")
    pt_B = model.set_point(15, -74.5, classes=["given"], label="B")
    pt_D = model.set_point(113, -74.5, classes=["given"], label="D")
    pt_C = model.set_point(171, -74.5, classes=["given"], label="C")

    # Segments
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_B, pt_D)
    model.set_segment(pt_D, pt_C)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_A, pt_D)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_D])
    model.set_polygon([pt_A, pt_D, pt_C])
    model.set_polygon([pt_A, pt_B, pt_C])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_A, pt_B, pt_B, pt_D)
    model.set_wedge(pt_A, pt_C, pt_C, pt_D)
    model.set_wedge(pt_D, pt_A, pt_A, pt_C)
    model.set_wedge(pt_D, pt_A, pt_A, pt_B)
    model.set_wedge(pt_B, pt_A, pt_A, pt_D)
    model.set_wedge(pt_C, pt_A, pt_A, pt_D)

    return model


if __name__ == "__main__":
    construct_0301_g2()
