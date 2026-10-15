"""Programmatic construction for Book VIII, Proposition 15 (0375.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0375_g1() -> Model:
    """Construct the figure 0375.g1 using geometor.model."""
    model = Model("0375.g1")

    # Single-letter horizontal number segments A, B, C, D, E, G, F, H, K
    A_l = model.set_point(26.0, -16.0, classes=["given"], label="A")
    A_r = model.set_point(61.0, -16.0, label="A_r")

    B_l = model.set_point(28.0, -40.0, classes=["given"], label="B")
    B_r = model.set_point(282.0, -40.0, label="B_r")

    C_l = model.set_point(26.0, -63.0, classes=["given"], label="C")
    C_r = model.set_point(48.0, -63.0, label="C_r")

    D_l = model.set_point(22.0, -88.0, classes=["given"], label="D")
    D_r = model.set_point(47.0, -88.0, label="D_r")

    E_l = model.set_point(31.0, -110.0, classes=["given"], label="E")
    E_r = model.set_point(51.0, -110.0, label="E_r")

    G_l = model.set_point(28.0, -133.0, classes=["given"], label="G")
    G_r = model.set_point(97.0, -133.0, label="G_r")

    F_l = model.set_point(29.0, -158.0, classes=["given"], label="F")
    F_r = model.set_point(65.0, -158.0, label="F_r")

    H_l = model.set_point(227.0, -64.0, classes=["given"], label="H")
    H_r = model.set_point(297.0, -64.0, label="H_r")

    K_l = model.set_point(228.0, -88.0, classes=["given"], label="K")
    K_r = model.set_point(361.0, -88.0, label="K_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(G_l, G_r)
    model.set_segment(F_l, F_r)
    model.set_segment(H_l, H_r)
    model.set_segment(K_l, K_r)

    return model


if __name__ == "__main__":
    construct_0375_g1()
