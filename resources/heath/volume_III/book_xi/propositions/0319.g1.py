"""Programmatic construction for Book XI, Proposition 23 Figure 1 (0319.g1).

Construct the three given isosceles triangles ABC, DEF, GHK containing the
three given plane angles at B, E, H with equal legs AB = BC = DE = EF = GH = HK.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0319_g1() -> Model:
    """Construct Figure 1 for Book XI, Proposition 23 using geometor.model."""
    model = Model("0319.g1")

    # Triangle ABC
    A = model.set_point(sp.Rational(30, 100), sp.Rational(-132, 100), classes=["given"], label="A")
    B = model.set_point(sp.Rational(96, 100), sp.Rational(-29, 100), classes=["given"], label="B")
    C = model.set_point(sp.Rational(160, 100), sp.Rational(-132, 100), classes=["given"], label="C")

    # Triangle DEF
    D = model.set_point(sp.Rational(233, 100), sp.Rational(-132, 100), classes=["given"], label="D")
    E = model.set_point(sp.Rational(311, 100), sp.Rational(-42, 100), classes=["given"], label="E")
    F = model.set_point(sp.Rational(392, 100), sp.Rational(-132, 100), classes=["given"], label="F")

    # Triangle GHK
    G = model.set_point(sp.Rational(431, 100), sp.Rational(-132, 100), classes=["given"], label="G")
    H = model.set_point(sp.Rational(492, 100), sp.Rational(-35, 100), classes=["given"], label="H")
    K = model.set_point(sp.Rational(578, 100), sp.Rational(-132, 100), classes=["given"], label="K")

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, C)

    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(D, F)

    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(G, K)

    # Polygons (Triangles)
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([G, H, K])

    # Angles at B, E, H
    model.set_wedge(B, A, A, C)
    model.set_wedge(E, D, D, F)
    model.set_wedge(H, G, G, K)

    return model


if __name__ == "__main__":
    construct_0319_g1()
