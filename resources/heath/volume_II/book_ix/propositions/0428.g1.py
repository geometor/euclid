"""Programmatic construction for Book IX, Proposition 36 (0428.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0428_g1() -> Model:
    """Construct the figure 0428.g1 using geometor.model."""
    model = Model("0428.g1")

    # Single-letter number segments A, B, C, D, L, E, M, P, Q
    A_l = model.set_point(177.0, -21.5, classes=["given"], label="A")
    A_r = model.set_point(200.0, -21.5, label="A_r")

    B_l = model.set_point(253.0, -21.5, classes=["given"], label="B")
    B_r = model.set_point(305.0, -21.5, label="B_r")

    C_l = model.set_point(240.0, -40.5, classes=["given"], label="C")
    C_r = model.set_point(321.0, -40.5, label="C_r")

    D_l = model.set_point(235.0, -61.0, classes=["given"], label="D")
    D_r = model.set_point(394.0, -61.0, label="D_r")

    L_l = model.set_point(177.0, -82.5, classes=["given"], label="L")
    L_r = model.set_point(400.0, -82.5, label="L_r")

    E_l = model.set_point(455.0, -83.5, classes=["given"], label="E")
    E_r = model.set_point(515.0, -83.5, label="E_r")

    M_l = model.set_point(16.0, -101.0, classes=["given"], label="M")
    M_r = model.set_point(465.0, -101.0, label="M_r")

    # Subdivided number segment HK (divided at N)
    H = model.set_point(403.0, -113.5, classes=["given"], label="H")
    N = model.set_point(463.0, -113.5, label="N")
    K = model.set_point(521.0, -113.5, classes=["given"], label="K")

    # Subdivided number segment FG (divided at O)
    F = model.set_point(26.0, -126.0, classes=["given"], label="F")
    O = model.set_point(90.0, -126.0, label="O")
    G = model.set_point(297.0, -126.0, classes=["given"], label="G")

    # Single-letter number segments P, Q
    P_l = model.set_point(64.0, -151.5, classes=["given"], label="P")
    P_r = model.set_point(245.0, -151.5, label="P_r")

    Q_l = model.set_point(302.0, -151.5, classes=["given"], label="Q")
    Q_r = model.set_point(425.0, -151.5, label="Q_r")

    # Base lines for subdivided segments
    model.construct_line(H, K)
    model.construct_line(F, G)

    # Standalone segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(L_l, L_r)
    model.set_segment(E_l, E_r)
    model.set_segment(M_l, M_r)
    model.set_segment(P_l, P_r)
    model.set_segment(Q_l, Q_r)

    # Whole and subdivided segments on HK
    model.set_segment(H, K)
    model.set_segment(H, N)
    model.set_segment(N, K)

    # Whole and subdivided segments on FG
    model.set_segment(F, G)
    model.set_segment(F, O)
    model.set_segment(O, G)

    # Collinear sections
    model.set_section([H, N, K])
    model.set_section([F, O, G])

    return model


if __name__ == "__main__":
    construct_0428_g1()
