"""Programmatic construction for Book X, Proposition 15 (0043.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0043_g1() -> Model:
    """Construct the figure 0043.g1 using geometor.model."""
    model = Model("0043.g1")

    # Collinear points A, B, C on horizontal line AC
    A = model.set_point(16.0, -25.5, classes=["given"], label="A")
    B = model.set_point(149.0, -25.5, classes=["given"], label="B")
    C = model.set_point(249.0, -25.5, classes=["given"], label="C")

    # Common measure magnitude D
    D_l = model.set_point(19.0, -63.5, label="D")
    D_r = model.set_point(70.0, -63.5, label="D_r")

    # Base lines
    model.construct_line(A, C)
    model.construct_line(D_l, D_r)

    # Whole and subdivided segments on AC
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_section([A, B, C])

    # Magnitude segment D
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_0043_g1()
