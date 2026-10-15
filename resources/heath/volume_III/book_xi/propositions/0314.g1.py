"""Programmatic construction for Book XI, Proposition 21 Commentary (0314.g1).

Extension of Proposition 21 to any convex polyhedral angle with vertex V cut by
a plane in polygon ABCDE, with interior point O.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0314_g1() -> Model:
    """Construct the convex polyhedral angle figure for Book XI, Proposition 21 using geometor.model."""
    model = Model("0314.g1")

    # 1. Convex polyhedral angle with vertex V cut by a plane in polygon ABCDE,
    #    with interior point O.
    O = model.set_point(0, 0, classes=["given"], label="O")
    V = model.set_point(sp.Rational(12, 102), 1, classes=["given"], label="V")
    A = model.set_point(sp.Rational(-72, 102), sp.Rational(-8, 102), classes=["given"], label="A")
    B = model.set_point(sp.Rational(-34, 102), sp.Rational(-35, 102), classes=["given"], label="B")
    C = model.set_point(sp.Rational(34, 102), sp.Rational(-47, 102), classes=["given"], label="C")
    D = model.set_point(sp.Rational(98, 102), sp.Rational(16, 102), classes=["given"], label="D")
    E = model.set_point(sp.Rational(15, 102), sp.Rational(38, 102), classes=["given"], label="E")

    # Edges from V
    model.set_segment(V, A)
    model.set_segment(V, B)
    model.set_segment(V, C)
    model.set_segment(V, D)
    model.set_segment(V, E)

    # Polygon ABCDE edges
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, A)

    # Segments from O
    model.set_segment(O, A)
    model.set_segment(O, B)
    model.set_segment(O, C)
    model.set_segment(O, D)
    model.set_segment(O, E)

    # Polygons and faces
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([V, A, B])
    model.set_polygon([V, B, C])
    model.set_polygon([V, C, D])
    model.set_polygon([V, D, E])
    model.set_polygon([V, E, A])
    model.set_polygon([O, A, B])
    model.set_polygon([O, B, C])
    model.set_polygon([O, C, D])
    model.set_polygon([O, D, E])
    model.set_polygon([O, E, A])

    return model


if __name__ == "__main__":
    construct_0314_g1()
