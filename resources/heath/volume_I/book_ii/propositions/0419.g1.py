"""Programmatic construction for Book II, Proposition 12 alternative proof (0419.g1).

Alternative proof of Book II, Proposition 12 after the manner of I. 47.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0419_g1() -> Model:
    """Construct the figure for 0419.g1 using geometor.model."""
    model = Model("0419.g1")

    # Obtuse-angled triangle ABC with obtuse angle at A
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

    # Altitude ALP to BC and DE
    L = model.set_point(7, 0, label="L")
    P = model.set_point(7, -11, label="P")

    # Altitude BMQ to CA produced and FG produced
    M = model.set_point(sp.Rational(539, 149), sp.Rational(763, 149), label="M")
    Q = model.set_point(sp.Rational(956, 149), sp.Rational(1359, 149), label="Q")

    # Altitude CNR to BA produced and KH produced
    N = model.set_point(sp.Rational(1925, 203), sp.Rational(770, 203), label="N")
    R = model.set_point(sp.Rational(1357, 203), sp.Rational(2191, 203), label="R")

    # Base lines produced
    model.construct_line(C, A)
    model.construct_line(B, A)
    model.construct_line(F, G)
    model.construct_line(K, H)

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

    # Auxiliary triangles KBC, ABD, BAG, HAC
    model.set_polygon([K, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([B, A, G])
    model.set_polygon([H, A, C])

    # Segments
    for p1, p2 in [
        (B, C), (C, A), (A, B),
        (B, D), (D, E), (C, E), (B, L), (L, C), (D, P), (P, E),
        (A, L), (L, P), (A, P),
        (A, K), (B, K), (K, H), (A, H), (H, R), (K, R),
        (C, F), (F, G), (A, G), (G, Q), (F, Q),
        (A, M), (C, M), (B, M), (M, Q), (B, Q),
        (A, N), (B, N), (C, N), (N, R), (C, R),
        (A, D), (C, K), (B, G), (C, H),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0419_g1()
