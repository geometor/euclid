"""Programmatic construction for Book XI, Proposition 28 Commentary (0335.g1).

The sections of a prism MN made by parallel planes cutting all the lateral edges
are equal polygons ABCDE and A'B'C'D'E'.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0335_g1() -> Model:
    """Construct the prism cut by parallel planes for Book XI, Prop. 28 note."""
    model = Model("0335.g1")

    # Top pentagon vertices of prism MN
    M = model.set_point(sp.Rational(25, 100), sp.Rational(196, 100), classes=["given"], label="M")
    P2_top = model.set_point(sp.Rational(66, 100), sp.Rational(178, 100), label="P2_top")
    P3_top = model.set_point(sp.Rational(128, 100), sp.Rational(177, 100), label="P3_top")
    P4_top = model.set_point(sp.Rational(162, 100), sp.Rational(199, 100), label="P4_top")
    P5_top = model.set_point(sp.Rational(76, 100), sp.Rational(234, 100), label="P5_top")

    # Upper parallel section A'B'C'D'E'
    Ap = model.set_point(sp.Rational(45, 100), sp.Rational(107, 100), classes=["given"], label="A'")
    Bp = model.set_point(sp.Rational(83, 100), sp.Rational(105, 100), classes=["given"], label="B'")
    Cp = model.set_point(sp.Rational(143, 100), sp.Rational(114, 100), classes=["given"], label="C'")
    Dp = model.set_point(sp.Rational(176, 100), sp.Rational(138, 100), classes=["given"], label="D'")
    Ep = model.set_point(sp.Rational(94, 100), sp.Rational(154, 100), classes=["given"], label="E'")

    # Lower parallel section ABCDE
    A = model.set_point(sp.Rational(52, 100), sp.Rational(77, 100), classes=["given"], label="A")
    B = model.set_point(sp.Rational(89, 100), sp.Rational(75, 100), classes=["given"], label="B")
    C = model.set_point(sp.Rational(149, 100), sp.Rational(84, 100), classes=["given"], label="C")
    D = model.set_point(sp.Rational(183, 100), sp.Rational(107, 100), classes=["given"], label="D")
    E = model.set_point(sp.Rational(101, 100), sp.Rational(123, 100), classes=["given"], label="E")

    # Bottom pentagon vertices of prism MN
    M_bot = model.set_point(sp.Rational(62, 100), sp.Rational(29, 100), label="M_bot")
    P2_bot = model.set_point(sp.Rational(103, 100), sp.Rational(10, 100), label="P2_bot")
    P3_bot = model.set_point(sp.Rational(165, 100), sp.Rational(10, 100), label="P3_bot")
    N = model.set_point(sp.Rational(199, 100), sp.Rational(34, 100), classes=["given"], label="N")
    P5_bot = model.set_point(sp.Rational(113, 100), sp.Rational(68, 100), label="P5_bot")

    # Lateral edges
    model.set_segment(M, M_bot)
    model.set_segment(P2_top, P2_bot)
    model.set_segment(P3_top, P3_bot)
    model.set_segment(P4_top, N)
    model.set_segment(P5_top, P5_bot)

    # Section segments
    for pts in [(Ap, Bp, Cp, Dp, Ep), (A, B, C, D, E)]:
        for i in range(5):
            model.set_segment(pts[i], pts[(i + 1) % 5])
        model.set_polygon(list(pts))

    # Whole prism hull MN
    model.set_polygon([M, P5_top, P4_top, N, P3_bot, P2_bot, M_bot])

    return model


if __name__ == "__main__":
    construct_0335_g1()
