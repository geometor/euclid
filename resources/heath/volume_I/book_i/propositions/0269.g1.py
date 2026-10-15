"""Programmatic construction for Book I, Proposition 6 (0269.g1).

If in a triangle two angles be equal to one another, the sides which subtend
the equal angles will also be equal to one another.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0269_g1() -> Model:
    """Construct the figure for Book I, Proposition 6 using geometor.model."""
    model = Model("0269.g1")

    # 1. Let ABC be a triangle having the angle ABC equal to the angle ACB.
    A = model.set_point(58, -24, classes=["given"], label="A")
    B = model.set_point(14, -117, classes=["given"], label="B")
    C = model.set_point(98, -117, classes=["given"], label="C")

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_polygon([A, B, C])

    # 2. From AB the greater let DB be cut off equal to AC the less; let DC be joined.
    D = model.set_point(46, -50, label="D")
    model.set_section([A, D, B])
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(D, C)

    # 3. Triangle DBC compared with triangle ACB
    model.set_polygon([D, B, C])

    return model


if __name__ == "__main__":
    construct_0269_g1()
