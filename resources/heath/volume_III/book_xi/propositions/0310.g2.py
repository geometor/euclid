"""Programmatic construction for Book XI, Proposition 19 Lemma 2 (0310.g2).

To draw a common perpendicular to two straight lines not in the same plane,
and prove that only one common perpendicular can be drawn.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0310_g2() -> Model:
    """Construct the Lemma 2 figure for Book XI, Proposition 19 using geometor.model."""
    model = Model("0310.g2")

    # Plane MN boundary corners
    M1 = model.set_point(sp.Rational(-49, 80), sp.Rational(50, 80), label="M1")
    N = model.set_point(sp.Rational(197, 80), sp.Rational(50, 80), classes=["given"], label="N")
    M2 = model.set_point(sp.Rational(157, 80), sp.Rational(-58, 80), label="M2")
    M = model.set_point(sp.Rational(-94, 80), sp.Rational(-58, 80), classes=["given"], label="M")

    # 1. Let AB, CD be the given straight lines.
    # 2. Through CD draw the plane MN parallel to AB.
    # 3. Through AB draw the plane AF perpendicular to the plane MN, intersecting in EF.
    G = model.set_point(0, 0, classes=["given"], label="G")
    H = model.set_point(0, 1, classes=["given"], label="H")
    A = model.set_point(sp.Rational(-49, 80), 1, classes=["given"], label="A")
    B = model.set_point(sp.Rational(167, 80), 1, classes=["given"], label="B")
    E = model.set_point(sp.Rational(-49, 80), 0, classes=["given"], label="E")
    F = model.set_point(sp.Rational(167, 80), 0, classes=["given"], label="F")

    # 4. Line CD meeting EF in G, with L on CD
    C = model.set_point(sp.Rational(-11, 80), sp.Rational(17, 80), classes=["given"], label="C")
    L = model.set_point(sp.Rational(18, 80), sp.Rational(-26, 80), label="L")
    D = model.set_point(sp.Rational(35, 80), sp.Rational(-50, 80), classes=["given"], label="D")

    # 5. Uniqueness construction: KL, LQ, KP
    K = model.set_point(sp.Rational(109, 80), 1, label="K")
    P = model.set_point(sp.Rational(109, 80), 0, label="P")
    Q = model.set_point(sp.Rational(82, 80), sp.Rational(-26, 80), label="Q")

    # Segments
    model.set_segment(A, B)
    model.set_segment(E, F)
    model.set_segment(A, E)
    model.set_segment(B, F)
    model.set_segment(G, H)
    model.set_segment(C, D)
    model.set_segment(C, L)
    model.set_segment(K, L)
    model.set_segment(L, Q)
    model.set_segment(K, P)

    # Planes
    model.set_segment(M1, N)
    model.set_segment(N, M2)
    model.set_segment(M2, M)
    model.set_segment(M, M1)
    model.set_polygon([M1, N, M2, M])
    model.set_polygon([A, B, F, E])

    return model


if __name__ == "__main__":
    construct_0310_g2()
