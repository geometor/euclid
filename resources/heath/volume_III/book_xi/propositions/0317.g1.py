"""Programmatic construction for Book XI, Proposition 22 Figure 1 (0317.g1).

Three plane angles ABC, DEF, GHK of which any two are greater than the remaining
one, contained by equal straight lines AB, BC, DE, EF, GH, HK, with bases AC,
DF, GK joined.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0317_g1() -> Model:
    """Construct Figure 1 for Book XI, Proposition 22 using geometor.model."""
    model = Model("0317.g1")

    # 1. Three plane angles ABC, DEF, GHK contained by equal straight lines
    #    AB, BC, DE, EF, GH, HK, with bases AC, DF, GK joined.
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(sp.Rational(67, 130), sp.Rational(108, 130), classes=["given"], label="B")
    C = model.set_point(1, 0, classes=["given"], label="C")

    D = model.set_point(sp.Rational(170, 130), 0, classes=["given"], label="D")
    E = model.set_point(sp.Rational(255, 130), sp.Rational(94, 130), classes=["given"], label="E")
    F = model.set_point(sp.Rational(337, 130), 0, classes=["given"], label="F")

    G = model.set_point(sp.Rational(378, 130), 0, classes=["given"], label="G")
    H = model.set_point(sp.Rational(414, 130), sp.Rational(116, 130), classes=["given"], label="H")
    K = model.set_point(sp.Rational(453, 130), 0, classes=["given"], label="K")

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, C)

    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(D, F)

    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(G, K)

    # Triangles
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([G, H, K])

    return model


if __name__ == "__main__":
    construct_0317_g1()
