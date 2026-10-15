"""Programmatic construction for Book XI, Proposition 29 (0337.g2).

Parallelepipedal solids CM and CN on the same base AB (ACBL) and of the same height,
with the extremities of their standing sides on the same straight lines FN and DK.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0337_g2() -> Model:
    """Construct the two parallelepipeds CM and CN for Book XI, Proposition 29."""
    model = Model("0337.g2")

    # Top back collinear line DK
    D = model.set_point(sp.Rational(24, 100), sp.Rational(185, 100), classes=["given"], label="D")
    E = model.set_point(sp.Rational(88, 100), sp.Rational(185, 100), classes=["given"], label="E")
    H = model.set_point(sp.Rational(168, 100), sp.Rational(185, 100), classes=["given"], label="H")
    K = model.set_point(sp.Rational(232, 100), sp.Rational(185, 100), classes=["given"], label="K")

    # Top front collinear line FN
    F = model.set_point(sp.Rational(34, 100), sp.Rational(161, 100), classes=["given"], label="F")
    G = model.set_point(sp.Rational(98, 100), sp.Rational(161, 100), classes=["given"], label="G")
    M = model.set_point(sp.Rational(178, 100), sp.Rational(161, 100), classes=["given"], label="M")
    N = model.set_point(sp.Rational(242, 100), sp.Rational(161, 100), classes=["given"], label="N")

    # Base parallelogram ACBL
    C = model.set_point(sp.Rational(80, 100), sp.Rational(74, 100), classes=["given"], label="C")
    B = model.set_point(sp.Rational(224, 100), sp.Rational(74, 100), classes=["given"], label="B")
    A = model.set_point(sp.Rational(74, 100), sp.Rational(40, 100), classes=["given"], label="A")
    L = model.set_point(sp.Rational(218, 100), sp.Rational(40, 100), classes=["given"], label="L")

    # Collinear sub-segments on DK and FN
    for p, q in [
        (D, K), (D, H), (E, K), (E, H), (D, E), (H, K),
        (F, N), (F, M), (G, N), (G, M), (F, G), (M, N),
    ]:
        model.set_segment(p, q)

    # Standing edges and base/top transverse edges
    for p, q in [
        (C, B), (A, L), (A, C), (B, L),
        (D, F), (E, G), (H, M), (K, N),
        (A, G), (A, F), (L, M), (L, N),
        (C, D), (C, E), (B, H), (B, K),
    ]:
        model.set_segment(p, q)

    # Triangles and parallelograms
    model.set_polygon([D, C, E])
    model.set_polygon([H, B, K])
    model.set_polygon([A, F, G])
    model.set_polygon([M, L, N])

    model.set_polygon([A, C, B, L])
    model.set_polygon([C, D, H, B])
    model.set_polygon([C, E, K, B])
    model.set_polygon([D, E, G, F])
    model.set_polygon([H, K, N, M])
    model.set_polygon([C, D, F, A])
    model.set_polygon([B, H, M, L])
    model.set_polygon([C, E, G, A])
    model.set_polygon([B, K, N, L])
    model.set_polygon([G, E, H, M])

    return model


if __name__ == "__main__":
    construct_0337_g2()
