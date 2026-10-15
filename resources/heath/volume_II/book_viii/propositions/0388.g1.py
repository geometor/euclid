"""Programmatic construction for Book VIII, Proposition 27 (0388.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0388_g1() -> Model:
    """Construct the figure 0388.g1 using geometor.model."""
    model = Model("0388.g1")

    # Single-letter horizontal number segments A, C, B, D, E, F, G, H
    A_l = model.set_point(50.0, -15.0, classes=["given"], label="A")
    A_r = model.set_point(89.0, -15.0, label="A_r")

    C_l = model.set_point(387.0, -15.0, classes=["given"], label="C")
    C_r = model.set_point(462.0, -15.0, label="C_r")

    B_l = model.set_point(51.0, -40.0, classes=["given"], label="B")
    B_r = model.set_point(341.0, -40.0, label="B_r")

    D_l = model.set_point(387.0, -40.0, classes=["given"], label="D")
    D_r = model.set_point(531.0, -40.0, label="D_r")

    E_l = model.set_point(23.0, -69.0, classes=["given"], label="E")
    E_r = model.set_point(46.0, -69.0, label="E_r")

    F_l = model.set_point(98.0, -69.0, classes=["given"], label="F")
    F_r = model.set_point(135.0, -69.0, label="F_r")

    G_l = model.set_point(202.0, -69.0, classes=["given"], label="G")
    G_r = model.set_point(275.0, -69.0, label="G_r")

    H_l = model.set_point(334.0, -69.0, classes=["given"], label="H")
    H_r = model.set_point(478.0, -69.0, label="H_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(C_l, C_r)
    model.set_segment(B_l, B_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(G_l, G_r)
    model.set_segment(H_l, H_r)

    return model


if __name__ == "__main__":
    construct_0388_g1()
