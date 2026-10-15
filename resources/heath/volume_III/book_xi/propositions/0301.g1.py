"""Programmatic construction for Book XI, Proposition 15 (0301.g1).

If two straight lines meeting one another be parallel to two straight lines
meeting one another, not being in the same plane, the planes through them are
parallel.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0301_g1() -> Model:
    """Construct the figure for Book XI, Proposition 15 using geometor.model."""
    model = Model("0301.g1")

    # 1. Let the two straight lines AB, BC meeting one another be parallel to
    #    the two straight lines DE, EF meeting one another, not in the same plane.
    B = model.set_point(0, 1, classes=["given"], label="B")
    A = model.set_point(sp.Rational(-43, 145), sp.Rational(112, 145), classes=["given"], label="A")
    C = model.set_point(sp.Rational(30, 145), sp.Rational(112, 145), classes=["given"], label="C")

    # 2. Let BG be drawn from B perpendicular to the plane through DE, EF, meeting it at G.
    G = model.set_point(sp.Rational(4, 145), 0, label="G")
    E = model.set_point(sp.Rational(27, 145), sp.Rational(41, 145), classes=["given"], label="E")
    D = model.set_point(sp.Rational(-31, 145), sp.Rational(-5, 145), classes=["given"], label="D")
    F = model.set_point(sp.Rational(79, 145), sp.Rational(-20, 145), classes=["given"], label="F")

    # 3. Through G let GH be drawn parallel to ED, and GK parallel to EF.
    H = model.set_point(sp.Rational(-29, 145), sp.Rational(-25, 145), label="H")
    K = model.set_point(sp.Rational(25, 145), sp.Rational(-24, 145), label="K")

    # Plane through AB, BC corners
    P1 = model.set_point(sp.Rational(-75, 145), sp.Rational(168, 145), label="P1")
    P2 = model.set_point(sp.Rational(65, 145), sp.Rational(168, 145), label="P2")
    P3 = model.set_point(sp.Rational(34, 145), sp.Rational(100, 145), label="P3")
    P4 = model.set_point(sp.Rational(-89, 145), sp.Rational(99, 145), label="P4")

    # Plane through DE, EF corners
    Q1 = model.set_point(sp.Rational(-24, 145), sp.Rational(57, 145), label="Q1")
    Q2 = model.set_point(sp.Rational(135, 145), sp.Rational(57, 145), label="Q2")
    Q3 = model.set_point(sp.Rational(93, 145), sp.Rational(-36, 145), label="Q3")
    Q4 = model.set_point(sp.Rational(-56, 145), sp.Rational(-36, 145), label="Q4")

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(B, G)
    model.set_segment(G, H)
    model.set_segment(G, K)

    # Planes
    model.set_polygon([P1, P2, P3, P4])
    model.set_polygon([Q1, Q2, Q3, Q4])
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])

    # Wedges for angles BGH, BGK, GBA
    model.set_wedge(G, H, H, B)
    model.set_wedge(G, B, B, K)
    model.set_wedge(B, G, G, A)

    return model


if __name__ == "__main__":
    construct_0301_g1()
