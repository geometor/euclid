"""Programmatic construction for Book XI, Proposition 17 (0305.g2).

If two straight lines be cut by parallel planes, they will be cut in the same
ratios.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0305_g2() -> Model:
    """Construct the figure for Book XI, Proposition 17 using geometor.model."""
    model = Model("0305.g2")

    # 1. Let the two straight lines AB, CD be cut by the parallel planes GH, KL, MN
    #    at the points A, E, B and C, F, D.
    A = model.set_point(0, 1, classes=["given"], label="A")
    E = model.set_point(sp.Rational(75, 179), sp.Rational(84, 179), label="E")
    B = model.set_point(sp.Rational(142, 179), 0, classes=["given"], label="B")

    C = model.set_point(sp.Rational(-47, 179), sp.Rational(156, 179), classes=["given"], label="C")
    F = model.set_point(sp.Rational(5, 179), sp.Rational(63, 179), label="F")
    D = model.set_point(sp.Rational(44, 179), sp.Rational(-10, 179), classes=["given"], label="D")

    # 2. Let AC, BD, AD be joined, let AD meet plane KL at O, and join EO, OF.
    O = model.set_point(sp.Rational(24, 179), sp.Rational(77, 179), label="O")

    # Plane GH corners
    H1 = model.set_point(sp.Rational(-74, 179), sp.Rational(193, 179), label="H1")
    H = model.set_point(sp.Rational(25, 179), sp.Rational(193, 179), classes=["given"], label="H")
    H3 = model.set_point(sp.Rational(10, 179), sp.Rational(144, 179), label="H3")
    G = model.set_point(sp.Rational(-86, 179), sp.Rational(144, 179), classes=["given"], label="G")

    # Plane KL corners
    L1 = model.set_point(sp.Rational(4, 179), sp.Rational(102, 179), label="L1")
    L = model.set_point(sp.Rational(125, 179), sp.Rational(102, 179), classes=["given"], label="L")
    L3 = model.set_point(sp.Rational(108, 179), sp.Rational(52, 179), label="L3")
    K = model.set_point(sp.Rational(-11, 179), sp.Rational(52, 179), classes=["given"], label="K")

    # Plane MN corners
    N1 = model.set_point(sp.Rational(31, 179), sp.Rational(31, 179), label="N1")
    N = model.set_point(sp.Rational(166, 179), sp.Rational(31, 179), classes=["given"], label="N")
    N3 = model.set_point(sp.Rational(143, 179), sp.Rational(-35, 179), label="N3")
    M = model.set_point(sp.Rational(1, 179), sp.Rational(-35, 179), classes=["given"], label="M")

    # Segments and sections
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(A, B)
    model.set_section([A, E, B])
    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_segment(C, D)
    model.set_section([C, F, D])
    model.set_segment(A, O)
    model.set_segment(O, D)
    model.set_segment(A, D)
    model.set_section([A, O, D])
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(E, O)
    model.set_segment(O, F)

    # Planes and polygons
    model.set_polygon([H1, H, H3, G])
    model.set_polygon([L1, L, L3, K])
    model.set_polygon([N1, N, N3, M])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([E, B, D, O])
    model.set_polygon([A, O, F, C])

    return model


if __name__ == "__main__":
    construct_0305_g2()
