"""Programmatic construction for Book IX, Proposition 12 (0403.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0403_g1() -> Model:
    """Construct the figure 0403.g1 using geometor.model."""
    model = Model("0403.g1")

    # Left column: single-letter horizontal number segments A, B, C, D, E
    A_l = model.set_point(33.0, -23.0, classes=["given"], label="A")
    A_r = model.set_point(69.0, -23.0, label="A_r")

    B_l = model.set_point(31.0, -44.5, classes=["given"], label="B")
    B_r = model.set_point(88.0, -44.5, label="B_r")

    C_l = model.set_point(33.0, -62.5, classes=["given"], label="C")
    C_r = model.set_point(109.0, -62.5, label="C_r")

    D_l = model.set_point(32.0, -84.5, classes=["given"], label="D")
    D_r = model.set_point(157.0, -84.5, label="D_r")

    E_l = model.set_point(31.0, -104.5, classes=["given"], label="E")
    E_r = model.set_point(53.0, -104.5, label="E_r")

    # Right column: single-letter horizontal number segments F, G, H
    F_l = model.set_point(196.0, -23.5, classes=["given"], label="F")
    F_r = model.set_point(350.0, -23.5, label="F_r")

    G_l = model.set_point(196.0, -45.5, classes=["given"], label="G")
    G_r = model.set_point(306.0, -45.5, label="G_r")

    H_l = model.set_point(196.0, -68.5, classes=["given"], label="H")
    H_r = model.set_point(270.0, -68.5, label="H_r")

    # Number segments
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
    construct_0403_g1()
