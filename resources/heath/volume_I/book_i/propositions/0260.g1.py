"""Programmatic construction for Book I, Proposition 3 (0260.g1).

Given two unequal straight lines, to cut off from the greater a straight line
equal to the less.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0260_g1() -> Model:
    """Construct the figure for Book I, Proposition 3 using geometor.model."""
    model = Model("0260.g1")

    # 1. Let AB, C be the two given unequal straight lines, and let AB be the greater.
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(3, 0, classes=["given"], label="B")
    model.set_segment(A, B)

    # Standalone given straight line C (of length 2)
    C_start = model.set_point(-sp.Rational(1, 2), sp.Rational(5, 2), classes=["given"])
    C_end = model.set_point(sp.Rational(3, 2), sp.Rational(5, 2), classes=["given"], label="C")
    model.set_segment(C_start, C_end)

    # 2. At the point A let AD be placed equal to the straight line C [I. 2]
    D = model.set_point(-sp.Rational(8, 5), sp.Rational(6, 5), label="D")
    model.set_segment(A, D)

    # 3. With centre A and distance AD let the circle DEF be described [Post. 3]
    model.construct_circle(A, D)

    # Circumference point F and intersection point E on AB
    E = model.set_point(2, 0, label="E")
    F = model.set_point(sp.Rational(6, 5), -sp.Rational(8, 5), label="F")

    # 4. Cut-off segment AE and remainder EB along AB
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_section([A, E, B])

    return model


if __name__ == "__main__":
    construct_0260_g1()
