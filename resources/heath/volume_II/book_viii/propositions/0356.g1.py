"""Programmatic construction for Book VIII, Proposition 4, Diagram 1 (0356.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0356_g1() -> Model:
    """Construct the figure 0356.g1 using geometor.model."""
    model = Model("0356.g1")

    # Single-letter horizontal number segments A, B, C, D, E, F, G, H, K, L, M, N, O, P
    A_l = model.set_point(42.0, -14.0, classes=["given"], label="A")
    A_r = model.set_point(63.0, -14.0, label="A_r")

    B_l = model.set_point(201.0, -15.0, classes=["given"], label="B")
    B_r = model.set_point(239.0, -15.0, label="B_r")

    C_l = model.set_point(45.0, -36.0, classes=["given"], label="C")
    C_r = model.set_point(70.0, -36.0, label="C_r")

    D_l = model.set_point(196.0, -36.0, classes=["given"], label="D")
    D_r = model.set_point(232.0, -36.0, label="D_r")

    E_l = model.set_point(46.0, -60.0, classes=["given"], label="E")
    E_r = model.set_point(84.0, -60.0, label="E_r")

    F_l = model.set_point(200.0, -61.0, classes=["given"], label="F")
    F_r = model.set_point(248.0, -61.0, label="F_r")

    N_l = model.set_point(45.0, -85.0, classes=["given"], label="N")
    N_r = model.set_point(74.0, -85.0, label="N_r")

    G_l = model.set_point(200.0, -86.0, classes=["given"], label="G")
    G_r = model.set_point(350.0, -86.0, label="G_r")

    O_l = model.set_point(46.0, -111.0, classes=["given"], label="O")
    O_r = model.set_point(117.0, -111.0, label="O_r")

    H_l = model.set_point(199.0, -112.0, classes=["given"], label="H")
    H_r = model.set_point(247.0, -112.0, label="H_r")

    M_l = model.set_point(24.0, -142.0, classes=["given"], label="M")
    M_r = model.set_point(149.0, -142.0, label="M_r")

    K_l = model.set_point(197.0, -143.0, classes=["given"], label="K")
    K_r = model.set_point(435.0, -143.0, label="K_r")

    P_l = model.set_point(26.0, -168.0, classes=["given"], label="P")
    P_r = model.set_point(164.0, -168.0, label="P_r")

    L_l = model.set_point(198.0, -169.0, classes=["given"], label="L")
    L_r = model.set_point(465.0, -169.0, label="L_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(N_l, N_r)
    model.set_segment(G_l, G_r)
    model.set_segment(O_l, O_r)
    model.set_segment(H_l, H_r)
    model.set_segment(M_l, M_r)
    model.set_segment(K_l, K_r)
    model.set_segment(P_l, P_r)
    model.set_segment(L_l, L_r)

    return model


if __name__ == "__main__":
    construct_0356_g1()
