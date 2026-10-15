"""Programmatic construction for Book VII, Proposition 26 (0333.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0333_g1() -> Model:
    """Construct the figure 0333.g1 using geometor.model."""
    model = Model("0333.g1")

    # Single-letter horizontal number segments A, B, C, D, E, F
    A_l = model.set_point(24.0, -16.0, classes=["given"], label="A")
    A_r = model.set_point(143.0, -16.0, label="A_r")

    C_l = model.set_point(189.0, -16.0, classes=["given"], label="C")
    C_r = model.set_point(272.0, -16.0, label="C_r")

    B_l = model.set_point(24.0, -39.0, classes=["given"], label="B")
    B_r = model.set_point(123.0, -39.0, label="B_r")

    D_l = model.set_point(188.0, -39.0, classes=["given"], label="D")
    D_r = model.set_point(257.0, -39.0, label="D_r")

    E_l = model.set_point(26.0, -64.0, classes=["given"], label="E")
    E_r = model.set_point(195.0, -64.0, label="E_r")

    F_l = model.set_point(26.0, -90.0, classes=["given"], label="F")
    F_r = model.set_point(139.0, -90.0, label="F_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(C_l, C_r)
    model.set_segment(B_l, B_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)

    return model


if __name__ == "__main__":
    construct_0333_g1()
