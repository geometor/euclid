"""Programmatic construction for Book XI, Proposition 26 (0331.g1).

On a given straight line AB and at point A on it, construct a solid angle A-BLH
equal to a given solid angle D-CEF.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0331_g1() -> Model:
    """Construct the figure for Book XI, Proposition 26 using geometor.model."""
    model = Model("0331.g1")

    # Plane of reference boundary
    P1 = model.set_point(sp.Rational(42, 100), sp.Rational(-97, 100), label="P1")
    P2 = model.set_point(sp.Rational(388, 100), sp.Rational(-97, 100), label="P2")
    P3 = model.set_point(sp.Rational(362, 100), sp.Rational(-238, 100), label="P3")
    P4 = model.set_point(sp.Rational(16, 100), sp.Rational(-238, 100), label="P4")
    model.set_polygon([P1, P2, P3, P4])

    # Given solid angle at D
    D = model.set_point(sp.Rational(68, 100), sp.Rational(-184, 100), classes=["given"], label="D")
    C = model.set_point(sp.Rational(134, 100), sp.Rational(-138, 100), classes=["given"], label="C")
    E = model.set_point(sp.Rational(138, 100), sp.Rational(-218, 100), classes=["given"], label="E")
    F = model.set_point(sp.Rational(156, 100), sp.Rational(-56, 100), classes=["given"], label="F")
    G = model.set_point(sp.Rational(156, 100), sp.Rational(-184, 100), label="G")

    # Constructed solid angle at A on AB
    A = model.set_point(sp.Rational(251, 100), sp.Rational(-218, 100), classes=["given"], label="A")
    B = model.set_point(sp.Rational(345, 100), sp.Rational(-168, 100), classes=["given"], label="B")
    L = model.set_point(sp.Rational(233, 100), sp.Rational(-125, 100), label="L")
    K = model.set_point(sp.Rational(306, 100), sp.Rational(-125, 100), label="K")
    H = model.set_point(sp.Rational(325, 100), sp.Rational(-22, 100), label="H")

    # Segments
    for u, v in [
        (D, C), (D, E), (D, F), (D, G),
        (F, C), (F, E), (F, G), (C, G), (E, G),
        (A, B), (A, L), (A, K), (A, H),
        (H, L), (H, K), (H, B), (L, K), (K, B),
    ]:
        model.set_segment(u, v)

    # Polygons
    for poly in [
        [E, D, C], [E, D, F], [F, D, C], [F, G, D], [F, G, E], [G, D, E],
        [B, A, L], [B, A, H], [H, A, L], [H, K, A], [H, K, B], [K, A, B],
    ]:
        model.set_polygon(poly)

    # Angles
    model.set_wedge(D, E, E, C)
    model.set_wedge(D, E, E, F)
    model.set_wedge(D, F, F, C)
    model.set_wedge(D, E, E, G)
    model.set_wedge(G, F, F, D)
    model.set_wedge(G, F, F, E)
    model.set_wedge(A, B, B, L)
    model.set_wedge(A, B, B, K)
    model.set_wedge(A, B, B, H)
    model.set_wedge(A, H, H, L)
    model.set_wedge(K, H, H, A)
    model.set_wedge(K, H, H, B)

    return model


if __name__ == "__main__":
    construct_0331_g1()
