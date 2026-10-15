"""Programmatic construction for Book XI, Proposition 15 Commentary 4 (0303.g2).

If two straight lines forming an angle are respectively parallel to two other
straight lines forming an angle, the plane of the first angle is parallel to the
plane of the second.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0303_g2() -> Model:
    """Construct the figure for 0303.g2 using geometor.model."""
    model = Model("0303.g2")

    # 1. Let ABC, DEF be the angles formed by straight lines parallel to one another.
    B = model.set_point(0, 1, classes=["given"], label="B")
    A = model.set_point(sp.Rational(62, 76), sp.Rational(94, 76), classes=["given"], label="A")
    C = model.set_point(sp.Rational(32, 76), sp.Rational(71, 76), classes=["given"], label="C")

    E = model.set_point(sp.Rational(31, 76), 0, classes=["given"], label="E")
    D = model.set_point(sp.Rational(89, 76), sp.Rational(16, 76), classes=["given"], label="D")
    F = model.set_point(sp.Rational(102, 76), sp.Rational(-11, 76), classes=["given"], label="F")

    # Upper plane corners
    P1 = model.set_point(0, sp.Rational(106, 76), label="P1")
    P2 = model.set_point(sp.Rational(95, 76), sp.Rational(106, 76), label="P2")
    P3 = model.set_point(sp.Rational(55, 76), sp.Rational(60, 76), label="P3")
    P4 = model.set_point(sp.Rational(-41, 76), sp.Rational(60, 76), label="P4")

    # Lower plane corners
    Q1 = model.set_point(sp.Rational(30, 76), sp.Rational(28, 76), label="Q1")
    Q2 = model.set_point(sp.Rational(142, 76), sp.Rational(28, 76), label="Q2")
    Q3 = model.set_point(sp.Rational(107, 76), sp.Rational(-14, 76), label="Q3")
    Q4 = model.set_point(sp.Rational(-7, 76), sp.Rational(-14, 76), label="Q4")

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(D, E)
    model.set_segment(E, F)

    # Planes
    model.set_polygon([P1, P2, P3, P4])
    model.set_polygon([Q1, Q2, Q3, Q4])
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])

    # Wedges for angles ABC and DEF
    model.set_wedge(B, A, A, C)
    model.set_wedge(E, D, D, F)

    return model


if __name__ == "__main__":
    construct_0303_g2()
