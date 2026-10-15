"""Programmatic construction for Book VIII, Proposition 2 (0352.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0352_g1() -> Model:
    """Construct the figure 0352.g1 using geometor.model."""
    model = Model("0352.g1")

    # Single-letter horizontal number segments A, B, C, D, E, F, G, H, K
    A_l = model.set_point(29.0, -15.0, classes=["given"], label="A")
    A_r = model.set_point(71.0, -15.0, label="A_r")

    C_l = model.set_point(120.0, -15.0, classes=["given"], label="C")
    C_r = model.set_point(180.0, -15.0, label="C_r")

    B_l = model.set_point(27.0, -45.0, classes=["given"], label="B")
    B_r = model.set_point(81.0, -45.0, label="B_r")

    D_l = model.set_point(120.0, -45.0, classes=["given"], label="D")
    D_r = model.set_point(202.0, -45.0, label="D_r")

    E_l = model.set_point(48.0, -72.0, classes=["given"], label="E")
    E_r = model.set_point(161.0, -72.0, label="E_r")

    F_l = model.set_point(38.0, -100.0, classes=["given"], label="F")
    F_r = model.set_point(140.0, -100.0, label="F_r")

    G_l = model.set_point(178.0, -100.0, classes=["given"], label="G")
    G_r = model.set_point(304.0, -100.0, label="G_r")

    H_l = model.set_point(55.0, -126.0, classes=["given"], label="H")
    H_r = model.set_point(240.0, -126.0, label="H_r")

    K_l = model.set_point(64.0, -154.0, classes=["given"], label="K")
    K_r = model.set_point(224.0, -154.0, label="K_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(G_l, G_r)
    model.set_segment(H_l, H_r)
    model.set_segment(K_l, K_r)

    return model


if __name__ == "__main__":
    construct_0352_g1()
