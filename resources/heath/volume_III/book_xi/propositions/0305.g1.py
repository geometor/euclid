"""Programmatic construction for Book XI, Proposition 16 Commentary (0305.g1).

If a straight line is perpendicular to one of two parallel planes, it is
perpendicular to the other also.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0305_g1() -> Model:
    """Construct the figure for 0305.g1 using geometor.model."""
    model = Model("0305.g1")

    # 1. Suppose MN, PQ are two parallel planes, and AB is perpendicular to MN.
    A = model.set_point(0, 1, classes=["given"], label="A")
    B = model.set_point(0, 0, classes=["given"], label="B")

    # 2. Through AB draw any plane intersecting MN, PQ in AC, BD respectively.
    C = model.set_point(sp.Rational(50, 69), sp.Rational(74, 69), label="C")
    D = model.set_point(sp.Rational(50, 69), sp.Rational(5, 69), label="D")

    # Plane MN corners
    M1 = model.set_point(sp.Rational(-17, 69), sp.Rational(103, 69), label="M1")
    N = model.set_point(sp.Rational(76, 69), sp.Rational(79, 69), classes=["given"], label="N")
    M3 = model.set_point(sp.Rational(46, 69), sp.Rational(32, 69), label="M3")
    M = model.set_point(sp.Rational(-47, 69), sp.Rational(54, 69), classes=["given"], label="M")

    # Plane PQ corners
    P1 = model.set_point(sp.Rational(-7, 69), sp.Rational(32, 69), label="P1")
    Q = model.set_point(sp.Rational(97, 69), sp.Rational(8, 69), classes=["given"], label="Q")
    P3 = model.set_point(sp.Rational(71, 69), sp.Rational(-36, 69), label="P3")
    P = model.set_point(sp.Rational(-33, 69), sp.Rational(-9, 69), classes=["given"], label="P")

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, D)

    # Planes
    model.set_polygon([M1, N, M3, M])
    model.set_polygon([P1, Q, P3, P])
    model.set_polygon([A, C, D, B])

    return model


if __name__ == "__main__":
    construct_0305_g1()
