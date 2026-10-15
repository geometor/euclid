#!/usr/bin/env python3
"""
Programmatic construction for Euclid Book X, Proposition 58 (0132.g1)
using geometor.model.
"""
from geometor.model import Model


def build_model() -> Model:
    m = Model("0132.g1")

    # Left partitioned rectangle ABCD (with vertical dividers GH, EK, FL)
    A = m.set_point(17.0, 20.0, classes=["given"], label="A")
    G = m.set_point(115.5, 20.0, classes=["constructed"], label="G")
    E = m.set_point(133.5, 20.0, classes=["given"], label="E")
    F = m.set_point(176.5, 20.0, classes=["constructed"], label="F")
    D = m.set_point(218.0, 20.0, classes=["given"], label="D")

    B = m.set_point(17.0, 72.5, classes=["given"], label="B")
    H = m.set_point(115.5, 72.5, classes=["constructed"], label="H")
    K = m.set_point(133.5, 72.5, classes=["constructed"], label="K")
    L = m.set_point(176.5, 72.5, classes=["constructed"], label="L")
    C = m.set_point(218.0, 72.5, classes=["constructed"], label="C")

    # Top and bottom segments of ABCD
    m.set_segment(A, D)
    m.set_segment(A, E)
    m.set_segment(E, D)
    m.set_segment(E, F)
    m.set_segment(F, D)
    m.set_segment(A, G)
    m.set_segment(G, E)
    m.set_segment(B, C)
    m.set_segment(B, H)
    m.set_segment(H, K)
    m.set_segment(K, L)
    m.set_segment(L, C)

    # Vertical dividers of ABCD
    m.set_segment(A, B)
    m.set_segment(G, H)
    m.set_segment(E, K)
    m.set_segment(F, L)
    m.set_segment(D, C)

    # Polygons of ABCD
    m.set_polygon([A, B, C, D])  # AC
    m.set_polygon([A, B, K, E])  # AK
    m.set_polygon([A, B, H, G])  # AH
    m.set_polygon([G, H, K, E])  # GK / HE
    m.set_polygon([E, K, L, F])  # EL
    m.set_polygon([F, L, C, D])  # FC

    # Right square SQ with horizontal divider MO and vertical divider RP meeting at N
    TL = m.set_point(291.5, 20.0, classes=["constructed"], label="TL")
    R = m.set_point(363.0, 20.0, classes=["constructed"], label="R")
    Q = m.set_point(398.5, 20.0, classes=["constructed"], label="Q")

    M = m.set_point(291.5, 54.5, classes=["constructed"], label="M")
    N = m.set_point(363.0, 54.5, classes=["constructed"], label="N")
    O = m.set_point(398.5, 54.5, classes=["constructed"], label="O")

    S = m.set_point(291.5, 126.5, classes=["constructed"], label="S")
    P = m.set_point(363.0, 126.5, classes=["constructed"], label="P")
    BR = m.set_point(398.5, 126.5, classes=["constructed"], label="BR")

    # Segments of SQ
    m.set_segment(M, O)
    m.set_segment(M, N)
    m.set_segment(N, O)
    m.set_segment(R, P)
    m.set_segment(R, N)
    m.set_segment(N, P)
    m.set_segment(M, S)
    m.set_segment(S, P)
    m.set_segment(O, Q)
    m.set_segment(R, Q)

    # Polygons of SQ
    m.set_polygon([TL, S, BR, Q])  # SQ
    m.set_polygon([M, S, P, N])    # SN (square on MN)
    m.set_polygon([N, O, Q, R])    # NQ (square on NO)
    m.set_polygon([TL, M, N, R])   # MR (rectangle MN, NO)
    m.set_polygon([N, P, BR, O])   # NP (rectangle MN, NO)

    return m


if __name__ == "__main__":
    model = build_model()
    print(f"Constructed {model.name} with {len(model)} elements.")
