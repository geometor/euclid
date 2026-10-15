"""Programmatic construction for Book XI, Proposition 16 (0304.g1).

If two parallel planes be cut by any plane, their common sections are parallel.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0304_g1() -> Model:
    """Construct the figure for Book XI, Proposition 16 using geometor.model."""
    model = Model("0304.g1")

    # 1. Let the two parallel planes AB, CD be cut by the plane EFGH,
    #    and let EF, GH be their common sections.
    E = model.set_point(0, 1, classes=["given"], label="E")
    F = model.set_point(sp.Rational(100, 106), 1, classes=["given"], label="F")
    G = model.set_point(sp.Rational(25, 106), 0, classes=["given"], label="G")
    H = model.set_point(sp.Rational(146, 106), 0, classes=["given"], label="H")

    # 2. Suppose EF, GH produced meet at K.
    K = model.set_point(sp.Rational(366, 106), sp.Rational(36, 106), label="K")

    # Plane AB corners
    B1 = model.set_point(sp.Rational(9, 106), sp.Rational(142, 106), label="B1")
    B = model.set_point(sp.Rational(110, 106), sp.Rational(142, 106), classes=["given"], label="B")
    B3 = model.set_point(sp.Rational(95, 106), sp.Rational(89, 106), label="B3")
    A = model.set_point(sp.Rational(-4, 106), sp.Rational(89, 106), classes=["given"], label="A")

    # Plane CD corners
    D1 = model.set_point(sp.Rational(34, 106), sp.Rational(28, 106), label="D1")
    D = model.set_point(sp.Rational(166, 106), sp.Rational(28, 106), classes=["given"], label="D")
    D3 = model.set_point(sp.Rational(120, 106), sp.Rational(-36, 106), label="D3")
    C = model.set_point(sp.Rational(12, 106), sp.Rational(-36, 106), classes=["given"], label="C")

    # Segments and sections
    model.set_segment(E, F)
    model.set_segment(F, K)
    model.set_segment(E, K)
    model.set_section([E, F, K])
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(G, K)
    model.set_section([G, H, K])
    model.set_segment(E, G)
    model.set_segment(F, H)

    # Planes
    model.set_polygon([B1, B, B3, A])
    model.set_polygon([D1, D, D3, C])
    model.set_polygon([E, F, H, G])

    return model


if __name__ == "__main__":
    construct_0304_g1()
