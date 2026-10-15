"""Programmatic construction for Book III, Proposition 25 Case 1 (0061.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0061_g1() -> Model:
    """Construct the figure 0061.g1 using geometor.model."""
    model = Model("0061.g1")

    # Points (y-inverted)
    A = model.set_point(44.00, -28.00, classes=["given"], label="A")
    C = model.set_point(44.00, -152.00, classes=["given"], label="C")
    D = model.set_point(44.00, -90.00, label="D")
    B = model.set_point(27.34, -90.00, classes=["given"], label="B")
    E = model.set_point(151.00, -90.00, label="E")

    # Circle for segment ABC
    model.construct_circle(E, A)

    # Segments and sections
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(B, D)
    model.set_segment(D, E)
    model.set_segment(B, E)
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_section([A, D, C])
    model.set_section([B, D, E])

    # Polygons
    model.set_polygon([A, B, D])
    model.set_polygon([A, B, E])
    model.set_polygon([A, D, E])
    model.set_polygon([C, D, E])
    model.set_polygon([A, E, C])

    # Angles (wedges)
    model.set_wedge(B, A, A, D)
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, B, B, E)
    model.set_wedge(D, A, A, E)
    model.set_wedge(D, C, C, E)

    return model


if __name__ == "__main__":
    construct_0061_g1()
