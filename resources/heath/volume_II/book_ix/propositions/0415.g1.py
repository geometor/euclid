"""Programmatic construction for Book IX, Proposition 19 (0415.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0415_g1() -> Model:
    """Construct the figure 0415.g1 using geometor.model."""
    model = Model("0415.g1")

    # Single-letter horizontal number segments A, B, C, D, E
    A_l = model.set_point(29.0, -21.5, classes=["given"], label="A")
    A_r = model.set_point(88.0, -21.5, label="A_r")

    B_l = model.set_point(30.0, -46.5, classes=["given"], label="B")
    B_r = model.set_point(100.0, -46.5, label="B_r")

    C_l = model.set_point(30.0, -70.5, classes=["given"], label="C")
    C_r = model.set_point(136.0, -70.5, label="C_r")

    D_l = model.set_point(31.0, -89.5, classes=["given"], label="D")
    D_r = model.set_point(156.0, -89.5, label="D_r")

    E_l = model.set_point(30.0, -115.0, classes=["given"], label="E")
    E_r = model.set_point(216.0, -115.0, label="E_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_0415_g1()
