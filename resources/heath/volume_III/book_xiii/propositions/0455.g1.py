"""Programmatic construction for Book XIII, Proposition 7 (0455.g1).

If three angles of an equilateral pentagon, taken either in order or not in
order, be equal, the pentagon will be equiangular.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0455_g1() -> Model:
    """Construct the figure for Book XIII, Proposition 7 using geometor.model."""
    model = Model("0455.g1")

    # Equilateral pentagon ABCDE
    A = model.set_point(103.0, -21.0, classes=["given"], label="A")
    B = model.set_point(25.0, -78.0, classes=["given"], label="B")
    C = model.set_point(55.0, -170.0, classes=["given"], label="C")
    D = model.set_point(151.0, -170.0, classes=["given"], label="D")
    E = model.set_point(181.0, -78.0, classes=["given"], label="E")

    # Intersection F of diagonals AC and BE
    F = model.set_point(84.6, -78.0, label="F")

    # Pentagon sides
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, A)

    # Diagonals and sub-segments
    model.set_segment(A, C)
    model.set_segment(A, F)
    model.set_segment(F, C)
    model.set_segment(B, E)
    model.set_segment(B, F)
    model.set_segment(F, E)
    model.set_segment(F, D)
    model.set_segment(B, D)

    # Polygons
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, E])
    model.set_polygon([F, C, D])
    model.set_polygon([F, E, D])
    model.set_polygon([B, C, D])
    model.set_polygon([B, D, E])
    model.set_polygon([A, B, F])

    # Angles (wedges)
    model.set_wedge(B, C, C, A)
    model.set_wedge(A, B, B, E)
    model.set_wedge(C, B, B, A)
    model.set_wedge(E, B, B, A)
    model.set_wedge(B, A, A, E)
    model.set_wedge(A, C, C, B)
    model.set_wedge(C, F, F, D)
    model.set_wedge(E, F, F, D)
    model.set_wedge(C, B, B, D)
    model.set_wedge(E, A, A, D)
    model.set_wedge(D, C, C, E)
    model.set_wedge(D, C, C, B)
    model.set_wedge(D, B, B, E)

    return model


if __name__ == "__main__":
    construct_0455_g1()
