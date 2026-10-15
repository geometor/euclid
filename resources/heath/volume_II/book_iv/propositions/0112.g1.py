"""Programmatic construction for Book IV, Proposition 14 (0112.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0112_g1() -> Model:
    """Construct the figure 0112.g1 (Circle circumscribed about regular pentagon) using geometor.model."""
    model = Model("0112.g1")

    # Points (y-inverted for standard mathematical coordinates)
    F = model.set_point(93.00, -97.00, label="F")
    A = model.set_point(93.00, -29.00, classes=["given"], label="A")
    B = model.set_point(28.33, -75.99, classes=["given"], label="B")
    C = model.set_point(53.03, -152.01, classes=["given"], label="C")
    D = model.set_point(132.97, -152.01, classes=["given"], label="D")
    E = model.set_point(157.67, -75.99, classes=["given"], label="E")

    # Circumscribed circle ABCDE
    model.construct_circle(F, A)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, A)
    model.set_segment(F, A)
    model.set_segment(F, B)
    model.set_segment(F, C)
    model.set_segment(F, D)
    model.set_segment(F, E)

    # Polygons
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([F, C, D])

    # Angles (wedges)
    model.set_wedge(B, C, C, D)
    model.set_wedge(C, D, D, E)
    model.set_wedge(C, B, B, A)
    model.set_wedge(B, A, A, E)
    model.set_wedge(A, E, E, D)
    model.set_wedge(F, C, C, D)
    model.set_wedge(C, D, D, F)

    return model


if __name__ == "__main__":
    construct_0112_g1()
