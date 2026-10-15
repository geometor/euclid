"""Programmatic construction for Book XI, Proposition 28 Commentary (0337.g1).

Parallelepiped ABGH-DCFE cut by diagonal plane AGFD and right section KLMN
with diagonal KM dividing it into equal triangles KLM and MNK.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0337_g1() -> Model:
    """Construct the parallelepiped cut by diagonal plane and right section (0337.g1)."""
    model = Model("0337.g1")

    # Top face ABGH
    A = model.set_point(sp.Rational(30, 100), sp.Rational(162, 100), classes=["given"], label="A")
    H = model.set_point(sp.Rational(103, 100), sp.Rational(162, 100), classes=["given"], label="H")
    B = model.set_point(sp.Rational(16, 100), sp.Rational(141, 100), classes=["given"], label="B")
    G = model.set_point(sp.Rational(89, 100), sp.Rational(141, 100), classes=["given"], label="G")

    # Right section KLMN
    K = model.set_point(sp.Rational(52, 100), sp.Rational(94, 100), classes=["given"], label="K")
    L = model.set_point(sp.Rational(37, 100), sp.Rational(75, 100), classes=["given"], label="L")
    M = model.set_point(sp.Rational(106, 100), sp.Rational(88, 100), classes=["given"], label="M")
    N = model.set_point(sp.Rational(121, 100), sp.Rational(107, 100), classes=["given"], label="N")

    # Bottom face DCFE
    D = model.set_point(sp.Rational(68, 100), sp.Rational(44, 100), classes=["given"], label="D")
    E = model.set_point(sp.Rational(141, 100), sp.Rational(44, 100), classes=["given"], label="E")
    C = model.set_point(sp.Rational(54, 100), sp.Rational(23, 100), classes=["given"], label="C")
    F = model.set_point(sp.Rational(127, 100), sp.Rational(23, 100), classes=["given"], label="F")

    # Lateral edges and diagonals
    for p, q in [
        (A, D), (B, C), (G, F), (H, E),
        (A, G), (D, F), (K, M),
        (A, B), (B, G), (G, H), (H, A),
        (D, C), (C, F), (F, E), (E, D),
        (K, L), (L, M), (M, N), (N, K),
    ]:
        model.set_segment(p, q)

    # Polygons and triangles
    model.set_polygon([K, L, M, N])
    model.set_polygon([K, L, M])
    model.set_polygon([M, N, K])
    model.set_polygon([A, B, G])
    model.set_polygon([D, C, F])
    model.set_polygon([A, G, H])
    model.set_polygon([D, F, E])

    return model


if __name__ == "__main__":
    construct_0337_g1()
