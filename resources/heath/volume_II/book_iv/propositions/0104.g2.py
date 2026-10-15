"""Programmatic construction for Book IV, Proposition 10 Commentary (0104.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0104_g2() -> Model:
    """Construct the figure 0104.g2 (Equilateral triangle divided into six scalene right triangles) using geometor.model."""
    model = Model("0104.g2")

    # Points (y-inverted for standard mathematical coordinates)
    A = model.set_point(65.00, -18.86, classes=["given"], label="A")
    B = model.set_point(17.00, -102.00, classes=["given"], label="B")
    C = model.set_point(113.00, -102.00, classes=["given"], label="C")
    D = model.set_point(65.00, -102.00, label="D")
    E = model.set_point(89.00, -60.43, label="E")
    F = model.set_point(41.00, -60.43, label="F")
    O = model.set_point(65.00, -74.29, label="O")

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_segment(A, D)
    model.set_segment(B, E)
    model.set_segment(C, F)

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, F, O])
    model.set_polygon([B, F, O])
    model.set_polygon([B, D, O])
    model.set_polygon([C, D, O])
    model.set_polygon([C, E, O])
    model.set_polygon([A, E, O])

    return model


if __name__ == "__main__":
    construct_0104_g2()
