"""Programmatic construction for Book VIII, Proposition 14 (0373.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0373_g1() -> Model:
    """Construct the figure 0373.g1 using geometor.model."""
    model = Model("0373.g1")

    # Single-letter horizontal number segments A, B, C, D, E
    A_l = model.set_point(25.0, -15.0, classes=["given"], label="A")
    A_r = model.set_point(62.0, -15.0, label="A_r")

    B_l = model.set_point(25.0, -39.0, classes=["given"], label="B")
    B_r = model.set_point(148.0, -39.0, label="B_r")

    C_l = model.set_point(27.0, -62.0, classes=["given"], label="C")
    C_r = model.set_point(47.0, -62.0, label="C_r")

    D_l = model.set_point(110.0, -62.0, classes=["given"], label="D")
    D_r = model.set_point(147.0, -62.0, label="D_r")

    E_l = model.set_point(61.0, -87.0, classes=["given"], label="E")
    E_r = model.set_point(125.0, -87.0, label="E_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_0373_g1()
