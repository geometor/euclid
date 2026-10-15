"""Programmatic construction for Book VIII, Proposition 4, Diagram 2 (0357.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0357_g1() -> Model:
    """Construct the figure 0357.g1 using geometor.model."""
    model = Model("0357.g1")

    # Single-letter horizontal number segments A, B, C, D, E, F, G, H, K, M, N, O, P, Q, R, S, T
    A_l = model.set_point(78.0, -14.0, classes=["given"], label="A")
    A_r = model.set_point(113.0, -14.0, label="A_r")

    C_l = model.set_point(177.0, -14.0, classes=["given"], label="C")
    C_r = model.set_point(202.0, -14.0, label="C_r")

    E_l = model.set_point(290.0, -16.0, classes=["given"], label="E")
    E_r = model.set_point(339.0, -16.0, label="E_r")

    B_l = model.set_point(77.0, -36.0, classes=["given"], label="B")
    B_r = model.set_point(120.0, -36.0, label="B_r")

    D_l = model.set_point(177.0, -38.0, classes=["given"], label="D")
    D_r = model.set_point(202.0, -38.0, label="D_r")

    F_l = model.set_point(289.0, -38.0, classes=["given"], label="F")
    F_r = model.set_point(346.0, -38.0, label="F_r")

    G_l = model.set_point(146.0, -60.0, classes=["given"], label="G")
    G_r = model.set_point(225.0, -60.0, label="G_r")

    H_l = model.set_point(287.0, -60.0, classes=["given"], label="H")
    H_r = model.set_point(361.0, -60.0, label="H_r")

    K_l = model.set_point(136.0, -84.0, classes=["given"], label="K")
    K_r = model.set_point(257.0, -84.0, label="K_r")

    Q_l = model.set_point(349.0, -86.0, classes=["given"], label="Q")
    Q_r = model.set_point(434.0, -86.0, label="Q_r")

    M_l = model.set_point(24.0, -109.0, classes=["given"], label="M")
    M_r = model.set_point(261.0, -109.0, label="M_r")

    R_l = model.set_point(348.0, -110.0, classes=["given"], label="R")
    R_r = model.set_point(456.0, -110.0, label="R_r")

    O_l = model.set_point(24.0, -132.0, classes=["given"], label="O")
    O_r = model.set_point(183.0, -132.0, label="O_r")

    S_l = model.set_point(347.0, -132.0, classes=["given"], label="S")
    S_r = model.set_point(508.0, -132.0, label="S_r")

    N_l = model.set_point(24.0, -158.0, classes=["given"], label="N")
    N_r = model.set_point(152.0, -158.0, label="N_r")

    T_l = model.set_point(344.0, -160.0, classes=["given"], label="T")
    T_r = model.set_point(533.0, -160.0, label="T_r")

    P_l = model.set_point(26.0, -182.0, classes=["given"], label="P")
    P_r = model.set_point(300.0, -182.0, label="P_r")

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
    model.set_segment(M_l, M_r)
    model.set_segment(O_l, O_r)
    model.set_segment(N_l, N_r)
    model.set_segment(P_l, P_r)
    model.set_segment(Q_l, Q_r)
    model.set_segment(R_l, R_r)
    model.set_segment(S_l, S_r)
    model.set_segment(T_l, T_r)

    return model


if __name__ == "__main__":
    construct_0357_g1()
