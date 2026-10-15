"""Programmatic construction for Book II, Proposition 10 alternative figure (0411.g1).

Geometrical-algebra demonstration that the squares on AD, DB are double of the
squares on AC, CD.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0411_g1() -> Model:
    """Construct the alternative figure 0411.g1 for Book II, Proposition 10."""
    model = Model("0411.g1")

    # Top side AD with AB bisected at C and BD added
    # AC = 2, CB = 2, BD = 1 -> CD = 3, AD = 5
    A = model.set_point(0, 5, classes=["given"], label="A")
    C = model.set_point(2, 5, classes=["given"], label="C")
    B = model.set_point(4, 5, classes=["given"], label="B")
    D = model.set_point(5, 5, classes=["given"], label="D")

    # Outer square ADEF on AD (side = 5)
    F = model.set_point(0, 0, label="F")
    E = model.set_point(5, 0, label="E")

    # First horizontal divider at distance BD = 1 below AD (y = 4)
    L = model.set_point(0, 4, label="L")
    H = model.set_point(2, 4, label="H")
    M = model.set_point(4, 4, label="M")
    G = model.set_point(5, 4, label="G")

    # Second horizontal divider at distance CD = 3 below AD (y = 2)
    N = model.set_point(0, 2, label="N")
    K = model.set_point(2, 2, label="K")
    P = model.set_point(5, 2, label="P")

    # Bottom divider point below C (x = 2, y = 0)
    Q = model.set_point(2, 0, label="Q")

    # Segments along top edge AD
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(B, D)
    model.set_segment(A, B)
    model.set_segment(C, D)

    # Outer square sides and internal dividers
    model.set_segment(A, F)
    model.set_segment(F, E)
    model.set_segment(D, E)
    model.set_segment(L, G)
    model.set_segment(N, P)
    model.set_segment(C, Q)
    model.set_segment(B, M)

    # Polygons (squares and rectangles)
    model.set_polygon([A, D, E, F])  # Square on AD
    model.set_polygon([A, C, H, L])  # Rectangle AH
    model.set_polygon([C, B, M, H])  # Rectangle BH
    model.set_polygon([B, D, G, M])  # Square BG (on BD)
    model.set_polygon([L, H, K, N])  # First square on AC
    model.set_polygon([N, K, Q, F])  # Second square on AC
    model.set_polygon([H, G, P, K])  # Rectangle GK
    model.set_polygon([K, P, E, Q])  # Rectangle KE
    model.set_polygon([C, D, P, K])  # Square on CD

    return model


if __name__ == "__main__":
    construct_0411_g1()
