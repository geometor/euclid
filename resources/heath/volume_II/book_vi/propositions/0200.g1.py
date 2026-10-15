"""Programmatic construction for Book VI, Proposition 2 (0200.g1).

If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and conversely.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0200_g1() -> Model:
    """Construct the figure for 0200.g1 (VI.2) using geometor.model."""
    model = Model("0200.g1")

    # 1. Points
    A = model.set_point(55, -27, classes=["given"], label="A")
    B = model.set_point(27, -131, classes=["given"], label="B")
    C = model.set_point(132, -131, classes=["given"], label="C")
    D = model.set_point(36.24, -96.68, classes=["given"], label="D")
    E = model.set_point(106.59, -96.68, classes=["given"], label="E")

    # 3. Segments
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(A, C)
    model.set_segment(D, E)
    model.set_segment(B, C)
    model.set_segment(B, E)
    model.set_segment(C, D)

    # 4. Collinear Sections
    model.set_section([A, D, B])
    model.set_section([A, E, C])

    # 5. Polygons (Triangles)
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, E])
    model.set_polygon([B, D, E])
    model.set_polygon([C, D, E])

    return model


if __name__ == "__main__":
    construct_0200_g1()
