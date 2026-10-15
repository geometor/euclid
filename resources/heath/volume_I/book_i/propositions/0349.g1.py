"""Programmatic construction for Book I, I.38 (0349.g1).

Heron's comparison of areas of triangles when the included angles are together less than two right angles (Case 2).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0349_g1() -> Model:
    """Construct the figure for 0349.g1 (I.38) using geometor.model."""
    model = Model("0349.g1")

    # 1. Points
    A = model.set_point(132.5, -17, classes=["given"], label="A")
    B = model.set_point(75, -82, classes=["given"], label="B")
    C = model.set_point(223, -82, classes=["given"], label="C")
    D = model.set_point(313, -17, classes=["given"], label="D")
    E = model.set_point(256, -82, classes=["given"], label="E")
    F = model.set_point(353, -115, classes=["given"], label="F")
    H = model.set_point(392, -70, label="H")
    G = model.set_point(404, -82, label="G")

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(E, F)
    model.set_segment(D, G)
    model.set_segment(D, H)
    model.set_segment(H, G)
    model.set_segment(F, H)
    model.set_segment(E, H)
    model.set_segment(E, G)

    # 4. Collinear Sections
    model.set_section([D, H, G])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([D, E, H])
    model.set_polygon([D, E, G])

    # 6. Angles (Wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(D, E, E, F)
    model.set_wedge(D, E, E, G)
    model.set_wedge(H, D, D, F)
    model.set_wedge(F, D, D, H)

    return model


if __name__ == "__main__":
    construct_0349_g1()
