"""Programmatic construction for Book XI, Proposition 15 Commentary 3 (0303.g1).

If each of two intersecting straight lines is parallel to a given plane, the
plane containing them is parallel to the given plane.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0303_g1() -> Model:
    """Construct the figure for 0303.g1 using geometor.model."""
    model = Model("0303.g1")

    # 1. Let AB, AC be parallel to the plane MN.
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(sp.Rational(83, 112), sp.Rational(29, 112), classes=["given"], label="B")
    C = model.set_point(1, sp.Rational(-10, 112), classes=["given"], label="C")

    # Plane MN corners
    M1 = model.set_point(sp.Rational(-50, 112), sp.Rational(-30, 112), label="M1")
    N = model.set_point(sp.Rational(132, 112), sp.Rational(-30, 112), classes=["given"], label="N")
    M3 = model.set_point(sp.Rational(120, 112), sp.Rational(-94, 112), label="M3")
    M = model.set_point(sp.Rational(-62, 112), sp.Rational(-94, 112), classes=["given"], label="M")

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)

    # Planes
    model.set_polygon([A, B, C])
    model.set_polygon([M1, N, M3, M])

    return model


if __name__ == "__main__":
    construct_0303_g1()
