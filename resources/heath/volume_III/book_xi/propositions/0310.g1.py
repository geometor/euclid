"""Programmatic construction for Book XI, Proposition 19 Lemma 1 (0310.g1).

Given a plane and a straight line not perpendicular to it, one plane, and only
one, can be drawn through the straight line perpendicular to the plane.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0310_g1() -> Model:
    """Construct the Lemma 1 figure for Book XI, Proposition 19 using geometor.model."""
    model = Model("0310.g1")

    # Plane MN boundary corners
    M1 = model.set_point(sp.Rational(-67, 83), sp.Rational(44, 83), label="M1")
    N = model.set_point(sp.Rational(74, 83), sp.Rational(44, 83), classes=["given"], label="N")
    M2 = model.set_point(sp.Rational(46, 83), sp.Rational(-40, 83), label="M2")
    M = model.set_point(sp.Rational(-98, 83), sp.Rational(-40, 83), classes=["given"], label="M")

    # 1. Let AB be the given straight line, MN the given plane.
    # 2. From any point C in AB draw CD perpendicular to the plane MN.
    # 3. Through AB and CD draw a plane AE.
    D = model.set_point(0, 0, classes=["given"], label="D")
    C = model.set_point(0, 1, classes=["given"], label="C")
    A = model.set_point(sp.Rational(-47, 83), sp.Rational(101, 83), classes=["given"], label="A")
    B = model.set_point(sp.Rational(46, 83), sp.Rational(65, 83), classes=["given"], label="B")
    E = model.set_point(sp.Rational(46, 83), sp.Rational(-71, 83), classes=["given"], label="E")
    E_left = model.set_point(sp.Rational(-47, 83), sp.Rational(-71, 83), label="E_left")
    D_left = model.set_point(sp.Rational(-47, 83), 0, label="D_left")
    D_right = model.set_point(sp.Rational(46, 83), 0, label="D_right")

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(C, D)
    model.set_segment(D_left, D_right)

    # Planes
    model.set_segment(M1, N)
    model.set_segment(N, M2)
    model.set_segment(M2, M)
    model.set_segment(M, M1)
    model.set_polygon([M1, N, M2, M])

    model.set_segment(A, E_left)
    model.set_segment(E_left, E)
    model.set_segment(E, B)
    model.set_polygon([A, B, E, E_left])

    return model


if __name__ == "__main__":
    construct_0310_g1()
