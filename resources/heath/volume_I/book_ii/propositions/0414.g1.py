"""Programmatic construction for Book II, Proposition 10 side and diagonal numbers (0414.g1).

Hultsch's figure illustrating Proclus's application of Euclid II. 10 to side
and diagonal numbers.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0414_g1() -> Model:
    """Construct figure 0414.g1 for side and diagonal numbers."""
    model = Model("0414.g1")

    # Let AB = a = 1, BC = a = 1, CD = d = sqrt(2)
    # Then BD = a + d = 1 + sqrt(2), AD = 2a + d = 2 + sqrt(2)
    # DG = BD = 1 + sqrt(2), GH = AD = 2 + sqrt(2), DH = 3 + 2*sqrt(2)
    a = sp.Integer(1)
    d = sp.sqrt(2)
    a2 = a + d
    d2 = 2 * a + d
    a3 = a2 + d2

    xA = sp.Integer(0)
    xB = a
    xC = 2 * a
    xD = xB + a2
    xG = xD + a2
    xH = xD + a3

    A = model.set_point(xA, 0, classes=["given"], label="A")
    B = model.set_point(xB, 0, classes=["given"], label="B")
    C = model.set_point(xC, 0, label="C")
    D = model.set_point(xD, 0, label="D")
    G = model.set_point(xG, 0, label="G")
    H = model.set_point(xH, 0, label="H")

    # Top-left vertices of the three squares on AB, BD, DH
    E = model.set_point(xA, a, label="E")
    F = model.set_point(xB, a2, label="F")
    K = model.set_point(xD, a3, label="K")

    # Top-right vertices of the three squares
    E_rt = model.set_point(xB, a, label="E_rt")
    F_rt = model.set_point(xD, a2, label="F_rt")
    K_rt = model.set_point(xH, a3, label="K_rt")

    # Base line and collinear segments
    model.construct_line(A, H)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(A, D)
    model.set_segment(D, G)
    model.set_segment(G, H)
    model.set_segment(D, H)
    model.set_segment(A, H)

    # Diagonals BE, DF, HK
    model.set_segment(B, E)
    model.set_segment(D, F)
    model.set_segment(H, K)

    # Three squares
    model.set_polygon([A, B, E_rt, E])
    model.set_polygon([B, D, F_rt, F])
    model.set_polygon([D, H, K_rt, K])

    return model


if __name__ == "__main__":
    construct_0414_g1()
