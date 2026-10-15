"""Programmatic construction for Book XI, Proposition 19 Commentary (0309.g1).

Alternative proof of Proposition 19 (Legendre): If two planes be perpendicular
to a third, their intersection is also perpendicular to that third plane.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0309_g1() -> Model:
    """Construct the commentary figure for Book XI, Proposition 19 using geometor.model."""
    model = Model("0309.g1")

    # Plane MN boundary corners
    M1 = model.set_point(sp.Rational(-100, 79), sp.Rational(34, 79), label="M1")
    N = model.set_point(sp.Rational(97, 79), sp.Rational(34, 79), classes=["given"], label="N")
    M2 = model.set_point(sp.Rational(72, 79), sp.Rational(-55, 79), label="M2")
    M = model.set_point(sp.Rational(-125, 79), sp.Rational(-55, 79), classes=["given"], label="M")

    # 1. Let each of the two planes AC, AD intersecting in AB be perpendicular
    #    to the plane MN, intersecting MN in BC, BD respectively.
    B = model.set_point(0, 0, classes=["given"], label="B")
    A = model.set_point(0, 1, classes=["given"], label="A")
    C = model.set_point(sp.Rational(-56, 79), sp.Rational(-26, 79), classes=["given"], label="C")
    D = model.set_point(sp.Rational(39, 79), sp.Rational(-8, 79), classes=["given"], label="D")
    C_top = model.set_point(sp.Rational(-56, 79), sp.Rational(53, 79), label="C_top")
    D_top = model.set_point(sp.Rational(39, 79), sp.Rational(70, 79), label="D_top")

    # 2. In the plane MN draw BE at right angles to BC and BF at right angles to BD.
    F = model.set_point(sp.Rational(-14, 79), sp.Rational(-33, 79), label="F")
    E = model.set_point(sp.Rational(20, 79), sp.Rational(-32, 79), label="E")

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(B, E)
    model.set_segment(B, F)
    model.set_segment(C, C_top)
    model.set_segment(C_top, A)
    model.set_segment(D, D_top)
    model.set_segment(D_top, A)

    # Planes
    model.set_segment(M1, N)
    model.set_segment(N, M2)
    model.set_segment(M2, M)
    model.set_segment(M, M1)
    model.set_polygon([M1, N, M2, M])
    model.set_polygon([A, B, C, C_top])
    model.set_polygon([A, B, D, D_top])

    return model


if __name__ == "__main__":
    construct_0309_g1()
