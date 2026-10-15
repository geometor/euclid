"""Programmatic construction for Book X, Proposition 10 (0036.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0036_g1() -> Model:
    """Construct the figure 0036.g1 using geometor.model."""
    model = Model("0036.g1")

    # Single-letter straight line segment A
    A_l = model.set_point(28.0, -20.0, classes=["given"], label="A")
    A_r = model.set_point(113.0, -20.0, label="A_r")

    # Single-letter straight line segment D
    D_l = model.set_point(28.0, -47.0, label="D")
    D_r = model.set_point(132.0, -47.0, label="D_r")

    # Single-letter straight line segment E
    E_l = model.set_point(29.0, -66.0, label="E")
    E_r = model.set_point(124.0, -66.0, label="E_r")

    # Single-letter number segment B
    B_l = model.set_point(31.0, -88.5, classes=["given"], label="B")
    B_r = model.set_point(83.0, -88.5, label="B_r")

    # Single-letter number segment C
    C_l = model.set_point(30.0, -109.5, classes=["given"], label="C")
    C_r = model.set_point(111.0, -109.5, label="C_r")

    # Base lines
    model.construct_line(A_l, A_r)
    model.construct_line(D_l, D_r)
    model.construct_line(E_l, E_r)
    model.construct_line(B_l, B_r)
    model.construct_line(C_l, C_r)

    # Magnitude and number segments
    model.set_segment(A_l, A_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)

    return model


if __name__ == "__main__":
    construct_0036_g1()
