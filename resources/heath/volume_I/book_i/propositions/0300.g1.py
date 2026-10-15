"""Programmatic construction for Book I, Proposition 19 (0300.g1).

Heron and an-Nairizi Direct Proof of Book I, Proposition 19.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0300_g1() -> Model:
    """Construct the figure for 0300.g1 (I.19) using geometor.model."""
    model = Model("0300.g1")

    # Points
    pt_A = model.set_point(64.5, -28.5, classes=["given"], label="A")
    pt_B = model.set_point(24.5, -100.5, classes=["given"], label="B")
    pt_D = model.set_point(93, -100.5, classes=["given"], label="D")
    pt_C = model.set_point(159.5, -100.5, classes=["given"], label="C")
    pt_F = model.set_point(89, -80.5, classes=["given"], label="F")
    pt_E = model.set_point(123.5, -170.5, classes=["given"], label="E")

    # Base Constructions (Lines and Circles)
    model.construct_line(pt_A, pt_D)

    # Segments
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_B, pt_D)
    model.set_segment(pt_D, pt_C)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_A, pt_E)
    model.set_segment(pt_A, pt_D)
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_A, pt_F)
    model.set_segment(pt_F, pt_D)
    model.set_segment(pt_F, pt_E)
    model.set_segment(pt_B, pt_E)
    model.set_segment(pt_B, pt_F)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_A, pt_B, pt_D])
    model.set_polygon([pt_E, pt_C, pt_D])
    model.set_polygon([pt_A, pt_B, pt_F])
    model.set_polygon([pt_B, pt_F, pt_E])
    model.set_polygon([pt_A, pt_B, pt_E])

    # Angles (Wedges)
    model.set_wedge(pt_B, pt_A, pt_A, pt_C)
    model.set_wedge(pt_C, pt_A, pt_A, pt_B)
    model.set_wedge(pt_B, pt_D, pt_D, pt_E)
    model.set_wedge(pt_B, pt_A, pt_A, pt_E)
    model.set_wedge(pt_B, pt_A, pt_A, pt_F)
    model.set_wedge(pt_B, pt_E, pt_E, pt_F)
    model.set_wedge(pt_D, pt_A, pt_A, pt_B)
    model.set_wedge(pt_D, pt_E, pt_E, pt_C)

    return model


if __name__ == "__main__":
    construct_0300_g1()
