"""Programmatic construction for Book I, Proposition 10 Note — Apollonius' Bisection (0282.g1).

Apollonius' bisection of a finite straight line AB by describing two circles with
centres A, B and radii AB, BA intersecting at C and D, and joining CD bisecting AB at E.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0282_g1() -> Model:
    """Construct the figure for 0282.g1 using geometor.model."""
    model = Model("0282.g1")

    # 1. Given straight line AB and circles with centres A, B and radii AB, BA
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(1, 0, classes=["given"], label="B")
    model.set_segment(A, B)

    model.construct_circle(A, B)
    model.construct_circle(B, A)

    # 2. Intersections C and D of the two circles, and midpoint E on AB
    C = model.set_point(sp.Rational(1, 2), sp.sqrt(3) / 2, label="C")
    D = model.set_point(sp.Rational(1, 2), -sp.sqrt(3) / 2, label="D")
    E = model.set_point(sp.Rational(1, 2), 0, label="E")

    model.set_section([A, E, B])
    model.set_segment(A, E)
    model.set_segment(E, B)

    model.set_section([C, E, D])
    model.set_segment(C, E)
    model.set_segment(E, D)
    model.set_segment(C, D)

    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(A, D)
    model.set_segment(D, B)

    # Polygons
    model.set_polygon([A, C, B, D])
    model.set_polygon([A, C, D])
    model.set_polygon([B, C, D])
    model.set_polygon([A, B, C])
    model.set_polygon([A, C, E])
    model.set_polygon([B, C, E])

    return model


if __name__ == "__main__":
    construct_0282_g1()
