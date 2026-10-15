"""Programmatic construction for Book IV, Proposition 10 Commentary (0104.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0104_g1() -> Model:
    """Construct the figure 0104.g1 (Square divided into four isosceles right triangles) using geometor.model."""
    model = Model("0104.g1")

    # Points (y-inverted for standard mathematical coordinates)
    A = model.set_point(12.00, -12.00, classes=["given"], label="A")
    B = model.set_point(82.00, -12.00, classes=["given"], label="B")
    C = model.set_point(82.00, -82.00, classes=["given"], label="C")
    D = model.set_point(12.00, -82.00, classes=["given"], label="D")
    O = model.set_point(47.00, -47.00, label="O")

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(A, O)
    model.set_segment(B, O)
    model.set_segment(C, O)
    model.set_segment(D, O)

    # Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B, O])
    model.set_polygon([B, C, O])
    model.set_polygon([C, D, O])
    model.set_polygon([D, A, O])

    return model


if __name__ == "__main__":
    construct_0104_g1()
