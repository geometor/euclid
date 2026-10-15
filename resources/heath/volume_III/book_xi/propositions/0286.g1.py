"""Programmatic construction for Book XI, Proposition 5 Note (0286.g1).

At any point O in a straight line AO it is possible to draw only one plane
which is at right angles to the straight line.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0286_g1() -> Model:
    """Construct the figure for Book XI, Proposition 5 note (0286.g1) using geometor.model."""
    model = Model("0286.g1")

    # 1. Given straight line AO and point O on it.
    O = model.set_point(0, 0, classes=["given"], label="O")
    A = model.set_point(0, 1, classes=["given"], label="A")

    # 2. Perpendiculars BO, CO in the planes AOB, AOC, each perpendicular to AO.
    B = model.set_point(sp.Rational(-67, 56), sp.Rational(-23, 56), classes=["given"], label="B")
    C = model.set_point(sp.Rational(59, 56), sp.Rational(-14, 56), classes=["given"], label="C")

    # 3. Hypothetical second perpendicular OC' in the plane AOC.
    Cp = model.set_point(sp.Rational(80, 56), sp.Rational(-4, 56), label="C'")

    # Lines and segments
    model.construct_line(A, O)
    model.construct_line(O, B)
    model.construct_line(O, C)

    model.set_segment(A, O)
    model.set_segment(B, O)
    model.set_segment(C, O)
    model.set_segment(O, Cp)
    model.set_segment(A, B)
    model.set_segment(A, C)

    # Planes AOB, AOC, BOC, AOC'
    model.set_polygon([A, O, B])
    model.set_polygon([A, O, C])
    model.set_polygon([B, O, C])
    model.set_polygon([A, O, Cp])

    return model


if __name__ == "__main__":
    construct_0286_g1()
