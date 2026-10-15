"""Programmatic construction for Book III, Proposition 21 Converse (0056.g2).

Converse of Book III, Proposition 21: if two triangles on the same base BC and
on the same side of it have equal vertical angles at A and D, the circle BAC
will pass through D.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0056_g2() -> Model:
    """Construct the figure for 0056.g2 using geometor.model."""
    model = Model("0056.g2")

    # 1. Circle BAC passing through B, C, A, D
    O = model.set_point(0, 0, label="O")
    by = sp.Rational(-32, 69)
    bx = -sp.sqrt(1 - by**2)
    B = model.set_point(bx, by, classes=["given"], label="B")
    C = model.set_point(-bx, by, classes=["given"], label="C")

    dx = sp.Rational(-8, 69)
    dy = sp.sqrt(1 - dx**2)
    D = model.set_point(dx, dy, classes=["given"], label="D")

    ax = sp.Rational(40, 69)
    ay = sp.sqrt(1 - ax**2)
    A = model.set_point(ax, ay, classes=["given"], label="A")

    circle_BAC = model.construct_circle(O, B)

    # 2. Triangles BAC and BDC on base BC, plus supposed point E on BD and chord EC
    t_E = sp.Rational(4, 5)
    E = model.set_point(B.x + t_E * (D.x - B.x), B.y + t_E * (D.y - B.y), label="E")

    model.set_segment(B, C)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(D, C)

    model.set_segment(B, E)
    model.set_segment(E, D)
    model.set_segment(B, D)
    model.set_section([B, E, D])
    model.set_segment(E, C)

    model.set_polygon([B, A, C])
    model.set_polygon([B, D, C])
    model.set_polygon([B, E, C])

    return model


if __name__ == "__main__":
    construct_0056_g2()
