"""Programmatic construction for Book XI, Proposition 15 Commentary 5 (0303.g3).

Legendre's proof of Euclid's Proposition XI.15 using triangular prism sections.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0303_g3() -> Model:
    """Construct the figure for 0303.g3 using geometor.model."""
    model = Model("0303.g3")

    # 1. If ABC, DEF be the angles, make AB equal to DE, and BC equal to EF,
    #    and join CA, FD, BE, CF, AD.
    B = model.set_point(0, 1, classes=["given"], label="B")
    A = model.set_point(sp.Rational(65, 102), sp.Rational(123, 102), classes=["given"], label="A")
    C = model.set_point(sp.Rational(44, 102), sp.Rational(87, 102), classes=["given"], label="C")

    E = model.set_point(sp.Rational(60, 102), 0, classes=["given"], label="E")
    D = model.set_point(sp.Rational(126, 102), sp.Rational(21, 102), classes=["given"], label="D")
    F = model.set_point(sp.Rational(104, 102), sp.Rational(-17, 102), classes=["given"], label="F")

    # 2. Let the plane drawn through B parallel to plane DEF meet CF, AD in H, G.
    G = model.set_point(sp.Rational(74, 102), sp.Rational(108, 102), label="G")
    H = model.set_point(sp.Rational(48, 102), sp.Rational(80, 102), label="H")

    # Upper plane corners
    P1 = model.set_point(sp.Rational(-17, 102), sp.Rational(138, 102), label="P1")
    P2 = model.set_point(sp.Rational(109, 102), sp.Rational(137, 102), label="P2")
    P3 = model.set_point(sp.Rational(86, 102), sp.Rational(65, 102), label="P3")
    P4 = model.set_point(sp.Rational(-38, 102), sp.Rational(66, 102), label="P4")

    # Lower plane corners
    Q1 = model.set_point(sp.Rational(24, 102), sp.Rational(35, 102), label="Q1")
    Q2 = model.set_point(sp.Rational(173, 102), sp.Rational(35, 102), label="Q2")
    Q3 = model.set_point(sp.Rational(149, 102), sp.Rational(-50, 102), label="Q3")
    Q4 = model.set_point(sp.Rational(-1, 102), sp.Rational(-49, 102), label="Q4")

    # Segments and sections
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, D)
    model.set_segment(B, E)
    model.set_segment(C, F)
    model.set_segment(C, H)
    model.set_segment(H, F)
    model.set_section([C, H, F])
    model.set_segment(A, D)
    model.set_segment(A, G)
    model.set_segment(G, D)
    model.set_section([A, G, D])

    # Polygons and planes
    model.set_polygon([P1, P2, P3, P4])
    model.set_polygon([Q1, Q2, Q3, Q4])
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])

    # Wedges for angles ABC and DEF
    model.set_wedge(B, A, A, C)
    model.set_wedge(E, D, D, F)

    return model


if __name__ == "__main__":
    construct_0303_g3()
