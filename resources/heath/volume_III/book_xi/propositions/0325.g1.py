"""Programmatic construction for Book XI, Proposition 23 Simson's Case I (0325.g1).

Construct the three given isosceles triangles ABC, DEF, GHK and circumcircle
(O, L) of triangle LMN with O inside LMN and auxiliary triangles LPM, MQN, NLR
constructed inward on LM, MN, NL.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0325_g1() -> Model:
    """Construct Simson's Case I figure for Book XI, Proposition 23 using geometor.model."""
    model = Model("0325.g1")

    # Given triangles ABC, DEF, GHK
    A = model.set_point(sp.Rational(52, 100), sp.Rational(-102, 100), classes=["given"], label="A")
    B = model.set_point(sp.Rational(119, 100), sp.Rational(-43, 100), classes=["given"], label="B")
    C = model.set_point(sp.Rational(178, 100), sp.Rational(-102, 100), classes=["given"], label="C")

    D = model.set_point(sp.Rational(233, 100), sp.Rational(-102, 100), classes=["given"], label="D")
    E = model.set_point(sp.Rational(298, 100), sp.Rational(-32, 100), classes=["given"], label="E")
    F = model.set_point(sp.Rational(362, 100), sp.Rational(-102, 100), classes=["given"], label="F")

    G = model.set_point(sp.Rational(407, 100), sp.Rational(-102, 100), classes=["given"], label="G")
    H = model.set_point(sp.Rational(460, 100), sp.Rational(-32, 100), classes=["given"], label="H")
    K = model.set_point(sp.Rational(512, 100), sp.Rational(-102, 100), classes=["given"], label="K")

    # Circumcircle and triangle LMN with O inside
    O = model.set_point(sp.Rational(475, 100), sp.Rational(-226, 100), classes=["given"], label="O")
    L = model.set_point(sp.Rational(498, 100), sp.Rational(-150, 100), classes=["given"], label="L")
    M = model.set_point(sp.Rational(404, 100), sp.Rational(-264, 100), classes=["given"], label="M")
    N = model.set_point(sp.Rational(542, 100), sp.Rational(-264, 100), classes=["given"], label="N")

    # Auxiliary interior vertices P, Q, R
    P = model.set_point(sp.Rational(463, 100), sp.Rational(-215, 100), label="P")
    Q = model.set_point(sp.Rational(475, 100), sp.Rational(-244, 100), label="Q")
    R = model.set_point(sp.Rational(486, 100), sp.Rational(-222, 100), label="R")

    model.construct_circle(O, L)

    for u, v in [
        (A, B), (B, C), (A, C),
        (D, E), (E, F), (D, F),
        (G, H), (H, K), (G, K),
        (L, M), (M, N), (N, L),
        (L, O), (M, O), (N, O),
        (L, P), (M, P), (M, Q), (N, Q), (L, R), (N, R),
    ]:
        model.set_segment(u, v)

    for tri in [
        [A, B, C], [D, E, F], [G, H, K],
        [L, M, N], [L, O, M], [M, O, N], [N, O, L],
        [L, P, M], [M, Q, N], [N, R, L],
    ]:
        model.set_polygon(tri)

    # Angles at B, E, H, O, P, Q, R
    model.set_wedge(B, A, A, C)
    model.set_wedge(E, D, D, F)
    model.set_wedge(H, G, G, K)
    model.set_wedge(O, L, L, M)
    model.set_wedge(O, M, M, N)
    model.set_wedge(O, N, N, L)
    model.set_wedge(P, L, L, M)
    model.set_wedge(Q, M, M, N)
    model.set_wedge(R, N, N, L)

    return model


if __name__ == "__main__":
    construct_0325_g1()
