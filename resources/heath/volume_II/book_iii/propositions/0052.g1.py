"""Programmatic construction for Book III, Proposition 20 (0052.g1).

In a circle the angle at the centre is double of the angle at the circumference,
when the angles have the same circumference as base.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0052_g1() -> Model:
    """Construct the figure for Book III, Proposition 20 using geometor.model."""
    model = Model("0052.g1")

    # 1. Circle ABC about centre E.
    E = model.set_point(0, 0, classes=["given"], label="E")
    C = model.set_point(1, 0, classes=["given"], label="C")
    circle_ABC = model.construct_circle(E, C)

    # Points A, B, D on circumference and antipodal points F, G
    A = model.set_point(sp.Rational(-60, 61), sp.Rational(11, 61), classes=["given"], label="A")
    F = model.set_point(sp.Rational(60, 61), sp.Rational(-11, 61), label="F")
    B = model.set_point(sp.Rational(28, 45), sp.Rational(-35, 45), classes=["given"], label="B")
    D = model.set_point(sp.Rational(13, 37), sp.Rational(35, 37), label="D")
    G = model.set_point(sp.Rational(-13, 37), sp.Rational(-35, 37), label="G")

    # 2. First case: angle BEC at centre, angle BAC at circumference, diameter AEF.
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(E, B)
    model.set_segment(E, C)

    model.set_segment(A, E)
    model.set_segment(E, F)
    model.set_segment(A, F)
    model.set_section([A, E, F])

    model.set_polygon([E, A, B])
    model.set_polygon([E, A, C])

    # 3. Second case: inflected angle BDC at circumference, diameter DEG.
    model.set_segment(D, B)
    model.set_segment(D, C)

    model.set_segment(D, E)
    model.set_segment(E, G)
    model.set_segment(D, G)
    model.set_section([D, E, G])

    model.set_polygon([E, D, B])
    model.set_polygon([E, D, C])

    return model


if __name__ == "__main__":
    construct_0052_g1()
