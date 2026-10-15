"""Programmatic construction for Book IX, Proposition 5 (0393.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0393_g2() -> Model:
    """Construct the figure 0393.g2 using geometor.model."""
    model = Model("0393.g2")

    # Single-letter horizontal number segments A, B, C, D
    A_l = model.set_point(27.0, -21.0, classes=["given"], label="A")
    A_r = model.set_point(128.0, -21.0, label="A_r")

    B_l = model.set_point(27.0, -45.5, classes=["given"], label="B")
    B_r = model.set_point(153.0, -45.5, label="B_r")

    C_l = model.set_point(26.0, -68.0, classes=["given"], label="C")
    C_r = model.set_point(272.0, -68.0, label="C_r")

    D_l = model.set_point(28.0, -89.0, classes=["given"], label="D")
    D_r = model.set_point(182.0, -89.0, label="D_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_0393_g2()
