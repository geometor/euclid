"""Programmatic construction for Book XI, Proposition 19 (0308.g2).

If two planes which cut one another be at right angles to any plane, their
common section will also be at right angles to the same plane.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0308_g2() -> Model:
    """Construct the figure for Book XI, Proposition 19 using geometor.model."""
    model = Model("0308.g2")

    # Plane of reference boundary corners
    P1 = model.set_point(sp.Rational(-83, 91), sp.Rational(45, 91), label="P1")
    P2 = model.set_point(sp.Rational(81, 91), sp.Rational(45, 91), label="P2")
    P3 = model.set_point(sp.Rational(48, 91), sp.Rational(-55, 91), label="P3")
    P4 = model.set_point(sp.Rational(-106, 91), sp.Rational(-55, 91), label="P4")

    # 1. Let the two planes AB, BC be at right angles to the plane of reference,
    #    and let BD be their common section.
    D = model.set_point(0, 0, classes=["given"], label="D")
    B = model.set_point(0, 1, classes=["given"], label="B")
    A = model.set_point(sp.Rational(-63, 91), sp.Rational(-55, 91), classes=["given"], label="A")
    C = model.set_point(sp.Rational(34, 91), sp.Rational(-55, 91), classes=["given"], label="C")

    # Outer corners of planes AB and BC
    A_top = model.set_point(sp.Rational(-63, 91), sp.Rational(57, 91), label="A_top")
    B_right_top = model.set_point(sp.Rational(53, 91), sp.Rational(119, 91), label="B_right_top")
    B_right_bot = model.set_point(sp.Rational(53, 91), sp.Rational(45, 91), label="B_right_bot")

    C_top = model.set_point(sp.Rational(34, 91), sp.Rational(54, 91), label="C_top")
    B_left_top = model.set_point(sp.Rational(-25, 91), sp.Rational(119, 91), label="B_left_top")
    B_left_bot = model.set_point(sp.Rational(-25, 91), sp.Rational(53, 91), label="B_left_bot")

    # 2. From D let DE be drawn in plane AB at right angles to AD, and DF in
    #    plane BC at right angles to CD.
    E = model.set_point(sp.Rational(-16, 91), sp.Rational(53, 91), label="E")
    F = model.set_point(sp.Rational(9, 91), sp.Rational(57, 91), label="F")

    # Segments
    model.set_segment(B, D)
    model.set_segment(A, D)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(A, B_right_bot)

    # Plane boundaries and polygons
    model.set_segment(P1, P2)
    model.set_segment(P2, P3)
    model.set_segment(P3, P4)
    model.set_segment(P4, P1)
    model.set_polygon([P1, P2, P3, P4])

    model.set_polygon([A, A_top, B_right_top, B_right_bot])
    model.set_polygon([C, C_top, B_left_top, B_left_bot, D])

    return model


if __name__ == "__main__":
    construct_0308_g2()
