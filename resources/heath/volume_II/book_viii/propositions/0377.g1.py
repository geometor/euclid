"""Programmatic construction for Book VIII, Proposition 18 (0377.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0377_g1() -> Model:
    """Construct the figure 0377.g1 using geometor.model."""
    model = Model("0377.g1")

    # Single-letter horizontal number segments A, B, G, C, D, E, F
    A_l = model.set_point(22.0, -16.0, classes=["given"], label="A")
    A_r = model.set_point(92.0, -16.0, label="A_r")

    B_l = model.set_point(22.0, -41.0, classes=["given"], label="B")
    B_r = model.set_point(308.0, -41.0, label="B_r")

    G_l = model.set_point(25.0, -77.0, classes=["given"], label="G")
    G_r = model.set_point(165.0, -77.0, label="G_r")

    C_l = model.set_point(361.0, -15.0, classes=["given"], label="C")
    C_r = model.set_point(388.0, -15.0, label="C_r")

    D_l = model.set_point(361.0, -39.0, classes=["given"], label="D")
    D_r = model.set_point(399.0, -39.0, label="D_r")

    E_l = model.set_point(329.0, -63.0, classes=["given"], label="E")
    E_r = model.set_point(379.0, -63.0, label="E_r")

    F_l = model.set_point(330.0, -85.0, classes=["given"], label="F")
    F_r = model.set_point(406.0, -85.0, label="F_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(G_l, G_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)

    return model


if __name__ == "__main__":
    construct_0377_g1()
