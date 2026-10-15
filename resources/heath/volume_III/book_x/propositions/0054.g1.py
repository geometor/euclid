"""Programmatic construction for Book X, Proposition 21 (0054.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0054_g1() -> Model:
    """Construct the figure 0054.g1 using geometor.model."""
    model = Model("0054.g1")

    # Vertices of square AD (A, B, D, D_r) and rectangle AC (A, B, C, C_r)
    D = model.set_point(22.0, -13.5, label="D")
    B = model.set_point(22.0, -67.5, classes=["given"], label="B")
    C = model.set_point(22.0, -147.0, classes=["given"], label="C")
    A = model.set_point(75.5, -67.5, classes=["given"], label="A")
    D_r = model.set_point(75.5, -13.5, label="D_r")
    C_r = model.set_point(75.5, -147.0, label="C_r")

    # Base lines
    model.construct_line(D, C)
    model.construct_line(D_r, C_r)
    model.construct_line(D, D_r)
    model.construct_line(B, A)
    model.construct_line(C, C_r)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(D, B)
    model.set_segment(D, C)
    model.set_segment(D, D_r)
    model.set_segment(C, C_r)
    model.set_segment(D_r, A)
    model.set_segment(A, C_r)
    model.set_segment(D_r, C_r)

    # Collinear section on DC
    model.set_section([D, B, C])

    # Polygons: square AD and rectangle AC
    model.set_polygon([A, B, D, D_r])
    model.set_polygon([A, B, C, C_r])
    model.set_polygon([D, C, C_r, D_r])

    return model


if __name__ == "__main__":
    construct_0054_g1()
