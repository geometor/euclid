"""Programmatic construction for Book III, Proposition 18 (0050.g1).

If a straight line touch a circle, and a straight line be joined from the
centre to the point of contact, the straight line so joined will be
perpendicular to the tangent.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0050_g1() -> Model:
    """Construct the figure for Book III, Proposition 18 using geometor.model."""
    model = Model("0050.g1")

    # 1. Circle ABC about centre F, touched by straight line DE at C.
    F = model.set_point(0, 0, classes=["given"], label="F")
    C = model.set_point(sp.Rational(4, 5), sp.Rational(-3, 5), classes=["given"], label="C")
    B = model.set_point(1, 0, label="B")
    A = model.set_point(sp.Rational(-4, 5), sp.Rational(3, 5), label="A")

    circle_ABC = model.construct_circle(F, C)

    # 2. Tangent DE through C and radius FC joined.
    G = model.set_point(sp.Rational(5, 4), 0, label="G")
    D = model.set_point(sp.Rational(23, 16), sp.Rational(1, 4), label="D")
    E = model.set_point(sp.Rational(31, 80), sp.Rational(-23, 20), label="E")

    line_DE = model.construct_line(D, E)
    model.set_segment(D, G)
    model.set_segment(G, C)
    model.set_segment(C, E)
    model.set_segment(D, C)
    model.set_segment(G, E)
    model.set_segment(D, E)
    model.set_section([D, G, C])
    model.set_section([G, C, E])

    model.set_segment(F, C)

    # 3. Reductio: suppose FG is perpendicular to DE, cutting circle ABC at B.
    model.set_segment(F, B)
    model.set_segment(B, G)
    model.set_segment(F, G)
    model.set_section([F, B, G])

    model.set_polygon([F, C, G])

    return model


if __name__ == "__main__":
    construct_0050_g1()
