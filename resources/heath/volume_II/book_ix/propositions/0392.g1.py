"""Programmatic construction for Book IX, Proposition 3 (0392.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0392_g1() -> Model:
    """Construct the figure 0392.g1 using geometor.model."""
    model = Model("0392.g1")

    # Single-letter horizontal number segments A, B, C, D
    A_l = model.set_point(30.0, -22.5, classes=["given"], label="A")
    A_r = model.set_point(62.0, -22.5, label="A_r")

    B_l = model.set_point(33.0, -44.5, classes=["given"], label="B")
    B_r = model.set_point(129.0, -44.5, label="B_r")

    C_l = model.set_point(33.0, -72.5, classes=["given"], label="C")
    C_r = model.set_point(53.0, -72.5, label="C_r")

    D_l = model.set_point(122.0, -72.5, classes=["given"], label="D")
    D_r = model.set_point(141.0, -72.5, label="D_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_0392_g1()
