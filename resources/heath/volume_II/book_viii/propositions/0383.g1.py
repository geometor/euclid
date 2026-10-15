"""Programmatic construction for Book VIII, Proposition 21 (0383.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0383_g1() -> Model:
    """Construct the figure 0383.g1 using geometor.model."""
    model = Model("0383.g1")

    # Single-letter horizontal number segments A, B, C, D, N, O, E, F, G, H, K, L, M
    A_l = model.set_point(26.0, -14.0, classes=["given"], label="A")
    A_r = model.set_point(60.0, -14.0, label="A_r")

    B_l = model.set_point(24.0, -36.0, classes=["given"], label="B")
    B_r = model.set_point(309.0, -36.0, label="B_r")

    C_l = model.set_point(24.0, -57.0, classes=["given"], label="C")
    C_r = model.set_point(99.0, -57.0, label="C_r")

    D_l = model.set_point(24.0, -80.0, classes=["given"], label="D")
    D_r = model.set_point(173.0, -80.0, label="D_r")

    N_l = model.set_point(76.0, -102.0, classes=["given"], label="N")
    N_r = model.set_point(96.0, -102.0, label="N_r")

    O_l = model.set_point(76.0, -122.0, classes=["given"], label="O")
    O_r = model.set_point(112.0, -122.0, label="O_r")

    E_l = model.set_point(355.0, -14.0, classes=["given"], label="E")
    E_r = model.set_point(374.0, -14.0, label="E_r")

    F_l = model.set_point(355.0, -35.0, classes=["given"], label="F")
    F_r = model.set_point(380.0, -35.0, label="F_r")

    G_l = model.set_point(358.0, -56.0, classes=["given"], label="G")
    G_r = model.set_point(405.0, -56.0, label="G_r")

    H_l = model.set_point(358.0, -79.0, classes=["given"], label="H")
    H_r = model.set_point(372.0, -79.0, label="H_r")

    K_l = model.set_point(358.0, -99.0, classes=["given"], label="K")
    K_r = model.set_point(375.0, -99.0, label="K_r")

    L_l = model.set_point(358.0, -119.0, classes=["given"], label="L")
    L_r = model.set_point(376.0, -119.0, label="L_r")

    M_l = model.set_point(357.0, -140.0, classes=["given"], label="M")
    M_r = model.set_point(384.0, -140.0, label="M_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(N_l, N_r)
    model.set_segment(O_l, O_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(G_l, G_r)
    model.set_segment(H_l, H_r)
    model.set_segment(K_l, K_r)
    model.set_segment(L_l, L_r)
    model.set_segment(M_l, M_r)

    return model


if __name__ == "__main__":
    construct_0383_g1()
