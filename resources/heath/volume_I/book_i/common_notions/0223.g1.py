"""Programmatic construction for Book I, Postulate 5 Commentary: Nasiraddin (0223.g1).

Saccheri/Nasiraddin quadrilateral ABCD with diagonal BC.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0223_g1() -> Model:
    """Construct the figure for 0223.g1 using geometor.model."""
    model = Model("0223.g1")

    # Given / Constructed Points (y-inverted from SVG coordinates)
    pt_D = model.set_point(20.0, -30.0, classes=["given"], label="D")
    pt_C = model.set_point(128.0, -30.0, classes=["given"], label="C")
    pt_B = model.set_point(20.0, -82.0, classes=["given"], label="B")
    pt_A = model.set_point(128.0, -82.0, classes=["given"], label="A")

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_B, pt_D)
    model.set_segment(pt_C, pt_D)
    model.set_segment(pt_B, pt_C)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_D, pt_C])
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_B, pt_D, pt_C])

    # Angles (Wedges)
    model.set_wedge(pt_C, pt_A, pt_A, pt_D)
    model.set_wedge(pt_D, pt_C, pt_C, pt_B)

    return model


if __name__ == "__main__":
    construct_0223_g1()
