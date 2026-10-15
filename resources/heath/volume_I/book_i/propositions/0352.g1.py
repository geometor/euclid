"""Programmatic construction for Book I, I.41 (0352.g1).

If a parallelogram have the same base with a triangle and be in the same parallels, the parallelogram is double of the triangle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0352_g1() -> Model:
    """Construct the figure for 0352.g1 (I.41) using geometor.model."""
    model = Model("0352.g1")

    # 1. Points
    A = model.set_point(24, -36, classes=["given"], label="A")
    B = model.set_point(48, -112, classes=["given"], label="B")
    C = model.set_point(142, -112, classes=["given"], label="C")
    D = model.set_point(118, -36, classes=["given"], label="D")
    E = model.set_point(184, -36, classes=["given"], label="E")

    # 3. Segments
    model.set_segment(A, E)
    model.set_segment(A, D)
    model.set_segment(D, E)
    model.set_segment(B, C)
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(A, C)
    model.set_segment(E, B)
    model.set_segment(E, C)

    # 4. Collinear Sections
    model.set_section([A, D, E])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C, D])
    model.set_polygon([E, B, C])
    model.set_polygon([A, B, C])

    return model


if __name__ == "__main__":
    construct_0352_g1()
