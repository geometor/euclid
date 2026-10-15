"""Programmatic construction for Book X, Proposition 59 (0134.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0134_g1() -> Model:
    """Construct the figure 0134.g1 using geometor.model."""
    model = Model("0134.g1")

    # Rectangular area ABCD on the left, divided by GH, EK, FL
    A = model.set_point(18.0, -16.5, classes=["given"], label="A")
    G = model.set_point(117.5, -16.5, label="G")
    E = model.set_point(135.5, -16.5, classes=["given"], label="E")
    F = model.set_point(177.0, -16.5, label="F")
    D = model.set_point(219.0, -16.5, classes=["given"], label="D")

    B = model.set_point(18.0, -68.5, classes=["given"], label="B")
    H = model.set_point(117.5, -68.5, label="H")
    K = model.set_point(135.5, -68.5, label="K")
    L = model.set_point(177.0, -68.5, label="L")
    C = model.set_point(219.0, -68.5, classes=["given"], label="C")

    # Square SQ on the right, divided by MO and RP at N
    T_tl = model.set_point(299.0, -19.5, label="T_tl")
    R = model.set_point(370.5, -19.5, label="R")
    Q = model.set_point(405.5, -19.5, label="Q")

    M = model.set_point(299.0, -56.0, label="M")
    N = model.set_point(370.5, -56.0, label="N")
    O = model.set_point(405.5, -56.0, label="O")

    S = model.set_point(299.0, -127.5, label="S")
    P = model.set_point(370.5, -127.5, label="P")
    T_br = model.set_point(405.5, -127.5, label="T_br")

    # Base lines
    model.construct_line(A, D)
    model.construct_line(B, C)
    model.construct_line(A, B)
    model.construct_line(G, H)
    model.construct_line(E, K)
    model.construct_line(F, L)
    model.construct_line(D, C)

    model.construct_line(T_tl, Q)
    model.construct_line(M, O)
    model.construct_line(S, T_br)
    model.construct_line(T_tl, S)
    model.construct_line(R, P)
    model.construct_line(Q, T_br)

    # Segments on rectangle ABCD
    model.set_segment(A, D)
    model.set_segment(A, G)
    model.set_segment(A, E)
    model.set_segment(A, F)
    model.set_segment(G, E)
    model.set_segment(G, F)
    model.set_segment(G, D)
    model.set_segment(E, F)
    model.set_segment(E, D)
    model.set_segment(F, D)

    model.set_segment(B, C)
    model.set_segment(B, H)
    model.set_segment(B, K)
    model.set_segment(B, L)
    model.set_segment(H, K)
    model.set_segment(H, L)
    model.set_segment(H, C)
    model.set_segment(K, L)
    model.set_segment(K, C)
    model.set_segment(L, C)

    model.set_segment(A, B)
    model.set_segment(G, H)
    model.set_segment(E, K)
    model.set_segment(F, L)
    model.set_segment(D, C)

    # Segments on square SQ
    model.set_segment(T_tl, Q)
    model.set_segment(T_tl, R)
    model.set_segment(R, Q)
    model.set_segment(M, O)
    model.set_segment(M, N)
    model.set_segment(N, O)
    model.set_segment(S, T_br)
    model.set_segment(S, P)
    model.set_segment(P, T_br)

    model.set_segment(T_tl, S)
    model.set_segment(T_tl, M)
    model.set_segment(M, S)
    model.set_segment(R, P)
    model.set_segment(R, N)
    model.set_segment(N, P)
    model.set_segment(Q, T_br)
    model.set_segment(Q, O)
    model.set_segment(O, T_br)

    # Sections
    model.set_section([A, E, D])
    model.set_section([A, G, E])
    model.set_section([E, F, D])
    model.set_section([M, N, O])
    model.set_section([R, N, P])

    # Polygons on ABCD
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B, K, E])
    model.set_polygon([A, B, H, G])
    model.set_polygon([G, H, K, E])
    model.set_polygon([E, K, C, D])
    model.set_polygon([E, K, L, F])
    model.set_polygon([F, L, C, D])
    model.set_polygon([A, B, L, F])
    model.set_polygon([G, H, C, D])

    # Polygons on SQ
    model.set_polygon([T_tl, S, T_br, Q])
    model.set_polygon([M, S, P, N])
    model.set_polygon([N, R, Q, O])
    model.set_polygon([T_tl, M, N, R])
    model.set_polygon([N, P, T_br, O])

    return model


if __name__ == "__main__":
    construct_0134_g1()
