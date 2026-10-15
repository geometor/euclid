"""Programmatic construction for Book XI, Proposition 25 (0329.g1).

Parallelepipedal solid ABCD cut by plane FG parallel to opposite planes RA, DH,
with equimultiple solids LQ, KR to the left and DM, MT to the right.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0329_g1() -> Model:
    """Construct the figure for Book XI, Proposition 25 using geometor.model."""
    model = Model("0329.g1")

    # 7 cross-sectional planes from left to right (j = 0..6)
    # Top-back row (y = -29)
    X = model.set_point(sp.Rational(56, 100), sp.Rational(-29, 100), label="X")
    Q = model.set_point(sp.Rational(122, 100), sp.Rational(-29, 100), label="Q")
    R = model.set_point(sp.Rational(198, 100), sp.Rational(-29, 100), classes=["given"], label="R")
    U = model.set_point(sp.Rational(274, 100), sp.Rational(-29, 100), label="U")
    D = model.set_point(sp.Rational(336, 100), sp.Rational(-29, 100), classes=["given"], label="D")
    Y = model.set_point(sp.Rational(388, 100), sp.Rational(-29, 100), label="Y")
    T = model.set_point(sp.Rational(438, 100), sp.Rational(-29, 100), label="T")

    # Top-front row (y = -60)
    O = model.set_point(sp.Rational(23, 100), sp.Rational(-60, 100), label="O")
    O1 = model.set_point(sp.Rational(89, 100), sp.Rational(-60, 100), label="O1")
    B = model.set_point(sp.Rational(165, 100), sp.Rational(-60, 100), classes=["given"], label="B")
    G = model.set_point(sp.Rational(241, 100), sp.Rational(-60, 100), label="G")
    G4 = model.set_point(sp.Rational(303, 100), sp.Rational(-60, 100), label="G4")
    I = model.set_point(sp.Rational(355, 100), sp.Rational(-60, 100), label="I")
    I6 = model.set_point(sp.Rational(405, 100), sp.Rational(-60, 100), label="I6")

    # Bottom-back row (y = -146)
    P0 = model.set_point(sp.Rational(82, 100), sp.Rational(-146, 100), label="P0")
    P = model.set_point(sp.Rational(148, 100), sp.Rational(-146, 100), label="P")
    V = model.set_point(sp.Rational(224, 100), sp.Rational(-146, 100), label="V")
    F = model.set_point(sp.Rational(300, 100), sp.Rational(-146, 100), label="F")
    C = model.set_point(sp.Rational(362, 100), sp.Rational(-146, 100), classes=["given"], label="C")
    W = model.set_point(sp.Rational(414, 100), sp.Rational(-146, 100), label="W")
    S = model.set_point(sp.Rational(464, 100), sp.Rational(-146, 100), label="S")

    # Bottom-front row (y = -177)
    L = model.set_point(sp.Rational(49, 100), sp.Rational(-177, 100), label="L")
    K = model.set_point(sp.Rational(115, 100), sp.Rational(-177, 100), label="K")
    A = model.set_point(sp.Rational(191, 100), sp.Rational(-177, 100), classes=["given"], label="A")
    E = model.set_point(sp.Rational(267, 100), sp.Rational(-177, 100), label="E")
    H = model.set_point(sp.Rational(329, 100), sp.Rational(-177, 100), classes=["given"], label="H")
    M = model.set_point(sp.Rational(381, 100), sp.Rational(-177, 100), label="M")
    N = model.set_point(sp.Rational(431, 100), sp.Rational(-177, 100), label="N")

    # Segments along bottom-front edge
    for u, v in [
        (L, K), (K, A), (A, E), (E, H), (H, M), (M, N), (A, H),
    ]:
        model.set_segment(u, v)

    # Cross-section planes
    for p1, p2, p3, p4 in [
        (L, O, X, P0),
        (K, O1, Q, P),
        (A, B, R, V),
        (E, G, U, F),
        (H, G4, D, C),
        (M, I, Y, W),
        (N, I6, T, S),
    ]:
        model.set_polygon([p1, p2, p3, p4])

    # Base parallelograms
    for p1, p2, p3, p4 in [
        (L, P0, P, K),
        (K, P, V, A),
        (A, V, F, E),
        (E, F, C, H),
        (H, C, W, M),
        (M, W, S, N),
        (L, P0, F, E),
        (E, F, S, N),
    ]:
        model.set_polygon([p1, p2, p3, p4])

    # Front parallelograms
    for p1, p2, p3, p4 in [
        (L, O, O1, K),
        (K, O1, B, A),
        (A, B, G, E),
        (E, G, G4, H),
        (H, G4, I, M),
        (M, I, I6, N),
    ]:
        model.set_polygon([p1, p2, p3, p4])

    return model


if __name__ == "__main__":
    construct_0329_g1()
