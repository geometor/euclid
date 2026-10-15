"""Programmatic construction for Book I, Proposition 20 (0302.g2).

Third Alternative Proof of Book I, Proposition 20 (Case 2).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0302_g2() -> Model:
    """Construct the figure for 0302.g2 (I.20) using geometor.model."""
    model = Model("0302.g2")

    # Points
    pt_A = model.set_point(65, -23.5, classes=["given"], label="A")
    pt_B = model.set_point(8.5, -78.5, classes=["given"], label="B")
    pt_D = model.set_point(63.5, -78.5, classes=["given"], label="D")
    pt_E = model.set_point(93.5, -78.5, classes=["given"], label="E")
    pt_C = model.set_point(180, -78.5, classes=["given"], label="C")

    # Segments
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_B, pt_D)
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_E, pt_C)
    model.set_segment(pt_B, pt_E)
    model.set_segment(pt_D, pt_C)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_A, pt_D)
    model.set_segment(pt_A, pt_E)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_D])
    model.set_polygon([pt_A, pt_D, pt_E])
    model.set_polygon([pt_A, pt_E, pt_C])
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_A, pt_D, pt_C])
    model.set_polygon([pt_A, pt_B, pt_E])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_A, pt_B, pt_B, pt_D)
    model.set_wedge(pt_A, pt_D, pt_D, pt_E)
    model.set_wedge(pt_A, pt_C, pt_C, pt_E)
    model.set_wedge(pt_A, pt_D, pt_D, pt_C)
    model.set_wedge(pt_A, pt_B, pt_B, pt_E)
    model.set_wedge(pt_D, pt_B, pt_B, pt_A)
    model.set_wedge(pt_E, pt_C, pt_C, pt_A)

    return model


if __name__ == "__main__":
    construct_0302_g2()
