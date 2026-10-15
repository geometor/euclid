"""Programmatic construction for Book XI, Proposition 33 (0346.g1).

Similar parallelepipedal solids AB and CD are to one another in the triplicate
ratio of their corresponding sides AE and CF, proved by producing AE, GE, HE
to K, L, M and completing the continuously proportional solids EO, QL, KP.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0346_g1() -> Model:
    """Construct the similar parallelepipeds figure for XI.33 using geometor.model."""
    model = Model("0346.g1")

    # Left solid CD
    C1 = model.set_point(sp.Rational(48, 100), sp.Rational(361, 100), label="C1")
    N = model.set_point(sp.Rational(126, 100), sp.Rational(361, 100), classes=["given"], label="N")
    C = model.set_point(sp.Rational(30, 100), sp.Rational(319, 100), classes=["given"], label="C")
    F = model.set_point(sp.Rational(108, 100), sp.Rational(319, 100), classes=["given"], label="F")

    D1 = model.set_point(sp.Rational(70, 100), sp.Rational(274, 100), label="D1")
    D = model.set_point(sp.Rational(148, 100), sp.Rational(274, 100), classes=["given"], label="D")
    R1 = model.set_point(sp.Rational(52, 100), sp.Rational(232, 100), label="R1")
    R = model.set_point(sp.Rational(130, 100), sp.Rational(232, 100), classes=["given"], label="R")

    # Right compound figure (AB, EO, QL, KP)
    # Middle plane (z = 0)
    A_back = model.set_point(sp.Rational(282, 100), sp.Rational(215, 100), label="A_back")
    G = model.set_point(sp.Rational(392, 100), sp.Rational(215, 100), classes=["given"], label="G")
    K_back = model.set_point(sp.Rational(490, 100), sp.Rational(215, 100), label="K_back")

    A = model.set_point(sp.Rational(252, 100), sp.Rational(167, 100), classes=["given"], label="A")
    E = model.set_point(sp.Rational(362, 100), sp.Rational(167, 100), classes=["given"], label="E")
    K = model.set_point(sp.Rational(460, 100), sp.Rational(167, 100), label="K")

    L = model.set_point(sp.Rational(342, 100), sp.Rational(135, 100), label="L")
    K_front = model.set_point(sp.Rational(440, 100), sp.Rational(135, 100), label="K_front")

    # Top plane (z = +1)
    T_AB_BL = model.set_point(sp.Rational(250, 100), sp.Rational(359, 100), label="T_AB_BL")
    B = model.set_point(sp.Rational(360, 100), sp.Rational(359, 100), classes=["given"], label="B")
    O = model.set_point(sp.Rational(458, 100), sp.Rational(359, 100), label="O")

    T_AB_FL = model.set_point(sp.Rational(220, 100), sp.Rational(311, 100), label="T_AB_FL")
    H = model.set_point(sp.Rational(330, 100), sp.Rational(311, 100), classes=["given"], label="H")
    Q = model.set_point(sp.Rational(428, 100), sp.Rational(311, 100), label="Q")

    T_QL_FL = model.set_point(sp.Rational(310, 100), sp.Rational(279, 100), label="T_QL_FL")
    T_QL_FR = model.set_point(sp.Rational(408, 100), sp.Rational(279, 100), label="T_QL_FR")

    # Bottom plane (z = -1)
    M = model.set_point(sp.Rational(382, 100), sp.Rational(77, 100), label="M")
    M_right = model.set_point(sp.Rational(480, 100), sp.Rational(77, 100), label="M_right")
    P = model.set_point(sp.Rational(362, 100), sp.Rational(45, 100), label="P")
    P_right = model.set_point(sp.Rational(460, 100), sp.Rational(45, 100), label="P_right")

    # Left solid CD segments and faces
    for p1, p2 in [
        (C1, N), (N, F), (F, C), (C, C1),
        (D1, D), (D, R), (R, R1), (R1, D1),
        (C1, D1), (N, D), (F, R), (C, R1),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([C1, N, F, C])
    model.set_polygon([C, F, R, R1])
    model.set_polygon([F, N, D, R])

    # Right compound figure segments and faces
    for p1, p2 in [
        (A_back, G), (G, K_back),
        (A, E), (E, K),
        (L, K_front),
        (A_back, A), (G, E), (E, L), (K_back, K), (K, K_front),
        (T_AB_BL, B), (B, O),
        (T_AB_FL, H), (H, Q),
        (T_QL_FL, T_QL_FR),
        (T_AB_BL, T_AB_FL), (B, H), (H, T_QL_FL), (O, Q), (Q, T_QL_FR),
        (T_AB_BL, A_back), (T_AB_FL, A), (B, G), (O, K_back),
        (H, E), (E, M), (Q, K), (K, M_right),
        (T_QL_FL, L), (L, P), (T_QL_FR, K_front), (K_front, P_right),
        (M, M_right), (P, P_right), (M, P), (M_right, P_right),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([A_back, G, E, A])
    model.set_polygon([G, K_back, K, E])
    model.set_polygon([E, K, K_front, L])
    model.set_polygon([H, Q, K, E])
    model.set_polygon([E, K, M_right, M])
    model.set_polygon([E, L, P, M])

    return model


if __name__ == "__main__":
    construct_0346_g1()
