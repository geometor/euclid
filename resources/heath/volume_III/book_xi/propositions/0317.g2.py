"""Programmatic construction for Book XI, Proposition 22 Figure 2 (0317.g2).

On the straight line HK, and at the point H on it, construct the angle KHL equal
to the angle ABC, make HL equal to HK, and join KL, GL.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0317_g2() -> Model:
    """Construct Figure 2 for Book XI, Proposition 22 using geometor.model."""
    model = Model("0317.g2")

    # 1. Triangle GHK with angle KHL constructed on HK equal to angle ABC,
    #    HL made equal to HK, and KL, GL joined.
    H = model.set_point(0, 1, classes=["given"], label="H")
    G = model.set_point(sp.Rational(-32, 121), 0, classes=["given"], label="G")
    K = model.set_point(sp.Rational(41, 121), sp.Rational(4, 121), classes=["given"], label="K")
    L = model.set_point(sp.Rational(118, 121), sp.Rational(85, 121), label="L")

    # Segments
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(G, K)
    model.set_segment(H, L)
    model.set_segment(K, L)
    model.set_segment(G, L)

    # Triangles
    model.set_polygon([G, H, K])
    model.set_polygon([K, H, L])
    model.set_polygon([G, H, L])
    model.set_polygon([G, K, L])

    return model


if __name__ == "__main__":
    construct_0317_g2()
