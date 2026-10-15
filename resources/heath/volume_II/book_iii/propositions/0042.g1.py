"""Programmatic construction for Book III, Proposition 15 (0042.g1).

Of straight lines in a circle the diameter is greatest, and of the rest the
nearer to the centre is always greater than the more remote.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0042_g1() -> Model:
    """Construct the figure for Book III, Proposition 15 using geometor.model."""
    model = Model("0042.g1")

    # 1. Circle ABCD about centre E with diameter AD
    E = model.set_point(0, 0, classes=["given"], label="E")
    A = model.set_point(0, 1, classes=["given"], label="A")
    D = model.set_point(0, -1, classes=["given"], label="D")
    circle_ABCD = model.construct_circle(E, A)

    model.set_segment(A, E)
    model.set_segment(E, D)
    model.set_segment(A, D)
    model.set_section([A, E, D])

    # 2. Perpendicular EH to nearer chord BC
    H = model.set_point(sp.Rational(35, 76), sp.Rational(-5, 76), label="H")
    half_BC = sp.sqrt(1 - H.x**2 - H.y**2)
    len_EH = sp.sqrt(H.x**2 + H.y**2)
    ux_BC = -H.y / len_EH
    uy_BC = H.x / len_EH

    B = model.set_point(H.x + half_BC * ux_BC, H.y + half_BC * uy_BC, label="B")
    C = model.set_point(H.x - half_BC * ux_BC, H.y - half_BC * uy_BC, label="C")

    model.set_segment(E, H)
    model.set_segment(B, H)
    model.set_segment(H, C)
    model.set_segment(B, C)
    model.set_section([B, H, C])

    # 3. Perpendicular EK to more remote chord FG
    K = model.set_point(sp.Rational(-57, 76), sp.Rational(6, 76), label="K")
    half_FG = sp.sqrt(1 - K.x**2 - K.y**2)
    len_EK = sp.sqrt(K.x**2 + K.y**2)
    ux_FG = -K.y / len_EK
    uy_FG = K.x / len_EK

    F = model.set_point(K.x + half_FG * ux_FG, K.y + half_FG * uy_FG, label="F")
    G = model.set_point(K.x - half_FG * ux_FG, K.y - half_FG * uy_FG, label="G")

    # 4. Point L on EK with EL = EH, and chord MN through L perpendicular to EK
    L = model.set_point(K.x * len_EH / len_EK, K.y * len_EH / len_EK, label="L")
    M = model.set_point(L.x + half_BC * ux_FG, L.y + half_BC * uy_FG, label="M")
    N = model.set_point(L.x - half_BC * ux_FG, L.y - half_BC * uy_FG, label="N")

    model.set_segment(E, L)
    model.set_segment(L, K)
    model.set_segment(E, K)
    model.set_section([E, L, K])

    model.set_segment(F, K)
    model.set_segment(K, G)
    model.set_segment(F, G)
    model.set_section([F, K, G])

    model.set_segment(M, L)
    model.set_segment(L, N)
    model.set_segment(M, N)
    model.set_section([M, L, N])

    # 5. Radii ME, EN, FE, EG and triangles MEN, FEG
    model.set_segment(M, E)
    model.set_segment(E, N)
    model.set_segment(F, E)
    model.set_segment(E, G)

    model.set_polygon([M, E, N])
    model.set_polygon([F, E, G])

    return model


if __name__ == "__main__":
    construct_0042_g1()
