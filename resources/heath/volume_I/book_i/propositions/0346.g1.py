"""Programmatic construction for Book I, I.37 (0346.g1).

Triangles which are on the same base and in the same parallels are equal to one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0346_g1() -> Model:
    """Construct the figure for 0346.g1 (I.37) using geometor.model."""
    model = Model("0346.g1")

    # 1. Points
    E = model.set_point(31, -29, label="E")
    A = model.set_point(120, -29, classes=["given"], label="A")
    D = model.set_point(140, -29, classes=["given"], label="D")
    F = model.set_point(229, -29, label="F")
    B = model.set_point(64, -109.5, classes=["given"], label="B")
    C = model.set_point(153, -109.5, classes=["given"], label="C")
    E0 = model.set_point(20, -29, label="E0")
    F0 = model.set_point(235, -29, label="F0")

    # 2. Infinite / Extended Construction Lines
    model.construct_line(E0, F0)

    # 3. Segments
    model.set_segment(E, F)
    model.set_segment(E, A)
    model.set_segment(A, D)
    model.set_segment(D, F)
    model.set_segment(B, C)
    model.set_segment(B, E)
    model.set_segment(A, B)
    model.set_segment(C, A)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(C, F)

    # 4. Collinear Sections
    model.set_section([E, A, D])
    model.set_section([A, D, F])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C])
    model.set_polygon([D, B, C])
    model.set_polygon([E, B, C, A])
    model.set_polygon([D, B, C, F])
    model.set_polygon([E, A, B])
    model.set_polygon([F, D, C])

    return model


if __name__ == "__main__":
    construct_0346_g1()
