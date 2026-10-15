"""Programmatic construction for Book III, Proposition 19 (0051.g1).

If a straight line touch a circle, and from the point of contact a straight
line be drawn at right angles to the tangent, the centre of the circle will be
on the straight line so drawn.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0051_g1() -> Model:
    """Construct the figure for Book III, Proposition 19 using geometor.model."""
    model = Model("0051.g1")

    # 1. Circle ABC touched by straight line DE at C, and CA drawn at right angles to DE.
    O = model.set_point(0, 0, label="O")
    C = model.set_point(0, -1, classes=["given"], label="C")
    A = model.set_point(0, 1, classes=["given"], label="A")
    B = model.set_point(sp.Rational(60, 61), sp.Rational(11, 61), label="B")

    circle_ABC = model.construct_circle(O, C)

    D = model.set_point(sp.Rational(-43, 40), -1, label="D")
    E = model.set_point(sp.Rational(109, 80), -1, label="E")

    line_DE = model.construct_line(D, E)
    model.set_segment(D, C)
    model.set_segment(C, E)
    model.set_segment(D, E)
    model.set_section([D, C, E])

    model.set_segment(C, A)

    # 2. Reductio: suppose F is the centre, and join CF.
    F = model.set_point(sp.Rational(13, 40), sp.Rational(3, 40), label="F")
    model.set_segment(C, F)

    return model


if __name__ == "__main__":
    construct_0051_g1()
