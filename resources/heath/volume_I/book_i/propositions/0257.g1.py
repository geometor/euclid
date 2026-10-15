"""Programmatic construction for Book I, Proposition 1 Note — Isosceles Triangle (0257.g1).

Proclus' construction of an isosceles triangle with each of two sides double of the third side.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0257_g1() -> Model:
    """Construct Proclus' isosceles triangle figure (0257.g1) using geometor.model."""
    model = Model("0257.g1")

    # 1. Given finite straight line AB
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(1, 0, classes=["given"], label="B")
    model.set_segment(A, B)

    # 2. Inner circles with centres A, B and radii AB, BA meeting at C
    model.construct_circle(A, B)
    model.construct_circle(B, A)
    C = model.set_point(sp.Rational(1, 2), sp.sqrt(3) / 2, label="C")

    # 3. Produce AB in both directions [ D E ] to meet the respective inner circles in D, E
    model.construct_line(A, B)
    D = model.set_point(-1, 0, label="D")
    E = model.set_point(2, 0, label="E")

    # Sub-segments and radii along the produced line DE
    model.set_segment(D, A)
    model.set_segment(B, E)
    model.set_segment(A, E)
    model.set_segment(B, D)
    model.set_segment(D, E)

    # 4. Describe outer circles with A, B as centres and AE, BD as radii respectively
    model.construct_circle(A, E)
    model.construct_circle(B, D)

    # 5. Upper intersection F of outer circles ( A E ) and ( B D )
    F = model.set_point(sp.Rational(1, 2), sp.sqrt(15) / 2, label="F")

    # Join FA, FB to form the isosceles triangle FAB (with FA = FB = 2 * AB)
    model.set_segment(F, A)
    model.set_segment(F, B)
    model.set_polygon([F, A, B])

    return model


if __name__ == "__main__":
    construct_0257_g1()
