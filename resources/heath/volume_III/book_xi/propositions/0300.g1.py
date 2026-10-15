"""Programmatic construction for Book XI, Proposition 14 (0300.g1).

Planes to which the same straight line is at right angles will be parallel.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0300_g1() -> Model:
    """Construct the figure for Book XI, Proposition 14 using geometor.model."""
    model = Model("0300.g1")

    # 1. Let any straight line AB be at right angles to each of the planes CD, EF.
    A = model.set_point(0, 1, classes=["given"], label="A")
    B = model.set_point(sp.Rational(3, 69), 0, classes=["given"], label="B")

    # Plane CD corners
    C1 = model.set_point(sp.Rational(-25, 69), sp.Rational(85, 69), label="C1")
    C = model.set_point(sp.Rational(42, 69), sp.Rational(85, 69), classes=["given"], label="C")
    C3 = model.set_point(sp.Rational(29, 69), sp.Rational(54, 69), label="C3")
    D = model.set_point(sp.Rational(-35, 69), sp.Rational(54, 69), classes=["given"], label="D")

    # Plane EF corners
    F1 = model.set_point(sp.Rational(-45, 69), sp.Rational(19, 69), label="F1")
    F = model.set_point(sp.Rational(41, 69), sp.Rational(19, 69), classes=["given"], label="F")
    F3 = model.set_point(sp.Rational(26, 69), sp.Rational(-17, 69), label="F3")
    E = model.set_point(sp.Rational(-54, 69), sp.Rational(-17, 69), classes=["given"], label="E")

    # 2. Suppose they meet at common section GH, and let point K be taken on GH.
    G = model.set_point(sp.Rational(200, 69), sp.Rational(92, 69), label="G")
    H = model.set_point(sp.Rational(152, 69), sp.Rational(-19, 69), label="H")
    K = model.set_point(sp.Rational(180, 69), sp.Rational(46, 69), label="K")

    # Segments and section
    model.set_segment(A, B)
    model.set_segment(G, H)
    model.set_segment(G, K)
    model.set_segment(K, H)
    model.set_section([G, K, H])
    model.set_segment(A, K)
    model.set_segment(B, K)

    # Planes CD, EF and triangle ABK
    model.set_polygon([C1, C, C3, D])
    model.set_polygon([F1, F, F3, E])
    model.set_polygon([A, B, K])

    # Wedges for angles ABK and BAK
    model.set_wedge(B, A, A, K)
    model.set_wedge(A, K, K, B)

    return model


if __name__ == "__main__":
    construct_0300_g1()
