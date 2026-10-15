"""Programmatic construction for Book XI, Proposition 11 (0296.g1).

From a given elevated point to draw a straight line perpendicular to a given
plane.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0296_g1() -> Model:
    """Construct the figure for Book XI, Proposition 11 using geometor.model."""
    model = Model("0296.g1")

    # Plane of reference boundary corners
    P1 = model.set_point(sp.Rational(-46, 92), sp.Rational(42, 92), label="P1")
    P2 = model.set_point(sp.Rational(113, 92), sp.Rational(42, 92), label="P2")
    P3 = model.set_point(sp.Rational(97, 92), sp.Rational(-57, 92), label="P3")
    P4 = model.set_point(sp.Rational(-58, 92), sp.Rational(-57, 92), label="P4")

    # 1. Given elevated point A and random straight line BC in the plane of
    #    reference; AD drawn perpendicular to BC, DE at right angles to BC in
    #    the plane, AF perpendicular to DE, and GH through F parallel to BC.
    F = model.set_point(0, 0, classes=["given"], label="F")
    A = model.set_point(0, 1, classes=["given"], label="A")
    D = model.set_point(sp.Rational(61, 92), sp.Rational(-24, 92), label="D")
    E = model.set_point(sp.Rational(-36, 92), sp.Rational(15, 92), label="E")

    B = model.set_point(sp.Rational(25, 92), sp.Rational(-43, 92), label="B")
    C = model.set_point(sp.Rational(95, 92), sp.Rational(-6, 92), label="C")

    G = model.set_point(sp.Rational(-31, 92), sp.Rational(-17, 92), label="G")
    H = model.set_point(sp.Rational(60, 92), sp.Rational(32, 92), label="H")

    # Collinear lines and sub-segments
    model.construct_line(B, C)
    model.set_section([B, D, C])
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(B, C)

    model.construct_line(E, D)
    model.set_section([E, F, D])
    model.set_segment(E, F)
    model.set_segment(F, D)
    model.set_segment(D, E)

    model.construct_line(G, H)
    model.set_section([G, F, H])
    model.set_segment(G, F)
    model.set_segment(F, H)
    model.set_segment(G, H)

    # Perpendiculars AD and AF
    model.set_segment(A, D)
    model.set_segment(A, F)

    # Planes
    model.set_polygon([P1, P2, P3, P4])
    model.set_polygon([A, D, E])

    return model


if __name__ == "__main__":
    construct_0296_g1()
