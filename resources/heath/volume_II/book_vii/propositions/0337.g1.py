"""Programmatic construction for Book VII, Proposition 30 (0337.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0337_g1() -> Model:
    """Construct the figure 0337.g1 using geometor.model."""
    model = Model("0337.g1")

    # Single-letter horizontal number segments A, B, C, D, E
    A_l = model.set_point(22.0, -13.0, classes=["given"], label="A")
    A_r = model.set_point(122.0, -13.0, label="A_r")

    B_l = model.set_point(24.0, -36.0, classes=["given"], label="B")
    B_r = model.set_point(140.0, -36.0, label="B_r")

    C_l = model.set_point(23.0, -59.0, classes=["given"], label="C")
    C_r = model.set_point(173.0, -59.0, label="C_r")

    D_l = model.set_point(24.0, -86.0, classes=["given"], label="D")
    D_r = model.set_point(57.0, -86.0, label="D_r")

    E_l = model.set_point(25.0, -107.0, classes=["given"], label="E")
    E_r = model.set_point(153.0, -107.0, label="E_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_0337_g1()
