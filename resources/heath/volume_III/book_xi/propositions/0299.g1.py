"""Programmatic construction for Book XI, Proposition 13 (0299.g1).

From the same point two straight lines cannot be set up at right angles to the
same plane on the same side.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0299_g1() -> Model:
    """Construct the figure for Book XI, Proposition 13 using geometor.model."""
    model = Model("0299.g1")

    # Perspective plane of reference boundary corners
    P1 = model.set_point(sp.Rational(-50, 91), sp.Rational(48, 91), label="P1")
    P2 = model.set_point(sp.Rational(87, 91), sp.Rational(48, 91), label="P2")
    P3 = model.set_point(sp.Rational(63, 91), sp.Rational(-28, 91), label="P3")
    P4 = model.set_point(sp.Rational(-74, 91), sp.Rational(-28, 91), label="P4")

    # 1. From the same point A let the two straight lines AB, AC be set up at
    #    right angles to the plane of reference and on the same side.
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(0, 1, classes=["given"], label="B")
    C = model.set_point(sp.Rational(16, 91), sp.Rational(76, 91), classes=["given"], label="C")

    # 2. Let a plane be drawn through BA, AC making section DAE in the plane of reference.
    D = model.set_point(sp.Rational(-62, 91), sp.Rational(20, 91), label="D")
    E = model.set_point(sp.Rational(68, 91), sp.Rational(-21, 91), label="E")

    # Segments and section
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(D, A)
    model.set_segment(A, E)
    model.set_segment(D, E)
    model.set_section([D, A, E])

    # Plane of reference and plane through BA, AC
    model.set_segment(P1, P2)
    model.set_segment(P2, P3)
    model.set_segment(P3, P4)
    model.set_segment(P4, P1)
    model.set_polygon([P1, P2, P3, P4])
    model.set_polygon([B, A, C])
    model.set_polygon([B, A, E, C])

    # Wedges for angles CAE and BAE
    model.set_wedge(A, C, C, E)
    model.set_wedge(A, B, B, E)

    return model


if __name__ == "__main__":
    construct_0299_g1()
