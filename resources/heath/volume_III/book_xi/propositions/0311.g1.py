"""Programmatic construction for Book XI, Proposition 19 Rausenberger's Construction (0311.g1).

Draw through each straight line a plane parallel to the other, then through each
straight line a plane perpendicular to the plane through the other; their
intersection is the common perpendicular.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0311_g1() -> Model:
    """Construct Rausenberger's figure for Book XI, Proposition 19 using geometor.model."""
    model = Model("0311.g1")

    # Upper plane boundary (through AB)
    U1 = model.set_point(sp.Rational(-33, 88), sp.Rational(126, 88), label="U1")
    U2 = model.set_point(sp.Rational(101, 88), sp.Rational(126, 88), label="U2")
    U3 = model.set_point(sp.Rational(63, 88), sp.Rational(64, 88), label="U3")
    U4 = model.set_point(sp.Rational(-72, 88), sp.Rational(64, 88), label="U4")

    # Lower plane boundary (through CD)
    L1 = model.set_point(sp.Rational(-33, 88), sp.Rational(33, 88), label="L1")
    L2 = model.set_point(sp.Rational(104, 88), sp.Rational(33, 88), label="L2")
    L3 = model.set_point(sp.Rational(69, 88), sp.Rational(-23, 88), label="L3")
    L4 = model.set_point(sp.Rational(-73, 88), sp.Rational(-23, 88), label="L4")

    # Given skew lines AB and CD
    A = model.set_point(sp.Rational(-46, 88), 1, classes=["given"], label="A")
    B = model.set_point(sp.Rational(74, 88), 1, classes=["given"], label="B")
    C = model.set_point(sp.Rational(-9, 88), sp.Rational(26, 88), classes=["given"], label="C")
    D = model.set_point(sp.Rational(8, 88), sp.Rational(-19, 88), classes=["given"], label="D")

    # Common perpendicular endpoints
    P = model.set_point(0, 1, label="P")
    Q = model.set_point(0, 0, label="Q")

    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(P, Q)

    model.set_polygon([U1, U2, U3, U4])
    model.set_polygon([L1, L2, L3, L4])

    return model


if __name__ == "__main__":
    construct_0311_g1()
