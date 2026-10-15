"""Programmatic construction for Book VII, Proposition 16 (0322.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0322_g1() -> Model:
    """Construct the figure 0322.g1 using geometor.model."""
    model = Model("0322.g1")

    # Single-letter horizontal number segments A, B, C, D, E
    A_l = model.set_point(22.0, -16.0, classes=["given"], label="A")
    A_r = model.set_point(105.0, -16.0, label="A_r")

    B_l = model.set_point(23.0, -39.0, classes=["given"], label="B")
    B_r = model.set_point(134.0, -39.0, label="B_r")

    C_l = model.set_point(22.0, -63.0, classes=["given"], label="C")
    C_r = model.set_point(256.0, -63.0, label="C_r")

    D_l = model.set_point(21.0, -85.0, classes=["given"], label="D")
    D_r = model.set_point(278.0, -85.0, label="D_r")

    E_l = model.set_point(23.0, -111.0, classes=["given"], label="E")
    E_r = model.set_point(51.0, -111.0, label="E_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_0322_g1()
