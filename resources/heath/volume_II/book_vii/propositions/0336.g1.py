"""Programmatic construction for Book VII, Proposition 29 (0336.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0336_g1() -> Model:
    """Construct the figure 0336.g1 using geometor.model."""
    model = Model("0336.g1")

    # Single-letter horizontal number segments A, B, C
    A_l = model.set_point(16.0, -15.0, classes=["given"], label="A")
    A_r = model.set_point(113.0, -15.0, label="A_r")

    B_l = model.set_point(14.0, -39.0, classes=["given"], label="B")
    B_r = model.set_point(158.0, -39.0, label="B_r")

    C_l = model.set_point(13.0, -61.0, classes=["given"], label="C")
    C_r = model.set_point(63.0, -61.0, label="C_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)

    return model


if __name__ == "__main__":
    construct_0336_g1()
