"""Programmatic construction for Book XI, Proposition 30 (0339.g1).

Parallelepipedal solids CM and CN on the same base ACBL (AB) and of the same height,
whose standing sides do not have their extremities on the same straight lines,
compared via intermediate parallelepiped CP with top face OQRP.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0339_g1() -> Model:
    """Construct the three parallelepipeds CM, CN, CP for Book XI, Proposition 30."""
    model = Model("0339.g1")

    # Top plane vertices
    N = model.set_point(sp.Rational(20, 100), sp.Rational(206, 100), classes=["given"], label="N")
    P = model.set_point(sp.Rational(91, 100), sp.Rational(206, 100), label="P")
    K = model.set_point(sp.Rational(188, 100), sp.Rational(206, 100), classes=["given"], label="K")
    R = model.set_point(sp.Rational(251, 100), sp.Rational(206, 100), label="R")

    M = model.set_point(sp.Rational(101, 100), sp.Rational(182, 100), classes=["given"], label="M")
    H = model.set_point(sp.Rational(261, 100), sp.Rational(182, 100), classes=["given"], label="H")

    G = model.set_point(sp.Rational(36, 100), sp.Rational(168, 100), classes=["given"], label="G")
    O = model.set_point(sp.Rational(107, 100), sp.Rational(168, 100), label="O")
    E = model.set_point(sp.Rational(204, 100), sp.Rational(168, 100), classes=["given"], label="E")
    Q = model.set_point(sp.Rational(267, 100), sp.Rational(168, 100), label="Q")

    F = model.set_point(sp.Rational(115, 100), sp.Rational(148, 100), classes=["given"], label="F")
    D = model.set_point(sp.Rational(275, 100), sp.Rational(148, 100), classes=["given"], label="D")

    # Base parallelogram ACBL
    L = model.set_point(sp.Rational(20, 100), sp.Rational(60, 100), classes=["given"], label="L")
    B = model.set_point(sp.Rational(188, 100), sp.Rational(60, 100), classes=["given"], label="B")
    A = model.set_point(sp.Rational(36, 100), sp.Rational(22, 100), classes=["given"], label="A")
    C = model.set_point(sp.Rational(204, 100), sp.Rational(22, 100), classes=["given"], label="C")

    # Top plane collinear lines and segments
    for p, q in [
        (N, R), (N, K), (G, Q), (G, E), (M, H), (F, D),
        (N, G), (K, E), (F, P), (F, M), (D, R), (D, H),
    ]:
        model.set_segment(p, q)

    # Standing edges
    for p, q in [
        (A, F), (A, G), (A, O),
        (L, M), (L, N), (L, P),
        (C, D), (C, E), (C, Q),
        (B, H), (B, K), (B, R),
        (A, C), (C, B), (B, L), (L, A),
    ]:
        model.set_segment(p, q)

    # Base and opposite faces
    model.set_polygon([A, C, B, L])
    model.set_polygon([F, D, H, M])
    model.set_polygon([O, Q, R, P])
    model.set_polygon([G, E, K, N])

    return model


if __name__ == "__main__":
    construct_0339_g1()
