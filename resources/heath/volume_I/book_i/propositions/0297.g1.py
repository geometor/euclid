"""Programmatic construction for Book I, Proposition 18 (0297.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0297_g1() -> Model:
    """Construct the figure 0297.g1 using geometor.model."""
    model = Model("0297.g1")

    # Points
    A = model.set_point(18, -26, classes=["given"], label="A")
    B = model.set_point(70, -113.5, classes=["given"], label="B")
    C = model.set_point(246, -113.5, classes=["given"], label="C")
    D = model.set_point(113, -62.5, label="D")

    # Construction lines
    model.construct_line(A, C)

    # Construction circles
    model.construct_circle(A, B)

    # Segments
    model.set_segment(B, C)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(A, D)
    model.set_segment(D, C)

    # Collinear / broken sections
    model.set_section([A, D, C])

    # Polygons
    model.set_polygon([A, B, D])
    model.set_polygon([B, C, D])
    model.set_polygon([A, B, C])

    # Angles (wedges)
    model.set_wedge(B, A, A, C)
    model.set_wedge(B, A, A, D)
    model.set_wedge(B, D, D, C)
    model.set_wedge(D, A, A, B)
    model.set_wedge(D, B, B, C)
    model.set_wedge(C, A, A, B)
    model.set_wedge(A, B, B, C)

    return model


if __name__ == "__main__":
    construct_0297_g1()
