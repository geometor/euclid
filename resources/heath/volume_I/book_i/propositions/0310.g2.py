"""Programmatic construction for Book I, Proposition 24 (0310.g2).

If two triangles have the two sides equal to two sides respectively, but have the one of the angles contained by the equal straight lines greater than the other, they will also have the base greater than the base.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0310_g2() -> Model:
    """Construct the figure for 0310.g2 (I.24) using geometor.model."""
    model = Model("0310.g2")

    # Points
    pt_A = model.set_point(46.5, -39.5, classes=["given"], label="A")
    pt_B = model.set_point(10.5, -140, classes=["given"], label="B")
    pt_C = model.set_point(101, -114, classes=["given"], label="C")
    pt_D = model.set_point(207.5, -34.5, classes=["given"], label="D")
    pt_E = model.set_point(172.5, -135, classes=["given"], label="E")
    pt_F = model.set_point(208, -138, classes=["given"], label="F")
    pt_G = model.set_point(260, -110, classes=["given"], label="G")

    # Segments
    model.set_segment(pt_A, pt_B)
    model.set_segment(pt_A, pt_C)
    model.set_segment(pt_B, pt_C)
    model.set_segment(pt_D, pt_E)
    model.set_segment(pt_D, pt_F)
    model.set_segment(pt_E, pt_F)
    model.set_segment(pt_D, pt_G)
    model.set_segment(pt_E, pt_G)
    model.set_segment(pt_F, pt_G)

    # Polygons
    model.set_polygon([pt_A, pt_B, pt_C])
    model.set_polygon([pt_D, pt_E, pt_F])
    model.set_polygon([pt_D, pt_E, pt_G])
    model.set_polygon([pt_D, pt_F, pt_G])
    model.set_polygon([pt_E, pt_F, pt_G])

    # Angles (Wedges)
    model.set_wedge(pt_A, pt_B, pt_B, pt_C)
    model.set_wedge(pt_D, pt_E, pt_E, pt_F)
    model.set_wedge(pt_D, pt_E, pt_E, pt_G)
    model.set_wedge(pt_D, pt_F, pt_F, pt_G)
    model.set_wedge(pt_G, pt_D, pt_D, pt_F)
    model.set_wedge(pt_F, pt_D, pt_D, pt_G)
    model.set_wedge(pt_G, pt_E, pt_E, pt_F)
    model.set_wedge(pt_F, pt_E, pt_E, pt_G)

    return model


if __name__ == "__main__":
    construct_0310_g2()
