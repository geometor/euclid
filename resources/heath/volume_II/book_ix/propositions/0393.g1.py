"""Programmatic construction for Book IX, Proposition 4 (0393.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0393_g1() -> Model:
    """Construct the figure 0393.g1 using geometor.model."""
    model = Model("0393.g1")

    # Single-letter horizontal number segments A, B, C, D
    A_l = model.set_point(32.0, -22.5, classes=["given"], label="A")
    A_r = model.set_point(124.0, -22.5, label="A_r")

    B_l = model.set_point(31.0, -46.0, classes=["given"], label="B")
    B_r = model.set_point(156.0, -46.0, label="B_r")

    C_l = model.set_point(30.0, -67.0, classes=["given"], label="C")
    C_r = model.set_point(268.0, -67.0, label="C_r")

    D_l = model.set_point(30.0, -86.5, classes=["given"], label="D")
    D_r = model.set_point(181.0, -86.5, label="D_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_0393_g1()
