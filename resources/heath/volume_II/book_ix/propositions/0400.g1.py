"""Programmatic construction for Book IX, Proposition 10 (0400.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0400_g1() -> Model:
    """Construct the figure 0400.g1 using geometor.model."""
    model = Model("0400.g1")

    # Single-letter horizontal number segments A, B, C, D, E, F
    A_l = model.set_point(31.0, -19.5, classes=["given"], label="A")
    A_r = model.set_point(69.0, -19.5, label="A_r")

    B_l = model.set_point(30.0, -43.5, classes=["given"], label="B")
    B_r = model.set_point(86.0, -43.5, label="B_r")

    C_l = model.set_point(30.0, -67.5, classes=["given"], label="C")
    C_r = model.set_point(108.0, -67.5, label="C_r")

    D_l = model.set_point(32.0, -89.5, classes=["given"], label="D")
    D_r = model.set_point(134.0, -89.5, label="D_r")

    E_l = model.set_point(32.0, -111.0, classes=["given"], label="E")
    E_r = model.set_point(166.0, -111.0, label="E_r")

    F_l = model.set_point(32.0, -134.0, classes=["given"], label="F")
    F_r = model.set_point(205.0, -134.0, label="F_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)

    return model


if __name__ == "__main__":
    construct_0400_g1()
