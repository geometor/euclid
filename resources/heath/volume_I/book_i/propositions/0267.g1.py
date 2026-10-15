"""Programmatic construction for Book I, Proposition 5 Note — Aristotle's Pre-Euclidean Proof (0267.g1).

Aristotle's reference (Anal. Prior. I. 24, 41 b 13-22) to a pre-Euclidean proof of I. 5
using the mixed angles of a semicircle and of a segment of a circle.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0267_g1() -> Model:
    """Construct Aristotle's pre-Euclidean proof diagram (0267.g1) using geometor.model."""
    model = Model("0267.g1")

    # 1. Circle with centre O and radii OA, OB drawn to the base endpoints A, B
    O = model.set_point(0, 0, classes=["given"], label="O")
    A = model.set_point(-sp.Rational(71, 78), -sp.Rational(33, 78), classes=["given"], label="A")
    B = model.set_point(sp.Rational(71, 78), -sp.Rational(33, 78), classes=["given"], label="B")

    # Circle ( O A ) and extended diameter lines [ O A ] and [ O B ]
    model.construct_circle(O, A)
    model.construct_line(O, A)
    model.construct_line(O, B)

    # Radii OA, OB and chord/base AB of the isosceles triangle OAB
    model.set_segment(O, A)
    model.set_segment(O, B)
    model.set_segment(A, B)
    model.set_polygon([O, A, B])

    return model


if __name__ == "__main__":
    construct_0267_g1()
