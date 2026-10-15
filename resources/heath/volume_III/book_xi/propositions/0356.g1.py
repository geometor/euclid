"""Programmatic construction for Book XI, Proposition 35 (0356.g1).

Two equal plane rectilineal angles BAC and EDF with elevated straight lines
AG and DM containing equal angles with the original straight lines respectively,
and perpendiculars GL, HK and MN dropped to the planes BAC and EDF.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0356_g1() -> Model:
    """Construct the two elevated angle figures for XI.35 using geometor.model."""
    model = Model("0356.g1")

    # Left figure
    A = model.set_point(sp.Rational(46, 100), sp.Rational(78, 100), classes=["given"], label="A")
    H = model.set_point(sp.Rational(126, 100), sp.Rational(146, 100), label="H")
    G = model.set_point(sp.Rational(146, 100), sp.Rational(163, 100), classes=["given"], label="G")
    K = model.set_point(sp.Rational(122, 100), sp.Rational(74, 100), label="K")
    L = model.set_point(sp.Rational(141, 100), sp.Rational(73, 100), label="L")
    B = model.set_point(sp.Rational(112, 100), sp.Rational(95, 100), classes=["given"], label="B")
    C = model.set_point(sp.Rational(104, 100), sp.Rational(34, 100), classes=["given"], label="C")

    # Right figure
    D = model.set_point(sp.Rational(248, 100), sp.Rational(62, 100), classes=["given"], label="D")
    M = model.set_point(sp.Rational(308, 100), sp.Rational(152, 100), classes=["given"], label="M")
    E = model.set_point(sp.Rational(298, 100), sp.Rational(104, 100), classes=["given"], label="E")
    N = model.set_point(sp.Rational(332, 100), sp.Rational(80, 100), label="N")
    F = model.set_point(sp.Rational(318, 100), sp.Rational(46, 100), classes=["given"], label="F")

    # Left segments and triangles
    for p1, p2 in [
        (A, H), (H, G), (A, G),
        (G, L), (H, K),
        (A, K), (K, L), (A, L),
        (A, B), (A, C), (B, C),
        (K, B), (K, C), (H, B), (H, C),
    ]:
        model.set_segment(p1, p2)

    for pts in [
        [A, B, C], [G, A, L], [H, A, K], [H, A, C], [H, A, B],
        [B, C, K], [K, A, C], [H, C, K], [H, B, K],
    ]:
        model.set_polygon(pts)

    # Right segments and triangles
    for p1, p2 in [
        (D, M), (M, N), (D, N),
        (D, E), (D, F), (E, F),
        (N, E), (N, F), (M, E), (M, F),
    ]:
        model.set_segment(p1, p2)

    for pts in [
        [D, E, F], [M, D, N], [M, D, F], [M, D, E],
        [E, F, N], [N, D, F], [M, F, N],
    ]:
        model.set_polygon(pts)

    return model


if __name__ == "__main__":
    construct_0356_g1()
