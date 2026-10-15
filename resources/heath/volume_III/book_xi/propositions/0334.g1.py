"""Programmatic construction for Book XI, Proposition 28 (0334.g1).

Parallelepipedal solid AB cut by plane CDEF through the diagonals CF, DE of
opposite planes, bisecting the solid into two equal prisms.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0334_g1() -> Model:
    """Construct the figure for Book XI, Proposition 28 using geometor.model."""
    model = Model("0334.g1")

    B = model.set_point(sp.Rational(58, 100), sp.Rational(-22, 100), classes=["given"], label="B")
    F = model.set_point(sp.Rational(156, 100), sp.Rational(-22, 100), label="F")
    E = model.set_point(sp.Rational(138, 100), sp.Rational(-68, 100), label="E")
    H = model.set_point(sp.Rational(40, 100), sp.Rational(-68, 100), label="H")

    C = model.set_point(sp.Rational(42, 100), sp.Rational(-104, 100), label="C")
    G = model.set_point(sp.Rational(140, 100), sp.Rational(-104, 100), label="G")
    A = model.set_point(sp.Rational(122, 100), sp.Rational(-150, 100), classes=["given"], label="A")
    D = model.set_point(sp.Rational(24, 100), sp.Rational(-150, 100), label="D")

    # 12 edges + 2 diagonals CF, DE
    for u, v in [
        (B, F), (F, E), (E, H), (H, B),
        (C, G), (G, A), (A, D), (D, C),
        (B, C), (F, G), (E, A), (H, D),
        (C, F), (D, E),
    ]:
        model.set_segment(u, v)

    # Diagonal plane, faces, and triangular prism bases
    for poly in [
        [C, D, E, F],
        [C, G, A, D],
        [B, F, E, H],
        [G, F, E, A],
        [C, B, H, D],
        [C, G, F],
        [C, F, B],
        [A, D, E],
        [D, E, H],
    ]:
        model.set_polygon(poly)

    return model


if __name__ == "__main__":
    construct_0334_g1()
