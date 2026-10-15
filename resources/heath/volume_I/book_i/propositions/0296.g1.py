"""Programmatic construction for Book I, Proposition 17 (0296.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0296_g1() -> Model:
    """Construct the figure 0296.g1 using geometor.model."""
    model = Model("0296.g1")

    # Points
    A = model.set_point(44, -35, classes=["given"], label="A")
    B = model.set_point(88, -116.5, classes=["given"], label="B")
    C = model.set_point(191, -116.5, classes=["given"], label="C")
    D = model.set_point(305, -116.5, label="D")

    # Construction lines
    model.construct_line(B, D)

    # Segments
    model.set_segment(B, D)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(C, D)

    # Collinear / broken sections
    model.set_section([B, C, D])

    # Polygons
    model.set_polygon([A, B, C])

    # Angles (wedges)
    model.set_wedge(C, A, A, D)
    model.set_wedge(C, A, A, B)
    model.set_wedge(B, A, A, C)
    model.set_wedge(A, B, B, C)

    return model


if __name__ == "__main__":
    construct_0296_g1()
