"""Programmatic construction for Book VIII, Proposition 13 (0372.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0372_g1() -> Model:
    """Construct the figure 0372.g1 using geometor.model."""
    model = Model("0372.g1")

    # Single-letter horizontal number segments A, B, C, D, E, F, L, O, G, H, K, M, N, P, Q
    A_l = model.set_point(26.0, -16.0, classes=["given"], label="A")
    A_r = model.set_point(71.0, -16.0, label="A_r")

    B_l = model.set_point(27.0, -38.0, classes=["given"], label="B")
    B_r = model.set_point(78.0, -38.0, label="B_r")

    C_l = model.set_point(26.0, -62.0, classes=["given"], label="C")
    C_r = model.set_point(86.0, -62.0, label="C_r")

    D_l = model.set_point(26.0, -86.0, classes=["given"], label="D")
    D_r = model.set_point(113.0, -86.0, label="D_r")

    E_l = model.set_point(26.0, -110.0, classes=["given"], label="E")
    E_r = model.set_point(131.0, -110.0, label="E_r")

    F_l = model.set_point(27.0, -134.0, classes=["given"], label="F")
    F_r = model.set_point(156.0, -134.0, label="F_r")

    L_l = model.set_point(25.0, -156.0, classes=["given"], label="L")
    L_r = model.set_point(122.0, -156.0, label="L_r")

    O_l = model.set_point(26.0, -180.0, classes=["given"], label="O")
    O_r = model.set_point(138.0, -180.0, label="O_r")

    G_l = model.set_point(247.0, -18.0, classes=["given"], label="G")
    G_r = model.set_point(383.0, -18.0, label="G_r")

    H_l = model.set_point(247.0, -39.0, classes=["given"], label="H")
    H_r = model.set_point(428.0, -39.0, label="H_r")

    K_l = model.set_point(248.0, -62.0, classes=["given"], label="K")
    K_r = model.set_point(494.0, -62.0, label="K_r")

    M_l = model.set_point(248.0, -103.0, classes=["given"], label="M")
    M_r = model.set_point(393.0, -103.0, label="M_r")

    N_l = model.set_point(247.0, -128.0, classes=["given"], label="N")
    N_r = model.set_point(413.0, -128.0, label="N_r")

    P_l = model.set_point(248.0, -152.0, classes=["given"], label="P")
    P_r = model.set_point(449.0, -152.0, label="P_r")

    Q_l = model.set_point(247.0, -180.0, classes=["given"], label="Q")
    Q_r = model.set_point(466.0, -180.0, label="Q_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(L_l, L_r)
    model.set_segment(O_l, O_r)
    model.set_segment(G_l, G_r)
    model.set_segment(H_l, H_r)
    model.set_segment(K_l, K_r)
    model.set_segment(M_l, M_r)
    model.set_segment(N_l, N_r)
    model.set_segment(P_l, P_r)
    model.set_segment(Q_l, Q_r)

    return model


if __name__ == "__main__":
    construct_0372_g1()
