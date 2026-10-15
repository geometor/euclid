"""Programmatic construction for Book I, Proposition 2 Note — Proclus' Cases (0259.g1).

Models Proclus' two alternative cases of Proposition 2:
1. Case where AB < BC and G lies on BD produced beyond D.
2. Case where AB > BC and G lies on BD itself (no side of triangle DAB produced).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0259_g1() -> Model:
    """Construct Proclus' alternative cases for Book I, Proposition 2 (0259.g1)."""
    model = Model("0259.g1")

    #Given base AB and equilateral triangle DAB (drawn downward as in Heath p. 245)
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(1, 0, classes=["given"], label="B")
    model.set_segment(A, B)

    D = model.set_point(sp.Rational(1, 2), -sp.sqrt(3) / 2, label="D")
    model.set_segment(D, A)
    model.set_segment(D, B)
    model.set_polygon([D, A, B])

    # Given segment BC (for Case AB > BC, length 1/2 so G lies on BD itself;
    # and extended lines [ B D ], [ D A ] for Case AB < BC where G lies beyond D)
    C = model.set_point(sp.Rational(3, 4), sp.sqrt(3) / 4, classes=["given"], label="C")
    model.set_segment(B, C)

    model.construct_line(D, A)
    model.construct_line(D, B)

    # Circle ( B C ) intersecting DB at G, and circle ( D G ) intersecting DA at L
    model.construct_circle(B, C)
    G = model.set_point(sp.Rational(3, 4), -sp.sqrt(3) / 4, label="G")
    H = model.set_point(sp.Rational(3, 2), 0, label="H")

    model.construct_circle(D, G)
    L = model.set_point(sp.Rational(1, 4), -sp.sqrt(3) / 4, label="L")
    K = model.set_point(1, -sp.sqrt(3) / 2, label="K")

    # Collinear sections and segments referenced in Proclus' commentary
    model.set_section([D, A, L])
    model.set_section([D, B, G])

    model.set_segment(A, L)
    model.set_segment(B, G)
    model.set_segment(D, L)
    model.set_segment(D, G)

    return model


if __name__ == "__main__":
    construct_0259_g1()
