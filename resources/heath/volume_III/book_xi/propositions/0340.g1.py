"""Programmatic construction for Book XI, Proposition 30 Commentary (0340.g1).

Legendre's reduction of an oblique parallelepiped ABCD-EFGH to an equivalent
right parallelepiped ABCD-IKLM and then to a rectangular parallelepiped AOND-IPQM.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0340_g1() -> Model:
    """Construct Legendre's parallelepiped reduction figure (0340.g1)."""
    model = Model("0340.g1")

    # Base points ABCD and perpendicular feet O, N on BC
    D = model.set_point(sp.Rational(21, 100), sp.Rational(67, 100), classes=["given"], label="D")
    N = model.set_point(sp.Rational(106, 100), sp.Rational(67, 100), label="N")
    C = model.set_point(sp.Rational(116, 100), sp.Rational(56, 100), classes=["given"], label="C")
    A = model.set_point(sp.Rational(52, 100), sp.Rational(33, 100), classes=["given"], label="A")
    O = model.set_point(sp.Rational(137, 100), sp.Rational(33, 100), label="O")
    B = model.set_point(sp.Rational(147, 100), sp.Rational(22, 100), classes=["given"], label="B")

    # Top points of right and rectangular parallelepipeds
    M = model.set_point(sp.Rational(21, 100), sp.Rational(227, 100), label="M")
    Q = model.set_point(sp.Rational(106, 100), sp.Rational(227, 100), label="Q")
    L = model.set_point(sp.Rational(116, 100), sp.Rational(216, 100), label="L")
    I = model.set_point(sp.Rational(52, 100), sp.Rational(193, 100), label="I")
    P = model.set_point(sp.Rational(137, 100), sp.Rational(193, 100), label="P")
    K = model.set_point(sp.Rational(147, 100), sp.Rational(182, 100), label="K")

    # Top points of original oblique parallelepiped EFGH
    H = model.set_point(sp.Rational(152, 100), sp.Rational(246, 100), classes=["given"], label="H")
    G = model.set_point(sp.Rational(247, 100), sp.Rational(235, 100), classes=["given"], label="G")
    E = model.set_point(sp.Rational(183, 100), sp.Rational(212, 100), classes=["given"], label="E")
    F = model.set_point(sp.Rational(278, 100), sp.Rational(201, 100), classes=["given"], label="F")

    # Segments
    for p, q in [
        (A, I), (B, K), (C, L), (D, M), (O, P), (N, Q),
        (I, K), (K, L), (L, M), (M, I),
        (A, O), (D, N), (I, P), (M, Q), (B, C),
        (A, E), (B, F), (C, G), (D, H),
    ]:
        model.set_segment(p, q)

    # Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([E, F, G, H])
    model.set_polygon([I, K, L, M])
    model.set_polygon([A, O, N, D])
    model.set_polygon([A, D, M, I])
    model.set_polygon([A, B, K, I])
    model.set_polygon([B, C, L, K])
    model.set_polygon([C, D, M, L])

    return model


if __name__ == "__main__":
    construct_0340_g1()
