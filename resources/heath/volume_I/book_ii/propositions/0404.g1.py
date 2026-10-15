"""Programmatic construction for Book II, Proposition 8 (0404.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0404_g1() -> Model:
    """Construct the figure for 0404.g1 (II.8) using geometor.model."""
    model = Model("0404.g1")

    # 1. Points
    A = model.set_point(30.0, -29.0, classes=["given"], label="A")
    C = model.set_point(152.0, -29.0, classes=["given"], label="C")
    B = model.set_point(192.0, -29.0, classes=["given"], label="B")
    D = model.set_point(232.0, -29.0, label="D")

    M = model.set_point(30.0, -69.0, label="M")
    G = model.set_point(152.0, -69.0, label="G")
    K = model.set_point(192.0, -69.0, label="K")
    N = model.set_point(232.0, -69.0, label="N")

    O = model.set_point(30.0, -109.0, label="O")
    Q = model.set_point(152.0, -109.0, label="Q")
    R = model.set_point(192.0, -109.0, label="R")
    P = model.set_point(232.0, -109.0, label="P")

    E = model.set_point(30.0, -231.0, label="E")
    H = model.set_point(152.0, -231.0, label="H")
    L = model.set_point(192.0, -231.0, label="L")
    F = model.set_point(232.0, -231.0, label="F")

    # Gnomon markers
    S = model.set_point(124.0, -109.0, label="S")
    T = model.set_point(208.0, -53.0, label="T")
    U = model.set_point(152.0, -137.0, label="U")

    # 2. Segments
    # Horizontal Row 1: A, C, B, D
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(B, D)
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(A, D)

    # Horizontal Row 2: M, G, K, N
    model.set_segment(M, G)
    model.set_segment(G, K)
    model.set_segment(K, N)
    model.set_segment(M, K)
    model.set_segment(G, N)
    model.set_segment(M, N)

    # Horizontal Row 3: O, Q, R, P
    model.set_segment(O, Q)
    model.set_segment(Q, R)
    model.set_segment(R, P)
    model.set_segment(O, R)
    model.set_segment(Q, P)
    model.set_segment(O, P)

    # Horizontal Row 4: E, H, L, F
    model.set_segment(E, H)
    model.set_segment(H, L)
    model.set_segment(L, F)
    model.set_segment(E, L)
    model.set_segment(H, F)
    model.set_segment(E, F)

    # Vertical Col 1: A, M, O, E
    model.set_segment(A, M)
    model.set_segment(M, O)
    model.set_segment(O, E)
    model.set_segment(A, O)
    model.set_segment(M, E)
    model.set_segment(A, E)

    # Vertical Col 2: C, G, Q, H
    model.set_segment(C, G)
    model.set_segment(G, Q)
    model.set_segment(Q, H)
    model.set_segment(C, Q)
    model.set_segment(G, H)
    model.set_segment(C, H)

    # Vertical Col 3: B, K, R, L
    model.set_segment(B, K)
    model.set_segment(K, R)
    model.set_segment(R, L)
    model.set_segment(B, R)
    model.set_segment(K, L)
    model.set_segment(B, L)

    # Vertical Col 4: D, N, P, F
    model.set_segment(D, N)
    model.set_segment(N, P)
    model.set_segment(P, F)
    model.set_segment(D, P)
    model.set_segment(N, F)
    model.set_segment(D, F)

    # Diagonal: D, K, Q, E
    model.set_segment(D, K)
    model.set_segment(K, Q)
    model.set_segment(Q, E)
    model.set_segment(D, Q)
    model.set_segment(K, E)
    model.set_segment(D, E)

    # 3. Polygons (Squares, Rectangles, Gnomon)
    model.set_polygon([A, E, F, D])
    model.set_polygon([O, Q, H, E])
    model.set_polygon([C, B, K, G])
    model.set_polygon([B, D, N, K])
    model.set_polygon([G, K, R, Q])
    model.set_polygon([K, N, P, R])
    model.set_polygon([C, D, P, Q])
    model.set_polygon([A, C, G, M])
    model.set_polygon([M, G, Q, O])
    model.set_polygon([Q, R, L, H])
    model.set_polygon([R, P, F, L])
    model.set_polygon([M, K, L, E])
    model.set_polygon([A, B, K, M])
    model.set_polygon([A, D, F, H, Q, O])
    model.set_polygon([S, T, U])

    return model


if __name__ == "__main__":
    construct_0404_g1()
