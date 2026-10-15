"""Programmatic construction for Book XI, Prop. 23 Simson Case III & Prop. 24 (0327.g1).

Upper figure: Simson's Case III (O outside triangle LMN, with auxiliary vertices
P, Q, R and point S such that triangle NRS is congruent to LPM).
Lower figure: Book XI, Proposition 24 parallelepiped CDHG contained by six
parallel planes with face diagonals AH and DF.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0327_g1() -> Model:
    """Construct Simson's Case III and Book XI, Prop. 24 figures using geometor.model."""
    model = Model("0327.g1")

    # Simson Case III (Upper figure)
    O = model.set_point(sp.Rational(355, 100), sp.Rational(-326, 100), classes=["given"], label="O")
    L = model.set_point(sp.Rational(378, 100), sp.Rational(-214, 100), classes=["given"], label="L")
    M = model.set_point(sp.Rational(246, 100), sp.Rational(-278, 100), classes=["given"], label="M")
    N = model.set_point(sp.Rational(459, 100), sp.Rational(-288, 100), classes=["given"], label="N")
    P = model.set_point(sp.Rational(352, 100), sp.Rational(-296, 100), label="P")
    Q = model.set_point(sp.Rational(356, 100), sp.Rational(-282, 100), label="Q")
    R = model.set_point(sp.Rational(368, 100), sp.Rational(-298, 100), label="R")
    S = model.set_point(sp.Rational(392, 100), sp.Rational(-438, 100), label="S")

    model.construct_circle(O, L)

    for u, v in [
        (L, M), (M, N), (N, L),
        (L, O), (M, O), (N, O),
        (L, P), (M, P), (M, Q), (N, Q), (L, R), (N, R),
        (L, S), (R, S), (N, S),
    ]:
        model.set_segment(u, v)

    for tri in [
        [L, M, N], [L, O, M], [M, O, N], [N, O, L],
        [L, P, M], [M, Q, N], [N, R, L], [N, R, S], [L, N, S], [L, R, S],
    ]:
        model.set_polygon(tri)

    # Proposition 24 Parallelepiped CDHG (Lower figure)
    A = model.set_point(sp.Rational(306, 100), sp.Rational(-692, 100), classes=["given"], label="A")
    B = model.set_point(sp.Rational(319, 100), sp.Rational(-638, 100), classes=["given"], label="B")
    C = model.set_point(sp.Rational(345, 100), sp.Rational(-716, 100), classes=["given"], label="C")
    D = model.set_point(sp.Rational(332, 100), sp.Rational(-770, 100), classes=["given"], label="D")
    E = model.set_point(sp.Rational(488, 100), sp.Rational(-770, 100), classes=["given"], label="E")
    F = model.set_point(sp.Rational(501, 100), sp.Rational(-716, 100), classes=["given"], label="F")
    G = model.set_point(sp.Rational(462, 100), sp.Rational(-692, 100), classes=["given"], label="G")
    H = model.set_point(sp.Rational(475, 100), sp.Rational(-638, 100), classes=["given"], label="H")

    # 12 edges + 2 face diagonals AH, DF
    for u, v in [
        (A, B), (B, C), (C, D), (D, A),
        (H, G), (G, E), (E, F), (F, H),
        (B, H), (A, G), (C, F), (D, E),
        (A, H), (D, F),
    ]:
        model.set_segment(u, v)

    # 6 parallelogram faces + 2 triangles ABH, DCF + solid hull
    for poly in [
        [A, B, C, D],
        [H, G, E, F],
        [A, B, H, G],
        [D, C, F, E],
        [B, C, F, H],
        [A, D, E, G],
        [A, B, H],
        [D, C, F],
    ]:
        model.set_polygon(poly)

    model.set_wedge(B, A, A, H)
    model.set_wedge(C, D, D, F)

    return model


if __name__ == "__main__":
    construct_0327_g1()
