"""Programmatic construction for Book I, Proposition 26 (0316.g1).

If two triangles have the two angles equal to two angles respectively, and one
side equal to one side, namely, either the side adjoining the equal angles, or
that subtending one of the equal angles, they will also have the remaining sides
equal to the remaining sides and the remaining angle to the remaining angle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0316_g1() -> Model:
    """Construct the figure for Book I, Proposition 26 using geometor.model."""
    model = Model("0316.g1")

    # 1. Left triangle ABC with auxiliary points G on AB and H on BC
    A = model.set_point(32.5, -19, classes=["given"], label="A")
    B = model.set_point(13, -117, classes=["given"], label="B")
    C = model.set_point(127, -117, classes=["given"], label="C")
    G = model.set_point(26.5, -47, label="G")
    H = model.set_point(97, -117, label="H")

    # 2. Right triangle DEF
    D = model.set_point(224.5, -18.5, classes=["given"], label="D")
    E = model.set_point(207.5, -117, classes=["given"], label="E")
    F = model.set_point(317.5, -117, classes=["given"], label="F")

    # Segments and collinear sub-segments of ABC
    model.set_segment(A, B)
    model.set_segment(B, G)
    model.set_segment(A, G)
    model.set_section([A, G, B])

    model.set_segment(B, C)
    model.set_segment(B, H)
    model.set_segment(H, C)
    model.set_section([B, H, C])

    model.set_segment(A, C)
    model.set_segment(G, C)
    model.set_segment(A, H)

    # Polygons in left figure
    model.set_polygon([A, B, C])
    model.set_polygon([G, B, C])
    model.set_polygon([A, G, C])
    model.set_polygon([A, B, H])
    model.set_polygon([A, H, C])

    # Segments and polygon of DEF
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(E, F)
    model.set_polygon([D, E, F])

    # Angles (wedges)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, B, B, A)
    model.set_wedge(A, B, B, C)
    model.set_wedge(C, G, G, B)
    model.set_wedge(H, B, B, A)

    model.set_wedge(E, D, D, F)
    model.set_wedge(F, E, E, D)
    model.set_wedge(D, E, E, F)

    return model


if __name__ == "__main__":
    construct_0316_g1()
