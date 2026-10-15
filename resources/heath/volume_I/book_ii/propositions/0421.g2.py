"""Programmatic construction for Book II, Proposition 13 alternative proof (0421.g2).

Alternative proof of Book II, Proposition 13 (acute-angled triangle case) after
the manner of I. 47.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0421_g2() -> Model:
    """Construct the figure for 0421.g2 using geometor.model."""
    model = Model("0421.g2")

    # Acute-angled triangle ABC
    B = model.set_point(0, 0, classes=["given"], label="B")
    C = model.set_point(40, 0, classes=["given"], label="C")
    A = model.set_point(26, 25, classes=["given"], label="A")

    # Square BCED on BC
    D = model.set_point(0, -40, label="D")
    E = model.set_point(40, -40, label="E")

    # Square ABKH on AB
    K = model.set_point(-25, 26, label="K")
    H = model.set_point(1, 51, label="H")

    # Square CAGF on CA
    F = model.set_point(65, 14, label="F")
    G = model.set_point(51, 39, label="G")

    # Altitude ALP
    L = model.set_point(26, 0, label="L")
    P = model.set_point(26, -40, label="P")

    # Altitude BMQ
    M = model.set_point(sp.Rational(24980, 821), sp.Rational(14000, 821), label="M")
    Q = model.set_point(sp.Rational(45505, 821), sp.Rational(25494, 821), label="Q")

    # Altitude CNR
    N = model.set_point(sp.Rational(27040, 1301), sp.Rational(26000, 1301), label="N")
    R = model.set_point(sp.Rational(-5485, 1301), sp.Rational(59826, 1301), label="R")

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

    # Congruent triangles KBC, ABD, BAG, HAC
    model.set_polygon([K, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([B, A, G])
    model.set_polygon([H, A, C])

    # Segments
    for p1, p2 in [
        (B, C), (C, A), (A, B),
        (B, D), (D, E), (C, E), (B, L), (L, C),
        (A, L), (L, P), (A, P),
        (B, K), (K, H), (A, H), (A, N), (N, B), (C, N), (N, R), (C, R),
        (C, F), (F, G), (A, G), (A, M), (M, C), (B, M), (M, Q), (B, Q),
        (K, C), (A, D), (B, G), (C, H),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0421_g2()
