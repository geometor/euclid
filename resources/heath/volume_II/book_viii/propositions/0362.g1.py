"""Programmatic construction for Book VIII, Proposition 7 (0362.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0362_g1() -> Model:
    """Construct the figure 0362.g1 using geometor.model."""
    model = Model("0362.g1")

    # Single-letter horizontal number segments A, B, C, D
    A_l = model.set_point(31.0, -15.0, classes=["given"], label="A")
    A_r = model.set_point(65.0, -15.0, label="A_r")

    B_l = model.set_point(28.0, -41.0, classes=["given"], label="B")
    B_r = model.set_point(90.0, -41.0, label="B_r")

    C_l = model.set_point(28.0, -67.0, classes=["given"], label="C")
    C_r = model.set_point(154.0, -67.0, label="C_r")

    D_l = model.set_point(24.0, -93.0, classes=["given"], label="D")
    D_r = model.set_point(275.0, -93.0, label="D_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_0362_g1()
