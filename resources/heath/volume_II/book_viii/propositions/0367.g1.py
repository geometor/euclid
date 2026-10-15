"""Programmatic construction for Book VIII, Proposition 10 (0367.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0367_g1() -> Model:
    """Construct the figure 0367.g1 using geometor.model."""
    model = Model("0367.g1")

    # Single-letter horizontal number segments C, D, E, F, G, A, B, H, K, L
    C_l = model.set_point(26.0, -16.0, classes=["given"], label="C")
    C_r = model.set_point(46.0, -16.0, label="C_r")

    D_l = model.set_point(26.0, -65.0, classes=["given"], label="D")
    D_r = model.set_point(58.0, -65.0, label="D_r")

    E_l = model.set_point(30.0, -88.0, classes=["given"], label="E")
    E_r = model.set_point(62.0, -88.0, label="E_r")

    F_l = model.set_point(26.0, -114.0, classes=["given"], label="F")
    F_r = model.set_point(57.0, -114.0, label="F_r")

    G_l = model.set_point(25.0, -139.0, classes=["given"], label="G")
    G_r = model.set_point(97.0, -139.0, label="G_r")

    A_l = model.set_point(161.0, -16.0, classes=["given"], label="A")
    A_r = model.set_point(227.0, -16.0, label="A_r")

    B_l = model.set_point(160.0, -37.0, classes=["given"], label="B")
    B_r = model.set_point(388.0, -37.0, label="B_r")

    H_l = model.set_point(180.0, -88.0, classes=["given"], label="H")
    H_r = model.set_point(243.0, -88.0, label="H_r")

    K_l = model.set_point(190.0, -112.0, classes=["given"], label="K")
    K_r = model.set_point(290.0, -112.0, label="K_r")

    L_l = model.set_point(193.0, -138.0, classes=["given"], label="L")
    L_r = model.set_point(334.0, -138.0, label="L_r")

    # Number segments
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(G_l, G_r)
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(H_l, H_r)
    model.set_segment(K_l, K_r)
    model.set_segment(L_l, L_r)

    return model


if __name__ == "__main__":
    construct_0367_g1()
