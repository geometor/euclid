"""Programmatic construction for Book I, Proposition 21 (0304.g1).

Proclus Counterexample for Book I, Proposition 21 (Straight Lines not from Extremities).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0304_g1() -> Model:
    """Construct the figure for 0304.g1 (I.21) using geometor.model."""
    model = Model("0304.g1")

    # Points
    pt_A = model.set_point(14.5, -11, classes=["given"], label="A")
    pt_B = model.set_point(14.5, -126, classes=["given"], label="B")
    pt_C = model.set_point(221, -126, classes=["given"], label="C")
    pt_D = model.set_point(128, -126, classes=["given"], label="D")
    pt_E = model.set_point(48, -45, classes=["given"], label="E")
    pt_F = model.set_point(31, -28, classes=["given"], label="F")

    # Segments
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_B, pt_D)
    model.set_segment(pt_D, pt_C)
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_A, pt_D)
    model.set_segment(pt_A, pt_F)
    model.set_segment(pt_F, pt_E)
    model.set_segment(pt_E, pt_D)
    model.set_segment(pt_A, pt_E)
    model.set_segment(pt_F, pt_D)
    model.set_segment(pt_F, pt_C)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_A, pt_B, pt_D])
    model.set_polygon([pt_A, pt_F, pt_C])
    model.set_polygon([pt_F, pt_D, pt_C])

    # Angles (Wedges)
    model.set_wedge(pt_B, pt_A, pt_A, pt_C)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_C, pt_A, pt_A, pt_B)

    return model


if __name__ == "__main__":
    construct_0304_g1()
