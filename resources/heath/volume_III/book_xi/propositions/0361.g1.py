"""Programmatic construction for Book XI, Proposition 36 (0361.g1).

If three straight lines A, B, C be proportional, the parallelepipedal solid LH
formed out of A, B, C is equal to the equilateral and equiangular
parallelepipedal solid EK on the mean B.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0361_g1() -> Model:
    """Construct the two equiangular parallelepipeds LH and EK and lines A, B, C for XI.36."""
    model = Model("0361.g1")

    # Left parallelepiped LH
    H = model.set_point(sp.Rational(48, 100), sp.Rational(229, 100), classes=["given"], label="H")
    H_right = model.set_point(sp.Rational(174, 100), sp.Rational(229, 100), label="H_right")
    N_left = model.set_point(sp.Rational(108, 100), sp.Rational(181, 100), label="N_left")
    N = model.set_point(sp.Rational(234, 100), sp.Rational(181, 100), classes=["given"], label="N")

    O_left = model.set_point(sp.Rational(12, 100), sp.Rational(159, 100), label="O_left")
    O = model.set_point(sp.Rational(138, 100), sp.Rational(159, 100), classes=["given"], label="O")
    M = model.set_point(sp.Rational(72, 100), sp.Rational(111, 100), classes=["given"], label="M")
    L = model.set_point(sp.Rational(198, 100), sp.Rational(111, 100), classes=["given"], label="L")

    # Proportional lines A, B, C
    A1 = model.set_point(sp.Rational(74, 100), sp.Rational(79, 100), classes=["given"], label="A")
    A2 = model.set_point(sp.Rational(196, 100), sp.Rational(79, 100), label="A2")
    B1 = model.set_point(sp.Rational(74, 100), sp.Rational(51, 100), classes=["given"], label="B")
    B2 = model.set_point(sp.Rational(166, 100), sp.Rational(51, 100), label="B2")
    C1 = model.set_point(sp.Rational(74, 100), sp.Rational(23, 100), classes=["given"], label="C")
    C2 = model.set_point(sp.Rational(142, 100), sp.Rational(23, 100), label="C2")

    # Right parallelepiped EK
    K = model.set_point(sp.Rational(356, 100), sp.Rational(215, 100), classes=["given"], label="K")
    K_right = model.set_point(sp.Rational(468, 100), sp.Rational(215, 100), label="K_right")
    D_left = model.set_point(sp.Rational(416, 100), sp.Rational(167, 100), label="D_left")
    D = model.set_point(sp.Rational(528, 100), sp.Rational(167, 100), classes=["given"], label="D")

    G_left = model.set_point(sp.Rational(312, 100), sp.Rational(129, 100), label="G_left")
    G = model.set_point(sp.Rational(424, 100), sp.Rational(129, 100), classes=["given"], label="G")
    F = model.set_point(sp.Rational(372, 100), sp.Rational(81, 100), classes=["given"], label="F")
    E = model.set_point(sp.Rational(484, 100), sp.Rational(81, 100), classes=["given"], label="E")

    for p1, p2 in [
        (H, H_right), (H_right, N), (N, N_left), (N_left, H),
        (O_left, O), (O, L), (L, M), (M, O_left),
        (O_left, H), (O, H_right), (L, N), (M, N_left),
        (A1, A2), (B1, B2), (C1, C2),
        (K, K_right), (K_right, D), (D, D_left), (D_left, K),
        (G_left, G), (G, E), (E, F), (F, G_left),
        (G_left, K), (G, K_right), (E, D), (F, D_left),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([M, L, N, N_left])
    model.set_polygon([O_left, O, L, M])
    model.set_polygon([F, E, D, D_left])
    model.set_polygon([G_left, G, E, F])

    return model


if __name__ == "__main__":
    construct_0361_g1()
