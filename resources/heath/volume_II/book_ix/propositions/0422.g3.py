"""Programmatic construction for Book IX, Proposition 29 (0422.g3)."""

from __future__ import annotations

from geometor.model import Model


def construct_0422_g3() -> Model:
    """Construct the figure 0422.g3 using geometor.model."""
    model = Model("0422.g3")

    # Single-letter horizontal number segments A, B, C
    A_l = model.set_point(32.0, -16.5, classes=["given"], label="A")
    A_r = model.set_point(58.0, -16.5, label="A_r")

    B_l = model.set_point(31.0, -38.5, classes=["given"], label="B")
    B_r = model.set_point(88.0, -38.5, label="B_r")

    C_l = model.set_point(33.0, -62.0, classes=["given"], label="C")
    C_r = model.set_point(195.0, -62.0, label="C_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)

    return model


if __name__ == "__main__":
    construct_0422_g3()
