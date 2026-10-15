"""Programmatic construction for Book XI, Proposition 12 (0298.g1).

To set up a straight line at right angles to a given plane from a given point
in it.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0298_g1() -> Model:
    """Construct the figure for Book XI, Proposition 12 using geometor.model."""
    model = Model("0298.g1")

    # Plane of reference boundary corners
    P1 = model.set_point(sp.Rational(-23, 107), sp.Rational(55, 107), label="P1")
    P2 = model.set_point(sp.Rational(112, 107), sp.Rational(56, 107), label="P2")
    P3 = model.set_point(sp.Rational(77, 107), sp.Rational(-27, 107), label="P3")
    P4 = model.set_point(sp.Rational(-42, 107), sp.Rational(-28, 107), label="P4")

    # 1. Given point A in the plane of reference, and elevated point B;
    #    BC drawn perpendicular to the plane, and AD drawn parallel to BC.
    A = model.set_point(0, 0, classes=["given"], label="A")
    D = model.set_point(0, 1, label="D")
    C = model.set_point(sp.Rational(76, 107), sp.Rational(28, 107), label="C")
    B = model.set_point(sp.Rational(75, 107), sp.Rational(112, 107), classes=["given"], label="B")

    model.set_segment(A, D)
    model.set_segment(B, C)

    model.set_segment(P1, P2)
    model.set_segment(P2, P3)
    model.set_segment(P3, P4)
    model.set_segment(P4, P1)
    model.set_polygon([P1, P2, P3, P4])

    return model


if __name__ == "__main__":
    construct_0298_g1()
