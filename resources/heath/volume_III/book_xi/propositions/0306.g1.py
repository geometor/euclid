"""Programmatic construction for Book XI, Proposition 18 (0306.g1).

If a straight line be at right angles to any plane, all the planes through it
will also be at right angles to the same plane.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0306_g1() -> Model:
    """Construct the figure for Book XI, Proposition 18 using geometor.model."""
    model = Model("0306.g1")

    # 1. Let any straight line AB be at right angles to the plane of reference.
    B = model.set_point(0, 0, classes=["given"], label="B")
    A = model.set_point(0, 1, classes=["given"], label="A")

    # 2. Let plane DE be drawn through AB, with common section CE.
    C = model.set_point(sp.Rational(-93, 78), 0, label="C")
    D = model.set_point(sp.Rational(-93, 78), 1, label="D")
    E = model.set_point(sp.Rational(56, 78), 0, label="E")
    E_top = model.set_point(sp.Rational(56, 78), 1, label="E_top")

    # 3. Let point F be taken at random on CE, and draw FG in plane DE at right angles to CE.
    F = model.set_point(sp.Rational(-43, 78), 0, label="F")
    G = model.set_point(sp.Rational(-43, 78), 1, label="G")

    # Plane of reference corners
    P1 = model.set_point(sp.Rational(-65, 78), sp.Rational(40, 78), label="P1")
    P2 = model.set_point(sp.Rational(94, 78), sp.Rational(40, 78), label="P2")
    P3 = model.set_point(sp.Rational(28, 78), sp.Rational(-29, 78), label="P3")
    P4 = model.set_point(sp.Rational(-115, 78), sp.Rational(-29, 78), label="P4")

    # Segments and sections
    model.set_segment(A, B)
    model.set_segment(F, G)
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, B)
    model.set_segment(B, E)
    model.set_segment(C, E)
    model.set_section([C, F, B])
    model.set_section([F, B, E])

    # Planes
    model.set_polygon([D, E_top, E, C])
    model.set_polygon([P1, P2, P3, P4])

    # Wedges for angles ABF and GFB
    model.set_wedge(B, F, F, A)
    model.set_wedge(F, G, G, B)

    return model


if __name__ == "__main__":
    construct_0306_g1()
