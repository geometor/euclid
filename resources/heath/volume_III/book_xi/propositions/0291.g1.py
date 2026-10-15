"""Programmatic construction for Book XI, Proposition 8 (0291.g1).

If two straight lines be parallel, and one of them be at right angles to any
plane, the remaining one will also be at right angles to the same plane.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0291_g1() -> Model:
    """Construct the figure for Book XI, Proposition 8 using geometor.model."""
    model = Model("0291.g1")

    # Plane of reference boundary corners
    P1 = model.set_point(sp.Rational(-20, 102), sp.Rational(45, 102), label="P1")
    P2 = model.set_point(sp.Rational(148, 102), sp.Rational(45, 102), label="P2")
    P3 = model.set_point(sp.Rational(101, 102), sp.Rational(-56, 102), label="P3")
    P4 = model.set_point(sp.Rational(-39, 102), sp.Rational(-56, 102), label="P4")

    # 1. Let AB, CD be two parallel straight lines, and let AB be at right
    #    angles to the plane of reference, meeting it at B, D.
    B = model.set_point(0, 0, classes=["given"], label="B")
    A = model.set_point(0, 1, classes=["given"], label="A")
    D = model.set_point(sp.Rational(100, 102), 0, classes=["given"], label="D")
    C = model.set_point(sp.Rational(100, 102), sp.Rational(100, 102), classes=["given"], label="C")

    # 2. Let BD be joined, and let DE be drawn in the plane of reference at
    #    right angles to BD, with DE equal to AB.
    E = model.set_point(sp.Rational(85, 102), sp.Rational(-42, 102), label="E")

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

    # Planes and triangles in the proof
    model.set_polygon([A, B, D])
    model.set_polygon([E, D, B])
    model.set_polygon([A, B, E])
    model.set_polygon([E, D, A])
    model.set_polygon([A, B, D, C])

    return model


if __name__ == "__main__":
    construct_0291_g1()
