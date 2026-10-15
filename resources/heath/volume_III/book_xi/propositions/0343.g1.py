"""Programmatic construction for Book XI, Proposition 31 Case 2 (0343.g1).

Oblique parallelepipedal solids AE and CF on equal bases AB and CD and of the
same height, together with right parallelepipedal solids KV and QI dropped
perpendicularly from top faces KM and QS to the planes of the bases.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0343_g1() -> Model:
    """Construct the two oblique-to-right parallelepiped figures for XI.31 Case 2."""
    model = Model("0343.g1")

    # Left figure: Top face GKEM, oblique base AHBL, right base UOTV
    G = model.set_point(sp.Rational(42, 100), sp.Rational(136, 100), classes=["given"], label="G")
    K = model.set_point(sp.Rational(146, 100), sp.Rational(136, 100), classes=["given"], label="K")
    E = model.set_point(sp.Rational(128, 100), sp.Rational(100, 100), classes=["given"], label="E")
    M = model.set_point(sp.Rational(24, 100), sp.Rational(100, 100), classes=["given"], label="M")

    U = model.set_point(sp.Rational(42, 100), sp.Rational(54, 100), label="U")
    O = model.set_point(sp.Rational(146, 100), sp.Rational(54, 100), label="O")
    T = model.set_point(sp.Rational(128, 100), sp.Rational(18, 100), label="T")
    V = model.set_point(sp.Rational(24, 100), sp.Rational(18, 100), label="V")

    A = model.set_point(sp.Rational(65, 100), sp.Rational(54, 100), classes=["given"], label="A")
    H = model.set_point(sp.Rational(169, 100), sp.Rational(54, 100), classes=["given"], label="H")
    B = model.set_point(sp.Rational(151, 100), sp.Rational(18, 100), classes=["given"], label="B")
    L = model.set_point(sp.Rational(47, 100), sp.Rational(18, 100), classes=["given"], label="L")

    # Right figure: Top face QFNS, oblique base PDRC, right base WXIY
    Q = model.set_point(sp.Rational(305, 100), sp.Rational(138, 100), classes=["given"], label="Q")
    F = model.set_point(sp.Rational(406, 100), sp.Rational(138, 100), classes=["given"], label="F")
    S = model.set_point(sp.Rational(426, 100), sp.Rational(102, 100), classes=["given"], label="S")
    N = model.set_point(sp.Rational(325, 100), sp.Rational(102, 100), classes=["given"], label="N")

    W = model.set_point(sp.Rational(305, 100), sp.Rational(54, 100), label="W")
    X = model.set_point(sp.Rational(406, 100), sp.Rational(54, 100), label="X")
    I = model.set_point(sp.Rational(426, 100), sp.Rational(18, 100), label="I")
    Y = model.set_point(sp.Rational(325, 100), sp.Rational(18, 100), label="Y")

    P = model.set_point(sp.Rational(282, 100), sp.Rational(54, 100), classes=["given"], label="P")
    D = model.set_point(sp.Rational(383, 100), sp.Rational(54, 100), classes=["given"], label="D")
    R = model.set_point(sp.Rational(403, 100), sp.Rational(18, 100), classes=["given"], label="R")
    C = model.set_point(sp.Rational(302, 100), sp.Rational(18, 100), classes=["given"], label="C")

    # Left segments and faces
    for p1, p2 in [
        (G, K), (K, E), (E, M), (M, G),
        (A, G), (H, K), (B, E), (L, M),
        (G, U), (K, O), (E, T), (M, V),
        (U, O), (O, T), (T, V), (V, U),
        (A, H), (H, B), (B, L), (L, A),
        (U, A), (A, O), (O, H),
        (V, L), (L, T), (T, B),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([G, K, E, M])
    model.set_polygon([U, O, T, V])
    model.set_polygon([A, H, B, L])

    # Right segments and faces
    for p1, p2 in [
        (Q, F), (F, S), (S, N), (N, Q),
        (P, Q), (D, F), (R, S), (C, N),
        (Q, W), (F, X), (S, I), (N, Y),
        (W, X), (X, I), (I, Y), (Y, W),
        (P, D), (D, R), (R, C), (C, P),
        (P, W), (W, D), (D, X),
        (C, Y), (Y, R), (R, I),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([Q, F, S, N])
    model.set_polygon([W, X, I, Y])
    model.set_polygon([P, D, R, C])

    return model


if __name__ == "__main__":
    construct_0343_g1()
