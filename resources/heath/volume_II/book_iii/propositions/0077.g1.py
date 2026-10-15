"""Programmatic construction for Book III, Proposition 34 (0077.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0077_g1() -> Model:
    """Construct the figure 0077.g1 using geometor.model."""
    model = Model("0077.g1")

    # Circle ABC with center O(97, -95), radius 67 (y-inverted)
    O = model.set_point(97.0, -95.0, label="O")
    B = model.set_point(30.0, -95.0, classes=["given"], label="B")
    C = model.set_point(86.0, -28.91, label="C")
    A = model.set_point(138.0, -148.0, label="A")
    F = model.set_point(30.0, -28.0, label="F")
    E = model.set_point(30.0, -158.0, label="E")

    # Given angle at D
    D = model.set_point(233.0, -138.0, classes=["given"], label="D")
    D1 = model.set_point(301.0, -138.0, label="D1")
    D2 = model.set_point(289.0, -92.0, label="D2")
    model.set_segment(D, D1)
    model.set_segment(D, D2)
    model.set_wedge(D, D1, D1, D2)

    # Construction circle ABC
    model.construct_circle(O, B)

    # Segments
    model.set_segment(E, F)
    model.set_segment(F, B)
    model.set_segment(B, E)
    model.set_segment(B, C)
    model.set_segment(B, A)
    model.set_segment(C, A)

    # Section
    model.set_section([E, B, F])

    # Polygon
    model.set_polygon([A, B, C])

    # Angles
    model.set_wedge(B, F, F, C)
    model.set_wedge(A, B, B, C)

    return model


if __name__ == "__main__":
    construct_0077_g1()
