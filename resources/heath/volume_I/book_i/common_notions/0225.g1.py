"""Programmatic construction for Postulate 5 Commentary, Saccheri (0225.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0225_g1() -> Model:
    """Construct the figure 0225.g1 (Saccheri's quadrilateral ABDC) using geometor.model."""
    model = Model("0225.g1")

    # Points (y negated for Cartesian coordinates)
    A = model.set_point(25, -97, classes=["given"], label="A")
    B = model.set_point(135, -97, classes=["given"], label="B")
    C = model.set_point(25, -28, label="C")
    D = model.set_point(135, -28, label="D")

    # Construction lines
    model.construct_line(A, B)
    model.construct_line(A, C)
    model.construct_line(B, D)
    model.construct_line(C, D)
    model.construct_line(A, D)
    model.construct_line(B, C)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(C, D)
    model.set_segment(A, D)
    model.set_segment(B, C)

    # Polygons
    model.set_polygon([A, B, D, C])
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, C, D])
    model.set_polygon([B, D, C])

    # Angles (wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, D, D, A)
    model.set_wedge(C, A, A, D)
    model.set_wedge(D, C, C, B)

    return model


if __name__ == "__main__":
    construct_0225_g1()
