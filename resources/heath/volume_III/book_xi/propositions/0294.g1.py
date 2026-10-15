"""Programmatic construction for Book XI, Proposition 9 (0294.g1).

Straight lines which are parallel to the same straight line and are not in the
same plane with it are also parallel to one another.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0294_g1() -> Model:
    """Construct the figure for Book XI, Proposition 9 using geometor.model."""
    model = Model("0294.g1")

    # 1. Let each of the straight lines AB, CD be parallel to EF, not being in
    #    the same plane with it.
    G = model.set_point(0, 0, classes=["given"], label="G")
    F = model.set_point(sp.Rational(-84, 84), 0, classes=["given"], label="F")
    E = model.set_point(sp.Rational(85, 84), 0, classes=["given"], label="E")

    B = model.set_point(sp.Rational(-34, 84), sp.Rational(54, 84), classes=["given"], label="B")
    H = model.set_point(sp.Rational(39, 84), sp.Rational(54, 84), label="H")
    A = model.set_point(sp.Rational(134, 84), sp.Rational(55, 84), classes=["given"], label="A")

    D = model.set_point(sp.Rational(-41, 84), sp.Rational(-35, 84), classes=["given"], label="D")
    K = model.set_point(sp.Rational(38, 84), sp.Rational(-34, 84), label="K")
    C = model.set_point(sp.Rational(147, 84), sp.Rational(-33, 84), classes=["given"], label="C")

    # Collinear lines and sub-segments
    model.construct_line(B, A)
    model.set_section([B, H, A])
    model.set_segment(B, H)
    model.set_segment(H, A)
    model.set_segment(A, B)

    model.construct_line(F, E)
    model.set_section([F, G, E])
    model.set_segment(F, G)
    model.set_segment(G, E)
    model.set_segment(E, F)

    model.construct_line(D, C)
    model.set_section([D, K, C])
    model.set_segment(D, K)
    model.set_segment(K, C)
    model.set_segment(C, D)

    # 2. Perpendiculars GH and GK from G to EF in the respective planes
    model.set_segment(G, H)
    model.set_segment(G, K)

    # Planes through GH, GK; through EF, AB; and through FE, CD
    model.set_polygon([H, G, K])
    model.set_polygon([B, A, E, F])
    model.set_polygon([F, E, C, D])

    return model


if __name__ == "__main__":
    construct_0294_g1()
