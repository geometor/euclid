"""Programmatic construction for Postulate 5 Commentary, Legendre (0232.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0232_g1() -> Model:
    """Construct the figure 0232.g1 (Legendre's Theorem V) using geometor.model."""
    model = Model("0232.g1")

    # Points (y negated for Cartesian coordinates)
    A_prime = model.set_point(10, -192, label="A'")
    A = model.set_point(63, -192, classes=["given"], label="A")
    B = model.set_point(175, -192, classes=["given"], label="B")
    C = model.set_point(175, -115, classes=["given"], label="C")
    C_prime = model.set_point(175, -23, label="C'")

    # Construction lines
    model.construct_line(A_prime, B)
    model.construct_line(B, C_prime)
    model.construct_line(A, C)
    model.construct_line(A_prime, C_prime)
    model.construct_line(A, C_prime)

    # Segments (including collinear sub-segments)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, C)
    model.set_segment(A_prime, A)
    model.set_segment(A_prime, B)
    model.set_segment(C, C_prime)
    model.set_segment(B, C_prime)
    model.set_segment(A_prime, C_prime)
    model.set_segment(A, C_prime)

    # Collinear sections
    model.set_section([A_prime, A, B])
    model.set_section([B, C, C_prime])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A_prime, B, C_prime])
    model.set_polygon([A, B, C_prime])
    model.set_polygon([A_prime, A, C_prime])
    model.set_polygon([A, C, C_prime])

    # Angles (wedges)
    model.set_wedge(B, C, C, A)
    model.set_wedge(A, B, B, C)
    model.set_wedge(C, A, A, B)
    model.set_wedge(A_prime, B, B, C_prime)
    model.set_wedge(C_prime, A_prime, A_prime, B)

    return model


if __name__ == "__main__":
    construct_0232_g1()
