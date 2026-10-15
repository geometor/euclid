"""Programmatic construction for Book VIII, Proposition 23 (0385.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0385_g2() -> Model:
    """Construct the figure 0385.g2 using geometor.model."""
    model = Model("0385.g2")

    # Single-letter horizontal number segments A, B, C, D
    A_l = model.set_point(19.0, -14.0, classes=["given"], label="A")
    A_r = model.set_point(86.0, -14.0, label="A_r")

    B_l = model.set_point(21.0, -34.0, classes=["given"], label="B")
    B_r = model.set_point(120.0, -34.0, label="B_r")

    C_l = model.set_point(22.0, -54.0, classes=["given"], label="C")
    C_r = model.set_point(162.0, -54.0, label="C_r")

    D_l = model.set_point(23.0, -75.0, classes=["given"], label="D")
    D_r = model.set_point(230.0, -75.0, label="D_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_0385_g2()
