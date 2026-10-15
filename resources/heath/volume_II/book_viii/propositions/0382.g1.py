"""Programmatic construction for Book VIII, Proposition 20 (0382.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0382_g1() -> Model:
    """Construct the figure 0382.g1 using geometor.model."""
    model = Model("0382.g1")

    # Single-letter horizontal number segments A, B, C, F, G, D, E
    A_l = model.set_point(20.0, -15.0, classes=["given"], label="A")
    A_r = model.set_point(95.0, -15.0, label="A_r")

    B_l = model.set_point(24.0, -42.0, classes=["given"], label="B")
    B_r = model.set_point(311.0, -42.0, label="B_r")

    C_l = model.set_point(22.0, -63.0, classes=["given"], label="C")
    C_r = model.set_point(164.0, -63.0, label="C_r")

    F_l = model.set_point(91.0, -87.0, classes=["given"], label="F")
    F_r = model.set_point(129.0, -87.0, label="F_r")

    G_l = model.set_point(92.0, -107.0, classes=["given"], label="G")
    G_r = model.set_point(164.0, -107.0, label="G_r")

    D_l = model.set_point(352.0, -15.0, classes=["given"], label="D")
    D_r = model.set_point(388.0, -15.0, label="D_r")

    E_l = model.set_point(351.0, -42.0, classes=["given"], label="E")
    E_r = model.set_point(423.0, -42.0, label="E_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(F_l, F_r)
    model.set_segment(G_l, G_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_0382_g1()
