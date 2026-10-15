"""Programmatic construction for Book VIII, Proposition 11 (0369.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0369_g1() -> Model:
    """Construct the figure 0369.g1 using geometor.model."""
    model = Model("0369.g1")

    # Single-letter horizontal number segments A, B, C, D, E
    A_l = model.set_point(26.0, -15.0, classes=["given"], label="A")
    A_r = model.set_point(89.0, -15.0, label="A_r")

    B_l = model.set_point(23.0, -41.0, classes=["given"], label="B")
    B_r = model.set_point(165.0, -41.0, label="B_r")

    C_l = model.set_point(24.0, -65.0, classes=["given"], label="C")
    C_r = model.set_point(58.0, -65.0, label="C_r")

    D_l = model.set_point(130.0, -65.0, classes=["given"], label="D")
    D_r = model.set_point(176.0, -65.0, label="D_r")

    E_l = model.set_point(24.0, -91.0, classes=["given"], label="E")
    E_r = model.set_point(118.0, -91.0, label="E_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_0369_g1()
