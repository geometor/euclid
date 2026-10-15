"""Programmatic construction for Book VIII, Proposition 26 (0387.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0387_g2() -> Model:
    """Construct the figure 0387.g2 using geometor.model."""
    model = Model("0387.g2")

    # Single-letter horizontal number segments A, B, C, D, E, F
    A_l = model.set_point(25.0, -14.0, classes=["given"], label="A")
    A_r = model.set_point(95.0, -14.0, label="A_r")

    B_l = model.set_point(144.0, -14.0, classes=["given"], label="B")
    B_r = model.set_point(431.0, -14.0, label="B_r")

    C_l = model.set_point(112.0, -44.0, classes=["given"], label="C")
    C_r = model.set_point(253.0, -44.0, label="C_r")

    D_l = model.set_point(19.0, -68.0, classes=["given"], label="D")
    D_r = model.set_point(58.0, -68.0, label="D_r")

    E_l = model.set_point(114.0, -68.0, classes=["given"], label="E")
    E_r = model.set_point(181.0, -68.0, label="E_r")

    F_l = model.set_point(243.0, -68.0, classes=["given"], label="F")
    F_r = model.set_point(388.0, -68.0, label="F_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)

    return model


if __name__ == "__main__":
    construct_0387_g2()
