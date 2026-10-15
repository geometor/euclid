"""Programmatic construction for Book X, Proposition 11 (0037.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0037_g1() -> Model:
    """Construct the figure 0037.g1 using geometor.model."""
    model = Model("0037.g1")

    # Four proportional magnitude segments A, B, C, D
    A_l = model.set_point(29.0, -18.5, classes=["given"], label="A")
    A_r = model.set_point(158.0, -18.5, label="A_r")

    B_l = model.set_point(203.0, -19.5, classes=["given"], label="B")
    B_r = model.set_point(274.0, -19.5, label="B_r")

    C_l = model.set_point(33.0, -38.5, classes=["given"], label="C")
    C_r = model.set_point(129.0, -38.5, label="C_r")

    D_l = model.set_point(208.0, -39.5, classes=["given"], label="D")
    D_r = model.set_point(258.0, -39.5, label="D_r")

    # Base lines
    model.construct_line(A_l, A_r)
    model.construct_line(B_l, B_r)
    model.construct_line(C_l, C_r)
    model.construct_line(D_l, D_r)

    # Magnitude segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_0037_g1()
