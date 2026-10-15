"""Programmatic construction for Book III, Proposition 21 Note 1 (0056.g1).

Alternative proof of Book III, Proposition 21 when the segment BAED is not
greater than a semicircle.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0056_g1() -> Model:
    """Construct the figure for 0056.g1 using geometor.model."""
    model = Model("0056.g1")

    # 1. Circle ABCD about centre F, with segment BAED not greater than a semicircle.
    F = model.set_point(0, 0, classes=["given"], label="F")
    by = sp.Rational(47, 142)
    bx = -sp.sqrt(1 - by**2)
    B = model.set_point(bx, by, classes=["given"], label="B")
    D = model.set_point(-bx, by, classes=["given"], label="D")

    circle_ABCD = model.construct_circle(F, B)

    # Points A, E in segment BAED and C diametrically opposite A
    ax = sp.Rational(-41, 71)
    ay = sp.sqrt(1 - ax**2)
    A = model.set_point(ax, ay, classes=["given"], label="A")
    C = model.set_point(-ax, -ay, label="C")

    ex = sp.Rational(31, 71)
    ey = sp.sqrt(1 - ex**2)
    E = model.set_point(ex, ey, classes=["given"], label="E")

    # 2. Chords AB, AD, EB, ED, BD, diameter AFC, and chord CE (plus auxiliary BC, DC)
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(E, B)
    model.set_segment(E, D)
    model.set_segment(B, D)

    model.set_segment(A, F)
    model.set_segment(F, C)
    model.set_segment(A, C)
    model.set_section([A, F, C])

    model.set_segment(C, E)
    model.set_segment(B, C)
    model.set_segment(D, C)

    model.set_polygon([B, A, D])
    model.set_polygon([B, E, D])

    return model


if __name__ == "__main__":
    construct_0056_g1()
