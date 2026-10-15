"""Programmatic construction for Book VII, Proposition 39 (0349.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0349_g1() -> Model:
    """Construct the figure 0349.g1 using geometor.model."""
    model = Model("0349.g1")

    # Given parts A, B, C
    A_l = model.set_point(66.0, -19.0, classes=["given"], label="A")
    A_r = model.set_point(93.0, -19.0, label="A_r")

    B_l = model.set_point(128.0, -19.0, classes=["given"], label="B")
    B_r = model.set_point(165.0, -19.0, label="B_r")

    C_l = model.set_point(210.0, -19.0, classes=["given"], label="C")
    C_r = model.set_point(260.0, -19.0, label="C_r")

    # Homonymous numbers D, E, F
    D_l = model.set_point(70.0, -43.0, classes=["given"], label="D")
    D_r = model.set_point(113.0, -43.0, label="D_r")

    E_l = model.set_point(149.0, -43.0, classes=["given"], label="E")
    E_r = model.set_point(224.0, -43.0, label="E_r")

    F_l = model.set_point(98.0, -67.0, classes=["given"], label="F")
    F_r = model.set_point(185.0, -67.0, label="F_r")

    # Least number G measured by D, E, F and lesser number H
    G_l = model.set_point(9.0, -93.0, classes=["given"], label="G")
    G_r = model.set_point(304.0, -93.0, label="G_r")

    H_l = model.set_point(45.0, -116.0, classes=["given"], label="H")
    H_r = model.set_point(255.0, -116.0, label="H_r")

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(G_l, G_r)
    model.set_segment(H_l, H_r)

    return model


if __name__ == "__main__":
    construct_0349_g1()
