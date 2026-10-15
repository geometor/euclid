"""Programmatic construction for Book I, I.34 (0338.g1).

In parallelogrammic areas the opposite sides and angles are equal to one another, and the diameter bisects the areas.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0338_g1() -> Model:
    """Construct the figure for 0338.g1 (I.34) using geometor.model."""
    model = Model("0338.g1")

    # 1. Points
    A = model.set_point(37, -37, classes=["given"], label="A")
    B = model.set_point(202, -37, classes=["given"], label="B")
    C = model.set_point(16, -117.5, classes=["given"], label="C")
    D = model.set_point(181, -117.5, classes=["given"], label="D")

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(B, C)

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, C, D, B])
    model.set_polygon([A, B, C])
    model.set_polygon([D, C, B])

    # 6. Angles (Wedges)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, B, B, D)
    model.set_wedge(C, A, A, B)
    model.set_wedge(B, C, C, D)
    model.set_wedge(A, B, B, C)
    model.set_wedge(D, C, C, B)
    model.set_wedge(B, A, A, D)
    model.set_wedge(C, A, A, D)

    return model


if __name__ == "__main__":
    construct_0338_g1()
