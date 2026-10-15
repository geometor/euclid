"""Programmatic construction for Book XI, Proposition 29 Commentary (0338.g1).

Two alternative cases of Proposition 29:
1. Left figure: the two top faces opposite to AB share an edge MG / HE.
2. Right figure: the two top faces opposite to AB are completely separate (H left of E).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0338_g1() -> Model:
    """Construct the two alternative cases of Book XI, Proposition 29 (0338.g1)."""
    model = Model("0338.g1")

    # Case 1 (Left): H=E, M=G
    D1 = model.set_point(sp.Rational(20, 100), sp.Rational(121, 100), classes=["given"], label="D")
    HE1 = model.set_point(sp.Rational(144, 100), sp.Rational(121, 100), classes=["given"], label="HE")
    K1 = model.set_point(sp.Rational(268, 100), sp.Rational(121, 100), classes=["given"], label="K")

    F1 = model.set_point(sp.Rational(25, 100), sp.Rational(97, 100), classes=["given"], label="F")
    MG1 = model.set_point(sp.Rational(149, 100), sp.Rational(97, 100), classes=["given"], label="MG")
    N1 = model.set_point(sp.Rational(273, 100), sp.Rational(97, 100), classes=["given"], label="N")

    C1 = model.set_point(sp.Rational(64, 100), sp.Rational(49, 100), classes=["given"], label="C")
    B1 = model.set_point(sp.Rational(188, 100), sp.Rational(49, 100), classes=["given"], label="B")
    A1 = model.set_point(sp.Rational(69, 100), sp.Rational(20, 100), classes=["given"], label="A")
    L1 = model.set_point(sp.Rational(193, 100), sp.Rational(20, 100), classes=["given"], label="L")

    for p, q in [
        (D1, K1), (F1, N1), (C1, B1), (A1, L1),
        (D1, F1), (HE1, MG1), (K1, N1), (C1, A1), (B1, L1),
        (C1, D1), (A1, F1), (C1, HE1), (A1, MG1),
        (B1, HE1), (L1, MG1), (B1, K1), (L1, N1),
    ]:
        model.set_segment(p, q)

    model.set_polygon([G := MG1, A1, L1])
    model.set_polygon([E := HE1, C1, B1])
    model.set_polygon([A1, C1, B1, L1])

    # Case 2 (Right): H left of E, M left of G
    D2 = model.set_point(sp.Rational(288, 100), sp.Rational(121, 100), classes=["given"], label="D'")
    H2 = model.set_point(sp.Rational(396, 100), sp.Rational(121, 100), classes=["given"], label="H'")
    E2 = model.set_point(sp.Rational(450, 100), sp.Rational(121, 100), classes=["given"], label="E'")
    K2 = model.set_point(sp.Rational(558, 100), sp.Rational(121, 100), classes=["given"], label="K'")

    F2 = model.set_point(sp.Rational(293, 100), sp.Rational(97, 100), classes=["given"], label="F'")
    M2 = model.set_point(sp.Rational(401, 100), sp.Rational(97, 100), classes=["given"], label="M'")
    G2 = model.set_point(sp.Rational(455, 100), sp.Rational(97, 100), classes=["given"], label="G'")
    N2 = model.set_point(sp.Rational(563, 100), sp.Rational(97, 100), classes=["given"], label="N'")

    C2 = model.set_point(sp.Rational(354, 100), sp.Rational(49, 100), classes=["given"], label="C'")
    B2 = model.set_point(sp.Rational(462, 100), sp.Rational(49, 100), classes=["given"], label="B'")
    A2 = model.set_point(sp.Rational(359, 100), sp.Rational(20, 100), classes=["given"], label="A'")
    L2 = model.set_point(sp.Rational(467, 100), sp.Rational(20, 100), classes=["given"], label="L'")

    for p, q in [
        (D2, K2), (F2, N2), (C2, B2), (A2, L2),
        (D2, F2), (H2, M2), (E2, G2), (K2, N2), (C2, A2), (B2, L2),
        (C2, D2), (A2, F2), (C2, E2), (A2, G2),
        (B2, H2), (L2, M2), (B2, K2), (L2, N2),
    ]:
        model.set_segment(p, q)

    model.set_polygon([F2, D2, K2, N2])
    model.set_polygon([A2, C2, B2, L2])

    return model


if __name__ == "__main__":
    construct_0338_g1()
