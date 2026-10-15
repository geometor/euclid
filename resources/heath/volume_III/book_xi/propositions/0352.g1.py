"""Programmatic construction for Book XI, Proposition 34 Case 2 (0352.g1).

Oblique parallelepipedal solids AB and CD on bases EH and NQ, together with
right parallelepipedal solids BT (or FV) and DX (or Oa) formed by dropping
perpendiculars FS, GT, BU, KV and OW, MX, DY, Ra to the planes of the bases.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0352_g1() -> Model:
    """Construct the oblique parallelepipeds figure for XI.34 Case 2 using geometor.model."""
    model = Model("0352.g1")

    # Left figure: Top face KBFG, oblique base HLEA, right base VUST
    K = model.set_point(sp.Rational(76, 100), sp.Rational(206, 100), classes=["given"], label="K")
    B = model.set_point(sp.Rational(182, 100), sp.Rational(206, 100), classes=["given"], label="B")
    F = model.set_point(sp.Rational(200, 100), sp.Rational(172, 100), classes=["given"], label="F")
    G = model.set_point(sp.Rational(94, 100), sp.Rational(172, 100), classes=["given"], label="G")

    H = model.set_point(sp.Rational(26, 100), sp.Rational(110, 100), classes=["given"], label="H")
    L = model.set_point(sp.Rational(132, 100), sp.Rational(110, 100), classes=["given"], label="L")
    E = model.set_point(sp.Rational(150, 100), sp.Rational(76, 100), classes=["given"], label="E")
    A = model.set_point(sp.Rational(44, 100), sp.Rational(76, 100), classes=["given"], label="A")

    V = model.set_point(sp.Rational(76, 100), sp.Rational(94, 100), label="V")
    U = model.set_point(sp.Rational(182, 100), sp.Rational(94, 100), label="U")
    S = model.set_point(sp.Rational(200, 100), sp.Rational(60, 100), label="S")
    T = model.set_point(sp.Rational(94, 100), sp.Rational(60, 100), label="T")

    # Right figure: Top face RDOM, oblique base QPNC, right base aYWX
    R = model.set_point(sp.Rational(295, 100), sp.Rational(234, 100), classes=["given"], label="R")
    D = model.set_point(sp.Rational(378, 100), sp.Rational(234, 100), classes=["given"], label="D")
    O = model.set_point(sp.Rational(352, 100), sp.Rational(197, 100), classes=["given"], label="O")
    M = model.set_point(sp.Rational(269, 100), sp.Rational(197, 100), classes=["given"], label="M")

    Q = model.set_point(sp.Rational(318, 100), sp.Rational(67, 100), classes=["given"], label="Q")
    P = model.set_point(sp.Rational(401, 100), sp.Rational(67, 100), classes=["given"], label="P")
    N = model.set_point(sp.Rational(375, 100), sp.Rational(30, 100), classes=["given"], label="N")
    C = model.set_point(sp.Rational(292, 100), sp.Rational(30, 100), classes=["given"], label="C")

    a = model.set_point(sp.Rational(295, 100), sp.Rational(78, 100), label="a")
    Y = model.set_point(sp.Rational(378, 100), sp.Rational(78, 100), label="Y")
    W = model.set_point(sp.Rational(352, 100), sp.Rational(41, 100), label="W")
    X = model.set_point(sp.Rational(269, 100), sp.Rational(41, 100), label="X")

    # Left segments and faces
    for p1, p2 in [
        (K, B), (B, F), (F, G), (G, K),
        (H, L), (L, E), (E, A), (A, H),
        (V, U), (U, S), (S, T), (T, V),
        (K, H), (B, L), (F, E), (G, A),
        (K, V), (B, U), (F, S), (G, T),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([K, B, F, G])
    model.set_polygon([H, L, E, A])
    model.set_polygon([V, U, S, T])

    # Right segments and faces
    for p1, p2 in [
        (R, D), (D, O), (O, M), (M, R),
        (Q, P), (P, N), (N, C), (C, Q),
        (a, Y), (Y, W), (W, X), (X, a),
        (R, Q), (D, P), (O, N), (M, C),
        (R, a), (D, Y), (O, W), (M, X),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([R, D, O, M])
    model.set_polygon([Q, P, N, C])
    model.set_polygon([a, Y, W, X])

    return model


if __name__ == "__main__":
    construct_0352_g1()
