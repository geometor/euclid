"""Programmatic construction for Book X, Proposition 27 (0064.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0064_g1() -> Model:
    """Construct the figure 0064.g1 using geometor.model."""
    model = Model("0064.g1")

    # Rational straight lines A, B and medial straight lines C, D
    A_t = model.set_point(24.0, -15.0, classes=["given"], label="A")
    A_b = model.set_point(24.0, -166.0, classes=["given"], label="A_b")

    B_t = model.set_point(50.5, -50.0, classes=["given"], label="B")
    B_b = model.set_point(50.5, -166.0, classes=["given"], label="B_b")

    C_t = model.set_point(95.5, -15.0, label="C")
    C_b = model.set_point(95.5, -116.0, label="C_b")

    D_t = model.set_point(120.5, -15.0, label="D")
    D_b = model.set_point(120.5, -89.0, label="D_b")

    # Base lines
    model.construct_line(A_t, A_b)
    model.construct_line(B_t, B_b)
    model.construct_line(C_t, C_b)
    model.construct_line(D_t, D_b)

    # Segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)
    model.set_segment(D_t, D_b)

    return model


if __name__ == "__main__":
    construct_0064_g1()
