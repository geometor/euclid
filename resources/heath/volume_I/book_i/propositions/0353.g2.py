"""Programmatic construction for Book I, I.42 (0353.g2).

To construct, in a given rectilineal angle, a parallelogram equal to a given triangle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0353_g2() -> Model:
    """Construct the figure for 0353.g2 (I.42) using geometor.model."""
    model = Model("0353.g2")

    # 1. Points
    A = model.set_point(88, -37, classes=["given"], label="A")
    B = model.set_point(67, -123, classes=["given"], label="B")
    C = model.set_point(195, -123, classes=["given"], label="C")
    E = model.set_point(131, -123, label="E")
    F = model.set_point(220, -37, label="F")
    G = model.set_point(284, -37, label="G")
    D = model.set_point(49.5, -90, classes=["given"], label="D")
    D1 = model.set_point(49.5, -37, label="D1")
    D2 = model.set_point(14, -54, label="D2")

    # 3. Segments
    model.set_segment(D, D1)
    model.set_segment(D, D2)
    model.set_segment(A, G)
    model.set_segment(A, F)
    model.set_segment(F, G)
    model.set_segment(B, C)
    model.set_segment(B, E)
    model.set_segment(E, C)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, E)
    model.set_segment(E, F)
    model.set_segment(C, G)

    # 4. Collinear Sections
    model.set_section([A, F, G])
    model.set_section([B, E, C])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, E])
    model.set_polygon([A, E, C])
    model.set_polygon([F, E, C, G])

    # 6. Angles (Wedges)
    model.set_wedge(D, D1, D1, D2)
    model.set_wedge(E, C, C, F)

    return model


if __name__ == "__main__":
    construct_0353_g2()
