"""Programmatic construction for Book IV, Proposition 1 (0086.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0086_g1() -> Model:
    """Construct the figure 0086.g1 using geometor.model."""
    model = Model("0086.g1")

    # Points (y-inverted for standard mathematical coordinates)
    O = model.set_point(93.0, -95.0, label="O")
    B = model.set_point(25.0, -95.0, classes=["given"], label="B")
    C = model.set_point(161.0, -95.0, classes=["given"], label="C")
    E = model.set_point(105.0, -95.0, label="E")
    A = model.set_point(137.94, -43.97, label="A")
    F = model.set_point(137.94, -146.03, label="F")

    # Standalone segment D endpoints
    D1 = model.set_point(202.0, -30.0, classes=["given"], label="D1")
    D2 = model.set_point(258.0, -30.0, classes=["given"], label="D2")

    # Circles
    model.construct_circle(O, B)
    model.construct_circle(C, E)

    # Construction lines
    model.construct_line(B, C)

    # Segments
    model.set_segment(B, C)
    model.set_segment(B, E)
    model.set_segment(C, E)
    model.set_segment(C, A)
    model.set_segment(D1, D2)

    # Collinear section
    model.set_section([B, E, C])

    return model


if __name__ == "__main__":
    construct_0086_g1()
