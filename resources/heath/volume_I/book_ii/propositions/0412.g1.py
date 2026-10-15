"""Programmatic construction for Book II, Proposition 10 combined proof (0412.g1).

Visual proof that twice the squares on AD, DB are equal to the squares on AB, CD.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0412_g1() -> Model:
    """Construct figure 0412.g1 for Book II, Proposition 10."""
    model = Model("0412.g1")

    # Let AD, DB be the two given straight lines (AD > DB) in one straight line,
    # and make AC = DB. Take AC = DB = 1, CD = 3 -> AD = CB = 4, AB = 5.
    A = model.set_point(0, 5, classes=["given"], label="A")
    C = model.set_point(1, 5, classes=["given"], label="C")
    D = model.set_point(4, 5, classes=["given"], label="D")
    B = model.set_point(5, 5, classes=["given"], label="B")

    # Outer square ABEF of side AB = 5
    F = model.set_point(0, 0, label="F")
    E = model.set_point(5, 0, label="E")

    # Interior square GHKL of side CD = 3
    G = model.set_point(1, 4, label="G")
    H = model.set_point(4, 4, label="H")
    K = model.set_point(4, 1, label="K")
    L = model.set_point(1, 1, label="L")

    # Border divider endpoints
    M = model.set_point(0, 4, label="M")
    N = model.set_point(0, 1, label="N")
    P = model.set_point(5, 4, label="P")
    Q = model.set_point(5, 1, label="Q")
    R = model.set_point(1, 0, label="R")
    S = model.set_point(4, 0, label="S")

    # Segments on top line AB
    model.set_segment(A, C)
    model.set_segment(C, D)
    model.set_segment(D, B)
    model.set_segment(A, D)
    model.set_segment(C, B)
    model.set_segment(A, B)

    # Vertical and horizontal grid segments
    model.set_segment(C, G)
    model.set_segment(D, H)
    model.set_segment(A, F)
    model.set_segment(F, E)
    model.set_segment(B, E)
    model.set_segment(M, P)
    model.set_segment(N, Q)
    model.set_segment(C, R)
    model.set_segment(D, S)

    # Polygons (squares and rectangles)
    model.set_polygon([A, B, E, F])  # Large square AE on AB
    model.set_polygon([G, H, K, L])  # Inner square GK on CD
    model.set_polygon([A, D, K, N])  # Square AK on AD
    model.set_polygon([M, H, S, F])  # Square FH on AD
    model.set_polygon([C, B, Q, L])  # Square BL on CB
    model.set_polygon([A, C, G, M])  # Small square AG on AC
    model.set_polygon([D, B, P, H])  # Small square BH on DB
    model.set_polygon([K, Q, E, S])  # Small square EK on DB
    model.set_polygon([N, L, R, F])  # Small square FL on AC

    return model


if __name__ == "__main__":
    construct_0412_g1()
