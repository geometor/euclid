"""Programmatic construction for Book XI, Proposition 7 (0289.g1).

If two straight lines be parallel and points be taken at random on each of them,
the straight line joining the points is in the same plane with the parallel
straight lines.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0289_g1() -> Model:
    """Construct the figure for Book XI, Proposition 7 using geometor.model."""
    model = Model("0289.g1")

    # 1. Let AB, CD be two parallel straight lines, and let points E, F be taken
    #    at random on them respectively.
    A = model.set_point(0, 1, classes=["given"], label="A")
    B = model.set_point(sp.Rational(151, 80), 1, classes=["given"], label="B")
    E = model.set_point(sp.Rational(67, 80), 1, classes=["given"], label="E")

    C = model.set_point(sp.Rational(-16, 80), 0, classes=["given"], label="C")
    D = model.set_point(sp.Rational(160, 80), 0, classes=["given"], label="D")
    F = model.set_point(sp.Rational(94, 80), 0, classes=["given"], label="F")

    # 2. Hypothetical elevated path EGF with point G
    G = model.set_point(sp.Rational(91, 80), sp.Rational(1, 2), label="G")

    # Collinear sections and segments along AB and CD
    model.construct_line(A, B)
    model.set_section([A, E, B])
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(A, B)

    model.construct_line(C, D)
    model.set_section([C, F, D])
    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_segment(C, D)

    # Transversal EF
    model.set_segment(E, F)

    # Plane ABCD
    model.set_polygon([A, B, D, C])

    return model


if __name__ == "__main__":
    construct_0289_g1()
