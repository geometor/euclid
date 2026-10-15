"""Programmatic construction for Book XI, Proposition 15 Commentary 2 (0302.g2).

If a straight line is parallel to a plane, it is also parallel to the
intersection of any plane through it with the given plane.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0302_g2() -> Model:
    """Construct the figure for 0302.g2 using geometor.model."""
    model = Model("0302.g2")

    # 1. Let AB be parallel to the plane MN, and let any plane through AB
    #    intersect MN in CD.
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(sp.Rational(25, 107), sp.Rational(48, 107), classes=["given"], label="B")
    C = model.set_point(1, sp.Rational(-55, 107), label="C")
    D = model.set_point(sp.Rational(132, 107), sp.Rational(-6, 107), label="D")

    # Plane MN corners
    M1 = model.set_point(sp.Rational(16, 107), sp.Rational(10, 107), label="M1")
    N = model.set_point(sp.Rational(163, 107), sp.Rational(10, 107), classes=["given"], label="N")
    M3 = model.set_point(sp.Rational(139, 107), sp.Rational(-71, 107), label="M3")
    M = model.set_point(sp.Rational(-9, 107), sp.Rational(-71, 107), classes=["given"], label="M")

    # Segments
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(A, C)
    model.set_segment(B, D)

    # Planes
    model.set_polygon([A, B, D, C])
    model.set_polygon([M1, N, M3, M])

    return model


if __name__ == "__main__":
    construct_0302_g2()
