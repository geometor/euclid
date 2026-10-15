"""Programmatic construction for Book I, Proposition 25 (0313.g1).

If two triangles have the two sides equal to two sides respectively, but have the base greater than the base, they will also have the one of the angles contained by the equal straight lines greater than the other.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0313_g1() -> Model:
    """Construct the figure for 0313.g1 (I.25) using geometor.model."""
    model = Model("0313.g1")

    # Points
    pt_A = model.set_point(60.5, -24, classes=["given"], label="A")
    pt_B = model.set_point(12, -114.5, classes=["given"], label="B")
    pt_C = model.set_point(144, -114.5, classes=["given"], label="C")
    pt_D = model.set_point(236, -23, classes=["given"], label="D")
    pt_E = model.set_point(220.5, -114.5, classes=["given"], label="E")
    pt_F = model.set_point(313, -114.5, classes=["given"], label="F")

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_D, pt_F)
    model.set_segment(pt_E, pt_F)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_D, pt_E, pt_F])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_B, pt_A, pt_A, pt_C)
    model.set_wedge(pt_C, pt_A, pt_A, pt_B)
    model.set_wedge(pt_D, pt_E, pt_E, pt_F)
    model.set_wedge(pt_E, pt_D, pt_D, pt_F)
    model.set_wedge(pt_F, pt_D, pt_D, pt_E)

    return model


if __name__ == "__main__":
    construct_0313_g1()
