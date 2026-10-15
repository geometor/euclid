"""Programmatic construction for Book IX, Proposition 6 (0394.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0394_g1() -> Model:
    """Construct the figure 0394.g1 using geometor.model."""
    model = Model("0394.g1")

    # Single-letter horizontal number segments A, B, C
    A_l = model.set_point(31.0, -21.5, classes=["given"], label="A")
    A_r = model.set_point(101.0, -21.5, label="A_r")

    B_l = model.set_point(31.0, -43.5, classes=["given"], label="B")
    B_r = model.set_point(124.0, -43.5, label="B_r")

    C_l = model.set_point(31.0, -68.5, classes=["given"], label="C")
    C_r = model.set_point(158.0, -68.5, label="C_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)

    return model


if __name__ == "__main__":
    construct_0394_g1()
