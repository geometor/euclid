"""Programmatic construction for Book XI, Proposition 5 Note (0286.g2).

One plane and only one can be drawn through a point P outside a straight line
AB at right angles to that line.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0286_g2() -> Model:
    """Construct the figure for Book XI, Proposition 5 note (0286.g2) using geometor.model."""
    model = Model("0286.g2")

    # 1. Given straight line AB and external point P.
    O = model.set_point(0, 0, classes=["given"], label="O")
    A = model.set_point(0, 1, classes=["given"], label="A")
    B = model.set_point(0, sp.Rational(-61, 55), classes=["given"], label="B")
    P = model.set_point(sp.Rational(-74, 55), sp.Rational(-15, 55), classes=["given"], label="P")

    # 2. Through O draw OQ at right angles to AB.
    Q = model.set_point(sp.Rational(57, 55), sp.Rational(-18, 55), label="Q")

    # Collinear line AB with O
    model.construct_line(A, B)
    model.set_section([A, O, B])
    model.set_segment(A, O)
    model.set_segment(O, B)
    model.set_segment(A, B)

    # Perpendiculars PO and OQ
    model.set_segment(P, O)
    model.set_segment(O, Q)

    # Planes through P, AB and through OP, OQ
    model.set_polygon([P, A, B])
    model.set_polygon([O, P, Q])

    return model


if __name__ == "__main__":
    construct_0286_g2()
