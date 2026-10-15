"""Programmatic construction for Book IX, Proposition 18 (0414.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0414_g1() -> Model:
    """Construct the figure 0414.g1 using geometor.model."""
    model = Model("0414.g1")

    # Left column: single-letter horizontal number segments A, B
    A_l = model.set_point(27.0, -20.0, classes=["given"], label="A")
    A_r = model.set_point(76.0, -20.0, label="A_r")

    B_l = model.set_point(28.0, -47.5, classes=["given"], label="B")
    B_r = model.set_point(92.0, -47.5, label="B_r")

    # Right column: single-letter horizontal number segments D, C
    D_l = model.set_point(179.0, -25.5, classes=["given"], label="D")
    D_r = model.set_point(261.0, -25.5, label="D_r")

    C_l = model.set_point(145.0, -54.0, classes=["given"], label="C")
    C_r = model.set_point(390.0, -54.0, label="C_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(D_l, D_r)
    model.set_segment(C_l, C_r)

    return model


if __name__ == "__main__":
    construct_0414_g1()
