"""Programmatic construction for Book XI, Proposition 18 Commentary (0308.g1).

Alternative proof of Proposition 18 (Legendre): If a straight line be at right
angles to any plane, all the planes through it will also be at right angles to
the same plane.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0308_g1() -> Model:
    """Construct the commentary figure for Book XI, Proposition 18 using geometor.model."""
    model = Model("0308.g1")

    # Plane MN boundary corners
    M1 = model.set_point(sp.Rational(-63, 60), sp.Rational(43, 60), label="M1")
    N = model.set_point(sp.Rational(136, 60), sp.Rational(43, 60), classes=["given"], label="N")
    M2 = model.set_point(sp.Rational(65, 60), sp.Rational(-40, 60), label="M2")
    M = model.set_point(sp.Rational(-134, 60), sp.Rational(-40, 60), classes=["given"], label="M")

    # Plane CE boundary corners
    C1 = model.set_point(sp.Rational(-35, 60), sp.Rational(33, 60), label="C1")
    E = model.set_point(sp.Rational(37, 60), sp.Rational(114, 60), classes=["given"], label="E")
    E2 = model.set_point(sp.Rational(37, 60), sp.Rational(-33, 60), label="E2")
    C2 = model.set_point(sp.Rational(-35, 60), sp.Rational(-113, 60), label="C2")

    # 1. Let AB be perpendicular to the plane MN, and CE any plane through AB,
    #    meeting the plane MN in the straight line CD.
    B = model.set_point(0, 0, classes=["given"], label="B")
    A = model.set_point(0, sp.Rational(52, 60), classes=["given"], label="A")
    C = model.set_point(sp.Rational(-35, 60), sp.Rational(-40, 60), classes=["given"], label="C")
    D = model.set_point(sp.Rational(37, 60), sp.Rational(43, 60), classes=["given"], label="D")

    # 2. In the plane MN draw BF at right angles to CD.
    F = model.set_point(sp.Rational(64, 60), 0, label="F")

    # Segments
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(C, B)
    model.set_segment(B, D)
    model.set_segment(B, F)

    # Plane boundaries
    model.set_segment(M1, N)
    model.set_segment(N, M2)
    model.set_segment(M2, M)
    model.set_segment(M, M1)
    model.set_polygon([M1, N, M2, M])

    model.set_segment(C1, E)
    model.set_segment(E, E2)
    model.set_segment(E2, C2)
    model.set_segment(C2, C1)
    model.set_polygon([C1, E, E2, C2])

    return model


if __name__ == "__main__":
    construct_0308_g1()
