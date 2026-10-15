"""Programmatic construction for Book XI, Proposition 5 (0285.g1).

If a straight line be set up at right angles to three straight lines which meet
one another, at their common point of section, the three straight lines are in
one plane.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0285_g1() -> Model:
    """Construct the figure for Book XI, Proposition 5 using geometor.model."""
    model = Model("0285.g1")

    # Perspective plane of reference corners
    P1 = model.set_point(sp.Rational(-34, 77), sp.Rational(41, 77), label="P1")
    P2 = model.set_point(sp.Rational(112, 77), sp.Rational(41, 77), label="P2")
    P3 = model.set_point(sp.Rational(100, 77), sp.Rational(-46, 77), label="P3")
    P4 = model.set_point(sp.Rational(-50, 77), sp.Rational(-46, 77), label="P4")

    # 1. Let a straight line AB be set up at right angles to the three straight
    #    lines BC, BD, BE, at their point of meeting at B.
    B = model.set_point(0, 0, classes=["given"], label="B")
    A = model.set_point(0, 1, classes=["given"], label="A")
    C = model.set_point(sp.Rational(40, 77), sp.Rational(66, 77), classes=["given"], label="C")
    D = model.set_point(sp.Rational(79, 77), 0, classes=["given"], label="D")
    E = model.set_point(sp.Rational(40, 77), sp.Rational(-34, 77), classes=["given"], label="E")

    # 2. Let the plane through AB, BC be produced; let it make as common section
    #    in the plane of reference the straight line BF.
    F = model.set_point(sp.Rational(30, 77), sp.Rational(32, 77), label="F")

    # Base segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(B, E)
    model.set_segment(B, F)

    # Plane of reference boundary
    model.set_segment(P1, P2)
    model.set_segment(P2, P3)
    model.set_segment(P3, P4)
    model.set_segment(P4, P1)
    model.set_polygon([P1, P2, P3, P4])

    # Plane through BD, BE and plane through AB, BC
    model.set_polygon([B, D, E])
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, F])

    return model


if __name__ == "__main__":
    construct_0285_g1()
