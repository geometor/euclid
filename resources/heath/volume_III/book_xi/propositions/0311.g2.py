"""Programmatic construction for Book XI, Proposition 19 Smith and Bryant Construction (0311.g2).

Construction of the common perpendicular LK to two skew straight lines AB, CD.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0311_g2() -> Model:
    """Construct Smith and Bryant's figure for Book XI, Proposition 19 using geometor.model."""
    model = Model("0311.g2")

    # 1. Let AB, CD be the two given straight lines.
    K = model.set_point(0, 0, classes=["given"], label="K")
    C = model.set_point(sp.Rational(-49, 56), 0, classes=["given"], label="C")
    E = model.set_point(sp.Rational(86, 56), 0, classes=["given"], label="E")
    D = model.set_point(sp.Rational(167, 56), 0, classes=["given"], label="D")

    L = model.set_point(0, 1, label="L")
    A = model.set_point(sp.Rational(-21, 56), sp.Rational(45, 56), classes=["given"], label="A")
    G = model.set_point(sp.Rational(68, 56), sp.Rational(92, 56), classes=["given"], label="G")
    B = model.set_point(sp.Rational(141, 56), sp.Rational(131, 56), classes=["given"], label="B")

    # 2. Through E in CD draw EF parallel to AB.
    F = model.set_point(sp.Rational(193, 56), 1, label="F")
    F_ext = model.set_point(sp.Rational(41, 56), sp.Rational(-24, 56), label="F_ext")

    # 3. From G in AB draw GH perpendicular to plane CDF, meeting the plane in H.
    H = model.set_point(sp.Rational(68, 56), sp.Rational(36, 56), label="H")

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, L)
    model.set_segment(L, G)
    model.set_segment(G, B)
    model.set_segment(C, D)
    model.set_segment(C, K)
    model.set_segment(K, E)
    model.set_segment(E, D)
    model.set_segment(E, F)
    model.set_segment(F_ext, F)
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(L, K)

    # Planes and parallelogram
    model.set_polygon([G, H, K, L])
    model.set_polygon([A, B, H, K])
    model.set_polygon([C, D, F])

    return model


if __name__ == "__main__":
    construct_0311_g2()
