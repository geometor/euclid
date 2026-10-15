"""Programmatic construction for Book XI, Proposition 10 (0295.g1).

If two straight lines meeting one another be parallel to two straight lines
meeting one another not in the same plane, they will contain equal angles.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0295_g1() -> Model:
    """Construct the figure for Book XI, Proposition 10 using geometor.model."""
    model = Model("0295.g1")

    # Upper plane boundary corners
    U1 = model.set_point(sp.Rational(-30, 79), sp.Rational(19, 79), label="U1")
    U2 = model.set_point(sp.Rational(112, 79), sp.Rational(19, 79), label="U2")
    U3 = model.set_point(sp.Rational(68, 79), sp.Rational(-66, 79), label="U3")
    U4 = model.set_point(sp.Rational(-48, 79), sp.Rational(-66, 79), label="U4")

    # Lower plane boundary corners
    L1 = model.set_point(sp.Rational(25, 79), sp.Rational(-92, 79), label="L1")
    L2 = model.set_point(sp.Rational(222, 79), sp.Rational(-92, 79), label="L2")
    L3 = model.set_point(sp.Rational(178, 79), sp.Rational(-167, 79), label="L3")
    L4 = model.set_point(sp.Rational(-1, 79), sp.Rational(-167, 79), label="L4")

    # 1. Let the two straight lines AB, BC meeting one another be parallel to
    #    the two straight lines DE, EF meeting one another, not in the same
    #    plane; and let BA, BC, ED, EF be cut off equal to one another.
    B = model.set_point(0, 0, classes=["given"], label="B")
    A = model.set_point(sp.Rational(-17, 79), sp.Rational(-55, 79), classes=["given"], label="A")
    C = model.set_point(1, sp.Rational(-5, 79), classes=["given"], label="C")

    E = model.set_point(sp.Rational(78, 79), sp.Rational(-102, 79), classes=["given"], label="E")
    D = model.set_point(sp.Rational(62, 79), sp.Rational(-156, 79), classes=["given"], label="D")
    F = model.set_point(sp.Rational(157, 79), sp.Rational(-106, 79), classes=["given"], label="F")

    # 2. Join AD, CF, BE, AC, DF.
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, C)

    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(D, F)

    model.set_segment(A, D)
    model.set_segment(B, E)
    model.set_segment(C, F)

    # Upper and lower plane boundaries
    model.set_polygon([U1, U2, U3, U4])
    model.set_polygon([L1, L2, L3, L4])

    # Triangles and parallelograms in the proof
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([A, B, E, D])
    model.set_polygon([B, C, F, E])
    model.set_polygon([A, C, F, D])

    return model


if __name__ == "__main__":
    construct_0295_g1()
