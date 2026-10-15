"""Programmatic construction for Book X, Proposition 9 (0033.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0033_g1() -> Model:
    """Construct the figure 0033.g1 using geometor.model."""
    model = Model("0033.g1")

    # Single-letter straight line segment A
    A_l = model.set_point(16.0, -24.0, classes=["given"], label="A")
    A_r = model.set_point(153.0, -24.0, label="A_r")

    # Single-letter straight line segment B
    B_l = model.set_point(191.0, -23.5, classes=["given"], label="B")
    B_r = model.set_point(291.0, -23.5, label="B_r")

    # Single-letter number segment C
    C_l = model.set_point(124.0, -43.5, classes=["given"], label="C")
    C_r = model.set_point(178.0, -43.5, label="C_r")

    # Single-letter number segment D
    D_l = model.set_point(124.0, -66.5, classes=["given"], label="D")
    D_r = model.set_point(166.0, -66.5, label="D_r")

    # Base lines
    model.construct_line(A_l, A_r)
    model.construct_line(B_l, B_r)
    model.construct_line(C_l, C_r)
    model.construct_line(D_l, D_r)

    # Magnitude and number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_0033_g1()
