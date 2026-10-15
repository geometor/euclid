"""Programmatic construction for Book III, Proposition 21 (0055.g1).

In a circle the angles in the same segment are equal to one another.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0055_g1() -> Model:
    """Construct the figure for Book III, Proposition 21 using geometor.model."""
    model = Model("0055.g1")

    # 1. Circle ABCD about centre F
    F = model.set_point(0, 0, classes=["given"], label="F")
    C = model.set_point(0, -1, label="C")
    circle_ABCD = model.construct_circle(F, C)

    # Points B, D, A, E on circumference
    bx = sp.Rational(-61, 82)
    by = -sp.sqrt(1 - bx**2)
    B = model.set_point(bx, by, classes=["given"], label="B")
    D = model.set_point(-bx, by, classes=["given"], label="D")

    ax = sp.Rational(-33, 82)
    ay = sp.sqrt(1 - ax**2)
    A = model.set_point(ax, ay, classes=["given"], label="A")

    ey = sp.Rational(12, 82)
    ex = sp.sqrt(1 - ey**2)
    E = model.set_point(ex, ey, classes=["given"], label="E")

    # 2. Chords AB, AD, EB, ED, BD and radii BF, FD
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(E, B)
    model.set_segment(E, D)
    model.set_segment(B, D)
    model.set_segment(B, F)
    model.set_segment(F, D)

    model.set_polygon([B, A, D])
    model.set_polygon([B, E, D])
    model.set_polygon([B, F, D])

    return model


if __name__ == "__main__":
    construct_0055_g1()
