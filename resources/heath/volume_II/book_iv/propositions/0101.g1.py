"""Programmatic construction for Book IV, Proposition 9 (0101.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0101_g1() -> Model:
    """Construct the figure 0101.g1 using geometor.model."""
    model = Model("0101.g1")

    # Points (y-inverted for standard mathematical coordinates)
    E = model.set_point(87.00, -89.00, label="E")
    A = model.set_point(87.00, -30.00, classes=["given"], label="A")
    B = model.set_point(28.00, -89.00, classes=["given"], label="B")
    C = model.set_point(87.00, -148.00, classes=["given"], label="C")
    D = model.set_point(146.00, -89.00, classes=["given"], label="D")

    # Circumscribed circle ABCD
    model.construct_circle(E, A)

    # Construction lines (diagonals)
    model.construct_line(A, C)
    model.construct_line(B, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(E, A)
    model.set_segment(E, B)
    model.set_segment(E, C)
    model.set_segment(E, D)

    # Collinear sections
    model.set_section([A, E, C])
    model.set_section([B, E, D])

    # Polygons
    model.set_polygon([A, B, C, D])

    # Angles (wedges)
    model.set_wedge(A, D, D, B)
    model.set_wedge(A, D, D, C)
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, A, A, C)
    model.set_wedge(B, E, E, A)
    model.set_wedge(C, B, B, D)
    model.set_wedge(D, C, C, A)

    return model


if __name__ == "__main__":
    construct_0101_g1()
