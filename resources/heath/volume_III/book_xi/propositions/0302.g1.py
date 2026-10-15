"""Programmatic construction for Book XI, Proposition 15 Commentary 1 (0302.g1).

Any plane containing one, and only one, of two parallel straight lines is
parallel to the other.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0302_g1() -> Model:
    """Construct the figure for 0302.g1 using geometor.model."""
    model = Model("0302.g1")

    # 1. Suppose AB, CD to be parallel and CD to lie in the plane MN.
    C = model.set_point(0, 0, classes=["given"], label="C")
    D = model.set_point(1, 0, classes=["given"], label="D")
    A = model.set_point(sp.Rational(13, 122), sp.Rational(54, 122), classes=["given"], label="A")
    B = model.set_point(sp.Rational(135, 122), sp.Rational(54, 122), classes=["given"], label="B")

    # Plane MN corners
    M = model.set_point(sp.Rational(-36, 122), sp.Rational(-10, 122), classes=["given"], label="M")
    M2 = model.set_point(sp.Rational(29, 122), sp.Rational(44, 122), label="M2")
    N = model.set_point(sp.Rational(173, 122), sp.Rational(-2, 122), classes=["given"], label="N")
    M4 = model.set_point(sp.Rational(99, 122), sp.Rational(-58, 122), label="M4")

    # Segments
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(A, C)
    model.set_segment(B, D)

    # Planes
    model.set_polygon([A, B, D, C])
    model.set_polygon([M, M2, N, M4])

    return model


if __name__ == "__main__":
    construct_0302_g1()
