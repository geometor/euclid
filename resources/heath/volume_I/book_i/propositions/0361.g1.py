"""Programmatic construction for Book I, I.46 (0361.g1).

On a given straight line to describe a square.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0361_g1() -> Model:
    """Construct the figure for 0361.g1 (I.46) using geometor.model."""
    model = Model("0361.g1")

    # 1. Points
    A = model.set_point(30, -196, classes=["given"], label="A")
    B = model.set_point(134, -196, classes=["given"], label="B")
    D = model.set_point(30, -92, label="D")
    E = model.set_point(134, -92, label="E")
    C = model.set_point(30, -21, label="C")

    # 3. Segments
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(A, B)
    model.set_segment(D, E)
    model.set_segment(B, E)

    # 4. Collinear Sections
    model.set_section([A, D, C])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, D, E, B])

    # 6. Angles (Wedges)
    model.set_wedge(A, B, B, D)
    model.set_wedge(D, A, A, E)
    model.set_wedge(B, A, A, E)
    model.set_wedge(E, B, B, D)

    return model


if __name__ == "__main__":
    construct_0361_g1()
