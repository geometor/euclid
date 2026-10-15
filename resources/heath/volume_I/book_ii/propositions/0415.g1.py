"""Programmatic construction for Book II, Proposition 10 — Bergh's figure (0415.g1).

Geometrical discovery of successive side- and diagonal-numbers from an
isosceles right-angled triangle ABC with sides lengthened by the hypotenuse.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0415_g1() -> Model:
    """Construct Bergh's figure 0415.g1 for side and diagonal numbers."""
    model = Model("0415.g1")

    a = sp.Integer(1)
    d = sp.sqrt(2)
    a_next = a + d

    # Right-angled isosceles triangle ABC at A(0, 0)
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(a, 0, classes=["given"], label="B")
    C = model.set_point(0, a, classes=["given"], label="C")

    # Lengthen AB, AC by d to D, E
    D = model.set_point(a_next, 0, label="D")
    E = model.set_point(0, a_next, label="E")

    # Join BC and DE; draw BF, CG perpendicular to DE
    F = model.set_point(a + sp.Rational(1, 2), sp.Rational(1, 2), label="F")
    G = model.set_point(sp.Rational(1, 2), a + sp.Rational(1, 2), label="G")

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, D)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(C, E)
    model.set_segment(A, E)
    model.set_segment(B, C)
    model.set_segment(D, E)
    model.set_segment(E, G)
    model.set_segment(G, F)
    model.set_segment(F, D)
    model.set_segment(B, F)
    model.set_segment(C, G)

    # Polygons and right angle at A
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, E])
    model.set_polygon([B, F, G, C])
    model.set_wedge(A, B, B, C)

    return model


if __name__ == "__main__":
    construct_0415_g1()
