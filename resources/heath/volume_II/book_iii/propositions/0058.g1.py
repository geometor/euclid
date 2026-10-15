"""Programmatic construction for Book III, Proposition 22 (0058.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0058_g1() -> Model:
    """Construct the figure 0058.g1 using geometor.model."""
    model = Model("0058.g1")

    # Center O and points A, B, C, D on circle ABCD (y-inverted)
    O = model.set_point(87, -92, label="O")
    A = model.set_point(31.69, -47.50, classes=["given"], label="A")
    B = model.set_point(142.31, -47.50, classes=["given"], label="B")
    C = model.set_point(141.08, -138.00, classes=["given"], label="C")
    D = model.set_point(85.00, -162.97, classes=["given"], label="D")

    # Circle ABCD
    model.construct_circle(O, A)

    # Sides and diagonals of cyclic quadrilateral ABCD
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)
    model.set_segment(A, C)
    model.set_segment(B, D)

    # Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, C])
    model.set_polygon([B, A, D])
    model.set_polygon([B, C, D])

    # Angles (wedges)
    model.set_wedge(A, C, C, B)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, B, B, A)
    model.set_wedge(D, B, B, C)
    model.set_wedge(D, A, A, B)
    model.set_wedge(D, A, A, C)
    model.set_wedge(A, B, B, D)
    model.set_wedge(C, D, D, B)

    return model


if __name__ == "__main__":
    construct_0058_g1()
