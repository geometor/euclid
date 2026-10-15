"""Programmatic construction for Book XI, Proposition 27 (0333.g1).

On a given straight line AB describe a parallelepipedal solid AL similar and
similarly situated to a given parallelepipedal solid CD.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0333_g1() -> Model:
    """Construct the figure for Book XI, Proposition 27 using geometor.model."""
    model = Model("0333.g1")

    # Given parallelepipedal solid CD
    C = model.set_point(sp.Rational(32, 100), sp.Rational(-128, 100), classes=["given"], label="C")
    E = model.set_point(sp.Rational(171, 100), sp.Rational(-128, 100), classes=["given"], label="E")
    F = model.set_point(sp.Rational(18, 100), sp.Rational(-52, 100), classes=["given"], label="F")
    Fr = model.set_point(sp.Rational(157, 100), sp.Rational(-52, 100), label="Fr")
    G = model.set_point(sp.Rational(49, 100), sp.Rational(-97, 100), classes=["given"], label="G")
    Db = model.set_point(sp.Rational(188, 100), sp.Rational(-97, 100), label="Db")
    Gt = model.set_point(sp.Rational(35, 100), sp.Rational(-28, 100), label="Gt")
    D = model.set_point(sp.Rational(174, 100), sp.Rational(-28, 100), classes=["given"], label="D")

    # Constructed parallelepipedal solid AL on AB
    A = model.set_point(sp.Rational(292, 100), sp.Rational(-119, 100), classes=["given"], label="A")
    B = model.set_point(sp.Rational(375, 100), sp.Rational(-119, 100), classes=["given"], label="B")
    H = model.set_point(sp.Rational(285, 100), sp.Rational(-77, 100), label="H")
    M = model.set_point(sp.Rational(368, 100), sp.Rational(-77, 100), label="M")
    K = model.set_point(sp.Rational(302, 100), sp.Rational(-104, 100), label="K")
    Lb = model.set_point(sp.Rational(385, 100), sp.Rational(-104, 100), label="Lb")
    Kt = model.set_point(sp.Rational(295, 100), sp.Rational(-62, 100), label="Kt")
    L = model.set_point(sp.Rational(378, 100), sp.Rational(-62, 100), label="L")

    # Edges
    for u, v in [
        (C, E), (C, F), (C, G), (F, Fr), (Fr, E), (G, Db), (Db, E), (Gt, D), (D, Db), (Gt, G), (Gt, F), (D, Fr),
        (A, B), (A, H), (A, K), (H, M), (M, B), (K, Lb), (Lb, B), (Kt, L), (L, Lb), (Kt, K), (Kt, H), (L, M),
    ]:
        model.set_segment(u, v)

    # Faces
    for poly in [
        [C, G, Db, E],
        [C, F, Gt, G],
        [C, F, Fr, E],
        [A, K, Lb, B],
        [A, H, Kt, K],
        [A, H, M, B],
    ]:
        model.set_polygon(poly)

    # Angles at C and A
    model.set_wedge(C, E, E, F)
    model.set_wedge(C, E, E, G)
    model.set_wedge(C, G, G, F)
    model.set_wedge(A, B, B, H)
    model.set_wedge(A, B, B, K)
    model.set_wedge(A, K, K, H)

    return model


if __name__ == "__main__":
    construct_0333_g1()
