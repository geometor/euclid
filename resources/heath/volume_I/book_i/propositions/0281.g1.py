"""Programmatic construction for Book I, Proposition 10 (0281.g1).

To bisect a given finite straight line.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0281_g1() -> Model:
    """Construct the figure for Book I, Proposition 10 using geometor.model."""
    model = Model("0281.g1")

    # 1. Let AB be the given finite straight line.
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(1, 0, classes=["given"], label="B")
    model.set_segment(A, B)

    # 2. Construct equilateral triangle ABC on AB [I. 1]
    C = model.set_point(sp.Rational(1, 2), sp.sqrt(3) / 2, label="C")
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_polygon([A, B, C])

    # 3. Bisect angle ACB by straight line CD meeting AB at D [I. 9]
    D = model.set_point(sp.Rational(1, 2), 0, label="D")
    model.set_section([A, D, B])
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(C, D)

    model.set_polygon([A, C, D])
    model.set_polygon([B, C, D])

    return model


if __name__ == "__main__":
    construct_0281_g1()
