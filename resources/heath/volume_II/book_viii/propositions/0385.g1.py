"""Programmatic construction for Book VIII, Proposition 22 (0385.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0385_g1() -> Model:
    """Construct the figure 0385.g1 using geometor.model."""
    model = Model("0385.g1")

    # Single-letter horizontal number segments A, B, C
    A_l = model.set_point(21.0, -14.0, classes=["given"], label="A")
    A_r = model.set_point(83.0, -14.0, label="A_r")

    B_l = model.set_point(22.0, -36.0, classes=["given"], label="B")
    B_r = model.set_point(116.0, -36.0, label="B_r")

    C_l = model.set_point(23.0, -62.0, classes=["given"], label="C")
    C_r = model.set_point(162.0, -62.0, label="C_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)

    return model


if __name__ == "__main__":
    construct_0385_g1()
