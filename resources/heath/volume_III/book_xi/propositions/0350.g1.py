"""Programmatic construction for Book XI, Proposition 34 Case 1 (0350.g1).

In equal right parallelepipedal solids AB and CD, the bases EH and NQ are
reciprocally proportional to the heights AG and CM, proved by cutting off
CT equal to AG and completing solid CV.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0350_g1() -> Model:
    """Construct the right parallelepipeds figure for XI.34 Case 1 using geometor.model."""
    model = Model("0350.g1")

    # Left solid AB
    K = model.set_point(sp.Rational(56, 100), sp.Rational(208, 100), classes=["given"], label="K")
    B = model.set_point(sp.Rational(155, 100), sp.Rational(208, 100), classes=["given"], label="B")
    F = model.set_point(sp.Rational(124, 100), sp.Rational(170, 100), classes=["given"], label="F")
    G = model.set_point(sp.Rational(25, 100), sp.Rational(170, 100), classes=["given"], label="G")

    H = model.set_point(sp.Rational(56, 100), sp.Rational(94, 100), classes=["given"], label="H")
    L = model.set_point(sp.Rational(155, 100), sp.Rational(94, 100), classes=["given"], label="L")
    E = model.set_point(sp.Rational(124, 100), sp.Rational(56, 100), classes=["given"], label="E")
    A = model.set_point(sp.Rational(25, 100), sp.Rational(56, 100), classes=["given"], label="A")

    # Right solid CD with middle slice TV
    R = model.set_point(sp.Rational(314, 100), sp.Rational(246, 100), classes=["given"], label="R")
    D = model.set_point(sp.Rational(385, 100), sp.Rational(246, 100), classes=["given"], label="D")
    O = model.set_point(sp.Rational(398, 100), sp.Rational(190, 100), classes=["given"], label="O")
    M = model.set_point(sp.Rational(327, 100), sp.Rational(190, 100), classes=["given"], label="M")

    V_left = model.set_point(sp.Rational(314, 100), sp.Rational(200, 100), label="V_left")
    V = model.set_point(sp.Rational(385, 100), sp.Rational(200, 100), label="V")
    T_right = model.set_point(sp.Rational(398, 100), sp.Rational(144, 100), label="T_right")
    T = model.set_point(sp.Rational(327, 100), sp.Rational(144, 100), label="T")

    Q = model.set_point(sp.Rational(314, 100), sp.Rational(81, 100), classes=["given"], label="Q")
    P = model.set_point(sp.Rational(385, 100), sp.Rational(81, 100), classes=["given"], label="P")
    N = model.set_point(sp.Rational(398, 100), sp.Rational(25, 100), classes=["given"], label="N")
    C = model.set_point(sp.Rational(327, 100), sp.Rational(25, 100), classes=["given"], label="C")

    # Left solid AB segments and faces
    for p1, p2 in [
        (K, B), (B, F), (F, G), (G, K),
        (H, L), (L, E), (E, A), (A, H),
        (K, H), (B, L), (F, E), (G, A),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([H, L, E, A])
    model.set_polygon([K, B, F, G])

    # Right solid CD segments and faces
    for p1, p2 in [
        (R, D), (D, O), (O, M), (M, R),
        (V_left, V), (V, T_right), (T_right, T), (T, V_left),
        (Q, P), (P, N), (N, C), (C, Q),
        (R, Q), (D, P), (O, N), (M, C),
        (C, T), (T, M),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([Q, P, N, C])
    model.set_polygon([V_left, V, T_right, T])
    model.set_polygon([R, D, O, M])
    model.set_polygon([M, R, Q, C])
    model.set_polygon([T, V_left, Q, C])

    return model


if __name__ == "__main__":
    construct_0350_g1()
