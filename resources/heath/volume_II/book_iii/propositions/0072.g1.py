"""Programmatic construction for Book III, Proposition 32 (0072.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0072_g1() -> Model:
    """Construct the figure 0072.g1 using geometor.model."""
    model = Model("0072.g1")

    # Center O (unlabeled) and points (y-inverted)
    O = model.set_point(103.0, -105.0, label="O")
    B = model.set_point(103.0, -184.0, classes=["given"], label="B")
    A = model.set_point(103.0, -26.0, label="A")
    E = model.set_point(18.0, -184.0, classes=["given"], label="E")
    F = model.set_point(190.0, -184.0, classes=["given"], label="F")
    D = model.set_point(142.0, -36.32, classes=["given"], label="D")
    C = model.set_point(176.0, -74.59, label="C")

    # Circle ABCD
    model.construct_circle(O, B)

    # Tangent EF
    model.construct_line(E, F)

    # Segments
    model.set_segment(E, F)
    model.set_segment(E, B)
    model.set_segment(B, F)
    model.set_segment(B, A)
    model.set_segment(B, D)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(C, B)

    # Section
    model.set_section([E, B, F])

    # Polygons
    model.set_polygon([A, B, D])
    model.set_polygon([B, C, D])
    model.set_polygon([A, B, C, D])

    # Angles
    model.set_wedge(B, F, F, D)
    model.set_wedge(B, E, E, D)
    model.set_wedge(D, A, A, B)
    model.set_wedge(A, B, B, D)
    model.set_wedge(B, A, A, D)
    model.set_wedge(B, A, A, F)
    model.set_wedge(C, D, D, B)

    return model


if __name__ == "__main__":
    construct_0072_g1()
