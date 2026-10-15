"""Programmatic construction for Book XI, Proposition 21 (0313.g1).

Any solid angle is contained by plane angles less than four right angles.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0313_g1() -> Model:
    """Construct the figure for Book XI, Proposition 21 using geometor.model."""
    model = Model("0313.g1")

    # 1. Let the angle at A be a solid angle contained by the plane angles
    #    BAC, CAD, DAB.
    # 2. Take points B, C, D at random on AB, AC, AD and join BC, CD, DB.
    A = model.set_point(0, 0, classes=["given"], label="A")
    C = model.set_point(sp.Rational(-24, 60), sp.Rational(45, 60), classes=["given"], label="C")
    B = model.set_point(sp.Rational(-78, 60), sp.Rational(-69, 60), classes=["given"], label="B")
    D = model.set_point(sp.Rational(110, 60), sp.Rational(-25, 60), classes=["given"], label="D")

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, B)

    # Triangles
    model.set_polygon([A, B, C])
    model.set_polygon([A, C, D])
    model.set_polygon([A, D, B])
    model.set_polygon([B, C, D])

    return model


if __name__ == "__main__":
    construct_0313_g1()
