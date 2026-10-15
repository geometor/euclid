"""Programmatic construction for Book XI, Proposition 23 Simson's Case II (0326.g1).

Construct the three given isosceles triangles ABC, DEF, GHK and circumcircle
(O, M) of triangle LMN where O lies on diameter MN, with auxiliary points P, R.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0326_g1() -> Model:
    """Construct Simson's Case II figure for Book XI, Proposition 23 using geometor.model."""
    model = Model("0326.g1")

    # Given triangles ABC, DEF, GHK
    A = model.set_point(sp.Rational(32, 100), sp.Rational(-115, 100), classes=["given"], label="A")
    B = model.set_point(sp.Rational(102, 100), sp.Rational(-45, 100), classes=["given"], label="B")
    C = model.set_point(sp.Rational(171, 100), sp.Rational(-115, 100), classes=["given"], label="C")

    D = model.set_point(sp.Rational(196, 100), sp.Rational(-115, 100), classes=["given"], label="D")
    E = model.set_point(sp.Rational(278, 100), sp.Rational(-56, 100), classes=["given"], label="E")
    F = model.set_point(sp.Rational(362, 100), sp.Rational(-115, 100), classes=["given"], label="F")

    G = model.set_point(sp.Rational(382, 100), sp.Rational(-115, 100), classes=["given"], label="G")
    H = model.set_point(sp.Rational(425, 100), sp.Rational(-35, 100), classes=["given"], label="H")
    K = model.set_point(sp.Rational(468, 100), sp.Rational(-115, 100), classes=["given"], label="K")

    # Circumcircle and triangle LMN with O on MN
    O = model.set_point(sp.Rational(255, 100), sp.Rational(-232, 100), classes=["given"], label="O")
    L = model.set_point(sp.Rational(282, 100), sp.Rational(-163, 100), classes=["given"], label="L")
    M = model.set_point(sp.Rational(181, 100), sp.Rational(-232, 100), classes=["given"], label="M")
    N = model.set_point(sp.Rational(329, 100), sp.Rational(-232, 100), classes=["given"], label="N")

    P = model.set_point(sp.Rational(244, 100), sp.Rational(-205, 100), label="P")
    R = model.set_point(sp.Rational(268, 100), sp.Rational(-215, 100), label="R")

    model.construct_circle(O, M)

    for u, v in [
        (A, B), (B, C), (A, C),
        (D, E), (E, F), (D, F),
        (G, H), (H, K), (G, K),
        (L, M), (M, N), (N, L),
        (L, O), (M, O), (N, O),
        (L, P), (M, P), (L, R), (N, R),
    ]:
        model.set_segment(u, v)

    for tri in [
        [A, B, C], [D, E, F], [G, H, K],
        [L, M, N], [L, O, M], [N, O, L],
        [L, P, M], [N, R, L],
    ]:
        model.set_polygon(tri)

    return model


if __name__ == "__main__":
    construct_0326_g1()
