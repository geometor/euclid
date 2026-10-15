"""Programmatic construction for Book I, I.41 (0353.g1).

Proclus' lemma: a triangle formed by joining the midpoint E of one non-parallel side DC of a trapezium ABCD to A and B is half the trapezium.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0353_g1() -> Model:
    """Construct the figure for 0353.g1 (I.41) using geometor.model."""
    model = Model("0353.g1")

    # 1. Points
    A = model.set_point(22, -37, classes=["given"], label="A")
    B = model.set_point(14, -96, classes=["given"], label="B")
    C = model.set_point(133, -96, classes=["given"], label="C")
    D = model.set_point(44, -37, classes=["given"], label="D")
    E = model.set_point(88.5, -66.5, classes=["given"], label="E")
    F = model.set_point(169, -37, label="F")

    # 3. Segments
    model.set_segment(A, F)
    model.set_segment(A, D)
    model.set_segment(D, F)
    model.set_segment(B, C)
    model.set_segment(A, B)
    model.set_segment(D, C)
    model.set_segment(D, E)
    model.set_segment(C, E)
    model.set_segment(B, F)
    model.set_segment(B, E)
    model.set_segment(E, F)
    model.set_segment(E, A)

    # 4. Collinear Sections
    model.set_section([A, D, F])
    model.set_section([D, E, C])
    model.set_section([B, E, F])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B, F])
    model.set_polygon([A, E, B])
    model.set_polygon([B, E, C])
    model.set_polygon([F, E, D])
    model.set_polygon([A, B, E, D])

    return model


if __name__ == "__main__":
    construct_0353_g1()
