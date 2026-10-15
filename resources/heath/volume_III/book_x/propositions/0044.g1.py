"""Programmatic construction for Book X, Proposition 16 (0044.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0044_g1() -> Model:
    """Construct the figure 0044.g1 using geometor.model."""
    model = Model("0044.g1")

    # Collinear points A, B, C on vertical line AC
    A = model.set_point(24.5, -14.0, classes=["given"], label="A")
    B = model.set_point(24.5, -123.0, classes=["given"], label="B")
    C = model.set_point(24.5, -195.0, classes=["given"], label="C")

    # Common measure magnitude D
    D_t = model.set_point(64.5, -15.0, label="D")
    D_b = model.set_point(64.5, -56.0, label="D_b")

    # Base lines
    model.construct_line(A, C)
    model.construct_line(D_t, D_b)

    # Whole and subdivided segments on AC
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_section([A, B, C])

    # Magnitude segment D
    model.set_segment(D_t, D_b)

    return model


if __name__ == "__main__":
    construct_0044_g1()
