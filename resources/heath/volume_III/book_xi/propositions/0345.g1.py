"""Programmatic construction for Book XI, Proposition 32 (0345.g1).

Parallelepipedal solids AB and CD of the same height are to one another as
their bases AE and CF, proved by applying parallelogram FH equal to AE to FG
and completing solid GK (or DH).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0345_g1() -> Model:
    """Construct the two parallelepiped figures for XI.32 using geometor.model."""
    model = Model("0345.g1")

    # Left solid AB with base AE
    T1 = model.set_point(sp.Rational(18, 100), sp.Rational(131, 100), label="T1")
    B = model.set_point(sp.Rational(116, 100), sp.Rational(131, 100), classes=["given"], label="B")
    T2 = model.set_point(sp.Rational(106, 100), sp.Rational(103, 100), label="T2")
    T3 = model.set_point(sp.Rational(8, 100), sp.Rational(103, 100), label="T3")

    A1 = model.set_point(sp.Rational(34, 100), sp.Rational(49, 100), label="A1")
    E = model.set_point(sp.Rational(132, 100), sp.Rational(49, 100), classes=["given"], label="E")
    A2 = model.set_point(sp.Rational(122, 100), sp.Rational(21, 100), label="A2")
    A = model.set_point(sp.Rational(24, 100), sp.Rational(21, 100), classes=["given"], label="A")

    # Right solid CK (CD + GK)
    L = model.set_point(sp.Rational(202, 100), sp.Rational(44, 100), classes=["given"], label="L")
    F = model.set_point(sp.Rational(286, 100), sp.Rational(44, 100), classes=["given"], label="F")
    M1 = model.set_point(sp.Rational(370, 100), sp.Rational(44, 100), label="M1")

    C = model.set_point(sp.Rational(234, 100), sp.Rational(18, 100), classes=["given"], label="C")
    G = model.set_point(sp.Rational(318, 100), sp.Rational(18, 100), classes=["given"], label="G")
    H = model.set_point(sp.Rational(402, 100), sp.Rational(18, 100), label="H")

    N1 = model.set_point(sp.Rational(224, 100), sp.Rational(129, 100), label="N1")
    D = model.set_point(sp.Rational(308, 100), sp.Rational(129, 100), classes=["given"], label="D")
    K = model.set_point(sp.Rational(392, 100), sp.Rational(129, 100), label="K")

    N2 = model.set_point(sp.Rational(256, 100), sp.Rational(103, 100), label="N2")
    D2 = model.set_point(sp.Rational(340, 100), sp.Rational(103, 100), label="D2")
    K2 = model.set_point(sp.Rational(424, 100), sp.Rational(103, 100), label="K2")

    # Left segments and faces
    for p1, p2 in [
        (T1, B), (B, T2), (T2, T3), (T3, T1),
        (A1, E), (E, A2), (A2, A), (A, A1),
        (T1, A1), (B, E), (T2, A2), (T3, A),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([A1, E, A2, A])
    model.set_polygon([T1, B, T2, T3])

    # Right segments and faces
    for p1, p2 in [
        (L, F), (F, M1), (C, G), (G, H),
        (L, C), (F, G), (M1, H),
        (N1, D), (D, K), (N2, D2), (D2, K2),
        (N1, N2), (D, D2), (K, K2),
        (L, N1), (C, N2), (F, D), (G, D2), (M1, K), (H, K2),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([L, F, G, C])
    model.set_polygon([F, M1, H, G])
    model.set_polygon([F, D, D2, G])

    return model


if __name__ == "__main__":
    construct_0345_g1()
