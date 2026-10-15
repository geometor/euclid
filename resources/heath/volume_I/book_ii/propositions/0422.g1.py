"""Programmatic construction for Book II, Proposition 13 obtuse-triangle case (0422.g1).

Alternative proof of Book II, Proposition 13 for an acute angle of an
obtuse-angled triangle after the manner of I. 47.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0422_g1() -> Model:
    """Construct the figure for 0422.g1 using geometor.model."""
    model = Model("0422.g1")

    # Obtuse-angled triangle ABC with obtuse angle at A and acute angle at B
    B = model.set_point(0, 0, classes=["given"], label="B")
    C = model.set_point(11, 0, classes=["given"], label="C")
    A = model.set_point(7, sp.Rational(14, 5), classes=["given"], label="A")

    # Square BCED on BC
    D = model.set_point(0, -11, label="D")
    E = model.set_point(11, -11, label="E")

    # Square ABKH on AB
    K = model.set_point(sp.Rational(-14, 5), 7, label="K")
    H = model.set_point(sp.Rational(21, 5), sp.Rational(49, 5), label="H")

    # Square CAGF on CA
    F = model.set_point(sp.Rational(69, 5), 4, label="F")
    G = model.set_point(sp.Rational(49, 5), sp.Rational(34, 5), label="G")

    # Altitudes ALP, BMQ, CNR
    L = model.set_point(7, 0, label="L")
    P = model.set_point(7, -11, label="P")
    M = model.set_point(sp.Rational(539, 149), sp.Rational(763, 149), label="M")
    Q = model.set_point(sp.Rational(956, 149), sp.Rational(1359, 149), label="Q")
    N = model.set_point(sp.Rational(1925, 203), sp.Rational(770, 203), label="N")
    R = model.set_point(sp.Rational(1357, 203), sp.Rational(2191, 203), label="R")

    # Triangle and squares
    model.set_polygon([A, B, C])
    model.set_polygon([B, C, E, D])
    model.set_polygon([C, A, G, F])
    model.set_polygon([A, B, K, H])

    # Sub-rectangles BP, CP, BR, CQ, AR, AQ
    model.set_polygon([B, L, P, D])
    model.set_polygon([L, C, E, P])
    model.set_polygon([B, N, R, K])
    model.set_polygon([C, M, Q, F])
    model.set_polygon([A, N, R, H])
    model.set_polygon([A, M, Q, G])

    # Angles at A and B
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, C, C, A)

    # Segments
    for p1, p2 in [
        (B, C), (C, A), (A, B),
        (B, D), (D, E), (C, E), (B, L), (L, C),
        (A, L), (L, P), (A, P),
        (B, K), (K, H), (A, H), (A, N), (B, N), (C, N), (N, R), (C, R),
        (C, F), (F, G), (A, G), (A, M), (C, M), (B, M), (M, Q), (B, Q),
        (A, D), (C, K), (B, G), (C, H),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0422_g1()
