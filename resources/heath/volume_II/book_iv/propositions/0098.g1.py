"""Programmatic construction for Book IV, Proposition 6 Commentary (0098.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0098_g1() -> Model:
    """Construct the figure 0098.g1 using geometor.model."""
    model = Model("0098.g1")

    # Points (y-inverted for standard mathematical coordinates)
    O = model.set_point(86.00, -95.00, label="O")
    A = model.set_point(21.44, -108.72, classes=["given"], label="A")
    B_prime = model.set_point(45.37, -42.99, label="B'")
    B = model.set_point(72.28, -30.44, classes=["given"], label="B")
    C = model.set_point(135.05, -50.84, classes=["given"], label="C")
    D_prime = model.set_point(151.84, -90.40, label="D'")
    D = model.set_point(147.19, -119.72, classes=["given"], label="D")

    # Circle ABCD
    model.construct_circle(O, A)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)
    model.set_segment(A, C)
    model.set_segment(A, B_prime)
    model.set_segment(B_prime, C)
    model.set_segment(C, D_prime)
    model.set_segment(D_prime, A)

    # Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B_prime, C, D_prime])

    # Angles (wedges)
    model.set_wedge(A, B, B, B_prime)
    model.set_wedge(A, D, D, D_prime)

    return model


if __name__ == "__main__":
    construct_0098_g1()
