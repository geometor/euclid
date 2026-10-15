"""Programmatic construction for Postulate 5 Commentary, Legendre (0231.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0231_g2() -> Model:
    """Construct the figure 0231.g2 (Legendre's Theorem III) using geometor.model."""
    model = Model("0231.g2")

    # Points (y negated for Cartesian coordinates)
    A = model.set_point(113, -22, classes=["given"], label="A")
    B = model.set_point(25, -100, classes=["given"], label="B")
    D = model.set_point(88, -100, label="D")
    C = model.set_point(155, -100, classes=["given"], label="C")

    # Construction lines
    model.construct_line(B, C)
    model.construct_line(A, B)
    model.construct_line(A, C)
    model.construct_line(A, D)

    # Segments (including collinear sub-segments)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)

    # Collinear section
    model.set_section([B, D, C])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])

    # Angles (wedges)
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, D, D, C)
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, D, D, A)
    model.set_wedge(C, A, A, D)
    model.set_wedge(D, A, A, B)
    model.set_wedge(D, C, C, A)

    return model


if __name__ == "__main__":
    construct_0231_g2()
