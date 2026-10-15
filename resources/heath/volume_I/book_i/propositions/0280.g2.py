"""Programmatic construction for Book I, Proposition 9 Note — Quadratrix of Hippias (0280.g2).

Division of an angle EAD in any given ratio by means of the quadratrix BFLG inside
the square ABCD and circular quadrant BED centered at A.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0280_g2() -> Model:
    """Construct the figure for 0280.g2 using geometor.model."""
    model = Model("0280.g2")

    # 1. Square ABCD and circular quadrant BED centered at A
    A = model.set_point(33, -164, classes=["given"], label="A")
    B = model.set_point(33, -17, classes=["given"], label="B")
    C = model.set_point(178, -17, classes=["given"], label="C")
    D = model.set_point(178, -164, classes=["given"], label="D")

    model.set_polygon([A, B, C, D])
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(A, D)

    # 2. Radial rays A-F-E and A-L-N, and perpendiculars F-K-H, L-M, and horizontal KL
    E = model.set_point(112, -38, label="E")
    F = model.set_point(96, -52, label="F")
    N = model.set_point(154, -98, label="N")
    L = model.set_point(122, -105, label="L")
    K = model.set_point(96, -105, label="K")
    H = model.set_point(96, -164, label="H")
    M = model.set_point(122, -164, label="M")
    G = model.set_point(126, -164, label="G")

    model.set_section([A, F, E])
    model.set_segment(A, F)
    model.set_segment(F, E)
    model.set_segment(A, E)

    model.set_section([A, L, N])
    model.set_segment(A, L)
    model.set_segment(L, N)
    model.set_segment(A, N)

    model.set_section([F, K, H])
    model.set_segment(F, K)
    model.set_segment(K, H)
    model.set_segment(F, H)

    model.set_segment(K, L)
    model.set_segment(L, M)

    return model


if __name__ == "__main__":
    construct_0280_g2()
