"""Programmatic construction for Book X, Proposition 24 (0059.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0059_g1() -> Model:
    """Construct the figure 0059.g1 using geometor.model."""
    model = Model("0059.g1")

    # Vertices of rectangle AC (A, B, C, C_l) and square AD (A, B, D, D_l)
    A = model.set_point(25.0, -97.5, classes=["given"], label="A")
    B = model.set_point(89.0, -97.5, classes=["given"], label="B")
    C = model.set_point(89.0, -14.5, classes=["given"], label="C")
    D = model.set_point(89.0, -160.5, label="D")
    C_l = model.set_point(25.0, -14.5, label="C_l")
    D_l = model.set_point(25.0, -160.5, label="D_l")

    # Base lines
    model.construct_line(C_l, D_l)
    model.construct_line(C, D)
    model.construct_line(C_l, C)
    model.construct_line(A, B)
    model.construct_line(D_l, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(C, D)
    model.set_segment(C_l, C)
    model.set_segment(D_l, D)
    model.set_segment(C_l, D_l)

    # Collinear section on CD
    model.set_section([C, B, D])

    # Polygons: rectangle AC and square AD
    model.set_polygon([A, B, C, C_l])
    model.set_polygon([A, B, D, D_l])
    model.set_polygon([C_l, C, D, D_l])

    return model


if __name__ == "__main__":
    construct_0059_g1()
