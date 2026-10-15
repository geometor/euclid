"""Programmatic construction for Book III, Proposition 31 Commentary — Lardner's proof (0070.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0070_g1() -> Model:
    """Construct the figure 0070.g1 using geometor.model."""
    model = Model("0070.g1")

    # Center O (unlabeled) and points on circle ABCD (y-inverted)
    O = model.set_point(80.0, -78.0, label="O")
    A = model.set_point(28.5, -85.15, classes=["given"], label="A")
    D = model.set_point(131.5, -70.85, classes=["given"], label="D")
    B = model.set_point(65.0, -28.21, classes=["given"], label="B")
    C = model.set_point(127.5, -99.06, classes=["given"], label="C")

    # Circle ABCD
    model.construct_circle(O, A)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_segment(A, D)
    model.set_segment(C, D)

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, C, D])

    # Angles
    model.set_wedge(C, A, A, D)
    model.set_wedge(D, A, A, C)
    model.set_wedge(B, A, A, C)

    return model


if __name__ == "__main__":
    construct_0070_g1()
