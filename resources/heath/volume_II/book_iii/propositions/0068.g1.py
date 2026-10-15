"""Programmatic construction for Book III, Proposition 31 (0068.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0068_g1() -> Model:
    """Construct the figure 0068.g1 using geometor.model."""
    model = Model("0068.g1")

    # Circle center E, points A, B, C, D on circle, and produced point F (y-inverted)
    E = model.set_point(129.00, -103.00, label="E")
    A = model.set_point(52.19, -89.46, classes=["given"], label="A")
    B = model.set_point(101.05, -175.82, classes=["given"], label="B")
    C = model.set_point(156.95, -30.18, classes=["given"], label="C")
    D = model.set_point(76.81, -45.03, classes=["given"], label="D")
    F = model.set_point(25.32, -41.96, label="F")

    # Circle ABCD
    model.construct_circle(E, A)

    # Segments and sections
    model.set_segment(B, C)
    model.set_segment(B, E)
    model.set_segment(E, C)
    model.set_segment(B, A)
    model.set_segment(A, F)
    model.set_segment(B, F)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(A, E)
    model.set_section([B, E, C])
    model.set_section([B, A, F])

    # Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, E])
    model.set_polygon([A, C, E])
    model.set_polygon([A, D, C])

    # Angles (wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, A, A, C)
    model.set_wedge(D, A, A, C)
    model.set_wedge(A, B, B, E)
    model.set_wedge(C, A, A, E)
    model.set_wedge(A, C, C, E)
    model.set_wedge(A, F, F, C)
    model.set_wedge(E, A, A, C)
    model.set_wedge(E, A, A, B)

    return model


if __name__ == "__main__":
    construct_0068_g1()
