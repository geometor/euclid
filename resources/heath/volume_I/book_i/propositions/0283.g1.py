"""Programmatic construction for Book I, Proposition 11 (0283.g1).

To draw a straight line at right angles to a given straight line from a given
point on it.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0283_g1() -> Model:
    """Construct the figure for Book I, Proposition 11 using geometor.model."""
    model = Model("0283.g1")

    # 1. Given straight line AB and given point C on it
    A = model.set_point(-sp.Rational(3, 2), 0, classes=["given"], label="A")
    B = model.set_point(sp.Rational(3, 2), 0, classes=["given"], label="B")
    C = model.set_point(0, 0, classes=["given"], label="C")
    model.construct_line(A, B)

    # 2. Take point D at random on AC, and make CE equal to CD [I. 3]
    D = model.set_point(-1, 0, label="D")
    E = model.set_point(1, 0, label="E")

    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(A, C)
    model.set_segment(C, E)
    model.set_segment(E, B)
    model.set_segment(C, B)
    model.set_segment(D, E)
    model.set_segment(A, B)

    # 3. Construct equilateral triangle FDE on DE [I. 1] and join FC
    F = model.set_point(0, sp.sqrt(3), label="F")
    model.set_segment(D, F)
    model.set_segment(E, F)
    model.set_segment(F, C)

    model.set_polygon([F, D, E])
    model.set_polygon([D, F, C])
    model.set_polygon([E, F, C])

    return model


if __name__ == "__main__":
    construct_0283_g1()
