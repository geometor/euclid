"""Programmatic construction for Book XI, Proposition 6 (0287.g1).

If two straight lines be at right angles to the same plane, the straight lines
will be parallel.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0287_g1() -> Model:
    """Construct the figure for Book XI, Proposition 6 using geometor.model."""
    model = Model("0287.g1")

    # Perspective plane of reference corners
    P1 = model.set_point(sp.Rational(-112, 77), sp.Rational(34, 77), label="P1")
    P2 = model.set_point(sp.Rational(47, 77), sp.Rational(35, 77), label="P2")
    P3 = model.set_point(sp.Rational(6, 77), sp.Rational(-53, 77), label="P3")
    P4 = model.set_point(sp.Rational(-129, 77), sp.Rational(-53, 77), label="P4")

    # 1. Let the two straight lines AB, CD be at right angles to the plane of
    #    reference, meeting it at the points B, D.
    B = model.set_point(0, 0, classes=["given"], label="B")
    A = model.set_point(0, 1, classes=["given"], label="A")
    D = model.set_point(sp.Rational(-85, 77), sp.Rational(-14, 77), classes=["given"], label="D")
    C = model.set_point(sp.Rational(-86, 77), sp.Rational(75, 77), classes=["given"], label="C")

    # 2. Let BD be joined, and let DE be drawn in the plane of reference at
    #    right angles to BD, with DE made equal to AB.
    E = model.set_point(sp.Rational(-70, 77), sp.Rational(-42, 77), label="E")

    # 3. Join BE, AE, AD.
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(B, D)
    model.set_segment(D, E)
    model.set_segment(B, E)
    model.set_segment(A, E)
    model.set_segment(A, D)

    # Plane of reference boundary
    model.set_segment(P1, P2)
    model.set_segment(P2, P3)
    model.set_segment(P3, P4)
    model.set_segment(P4, P1)
    model.set_polygon([P1, P2, P3, P4])

    # Triangles and planes compared in the proof
    model.set_polygon([A, B, D])
    model.set_polygon([E, D, B])
    model.set_polygon([A, B, E])
    model.set_polygon([E, D, A])
    model.set_polygon([B, D, A, C])

    return model


if __name__ == "__main__":
    construct_0287_g1()
