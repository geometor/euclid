"""Programmatic construction for Book I, Proposition 20 (0302.g1).

Third Alternative Proof of Book I, Proposition 20 (Case 1).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0302_g1() -> Model:
    """Construct the figure for 0302.g1 (I.20) using geometor.model."""
    model = Model("0302.g1")

    # Points
    pt_A = model.set_point(74.5, -25.5, classes=["given"], label="A")
    pt_B = model.set_point(17, -83.5, classes=["given"], label="B")
    pt_D = model.set_point(101.5, -83.5, classes=["given"], label="D")
    pt_C = model.set_point(183, -83.5, classes=["given"], label="C")

    # Segments
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_B, pt_D)
    model.set_segment(pt_D, pt_C)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_A, pt_D)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_D])
    model.set_polygon([pt_A, pt_C, pt_D])
    model.set_polygon([pt_A, pt_B, pt_C])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_A, pt_B, pt_B, pt_D)
    model.set_wedge(pt_A, pt_C, pt_C, pt_D)
    model.set_wedge(pt_D, pt_B, pt_B, pt_A)
    model.set_wedge(pt_D, pt_C, pt_C, pt_A)

    return model


if __name__ == "__main__":
    construct_0302_g1()
