"""Programmatic construction for Book II, Proposition 9 commentary (0408.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0408_g2() -> Model:
    """Construct the figure for 0408.g2 (II.9 geometrical algebra proof) using geometor.model."""
    model = Model("0408.g2")

    # 1. Points
    A = model.set_point(25.0, -29.0, classes=["given"], label="A")
    C = model.set_point(122.0, -29.0, classes=["given"], label="C")
    D = model.set_point(147.0, -29.0, classes=["given"], label="D")
    B = model.set_point(218.0, -29.0, classes=["given"], label="B")

    K = model.set_point(25.0, -54.0, label="K")
    R = model.set_point(122.0, -54.0, label="R")
    H = model.set_point(147.0, -54.0, label="H")

    O = model.set_point(25.0, -79.0, label="O")
    P = model.set_point(97.0, -79.0, label="P")
    N = model.set_point(122.0, -79.0, label="N")
    L = model.set_point(147.0, -79.0, label="L")

    G = model.set_point(147.0, -100.0, label="G")
    S = model.set_point(218.0, -100.0, label="S")

    F = model.set_point(25.0, -151.0, label="F")
    Q = model.set_point(97.0, -151.0, label="Q")
    M = model.set_point(122.0, -151.0, label="M")
    E = model.set_point(147.0, -151.0, label="E")

    # 2. Segments
    model.set_segment(A, C)
    model.set_segment(C, D)
    model.set_segment(D, B)
    model.set_segment(A, D)
    model.set_segment(C, B)
    model.set_segment(A, B)

    model.set_segment(K, R)
    model.set_segment(R, H)
    model.set_segment(K, H)

    model.set_segment(O, P)
    model.set_segment(P, N)
    model.set_segment(N, L)
    model.set_segment(O, N)
    model.set_segment(P, L)
    model.set_segment(O, L)

    model.set_segment(G, S)

    model.set_segment(F, Q)
    model.set_segment(Q, M)
    model.set_segment(M, E)
    model.set_segment(F, M)
    model.set_segment(Q, E)
    model.set_segment(F, E)

    model.set_segment(A, K)
    model.set_segment(K, O)
    model.set_segment(O, F)
    model.set_segment(A, F)

    model.set_segment(P, Q)

    model.set_segment(C, R)
    model.set_segment(R, N)
    model.set_segment(N, M)
    model.set_segment(C, N)
    model.set_segment(C, M)

    model.set_segment(D, H)
    model.set_segment(H, L)
    model.set_segment(L, G)
    model.set_segment(G, E)
    model.set_segment(H, E)
    model.set_segment(L, E)
    model.set_segment(D, L)
    model.set_segment(D, G)
    model.set_segment(D, E)

    model.set_segment(B, S)

    # 3. Collinear Sections
    model.set_section([A, C, D])
    model.set_section([C, D, B])
    model.set_section([A, D, B])
    model.set_section([O, P, N])
    model.set_section([P, N, L])
    model.set_section([O, N, L])
    model.set_section([C, N, M])
    model.set_section([D, H, L])
    model.set_section([H, L, E])
    model.set_section([D, H, E])

    # 4. Polygons (Squares & Rectangles)
    model.set_polygon([A, D, E, F])
    model.set_polygon([D, B, S, G])
    model.set_polygon([A, D, H, K])
    model.set_polygon([K, H, L, O])
    model.set_polygon([O, N, M, F])
    model.set_polygon([O, P, Q, F])
    model.set_polygon([P, N, M, Q])
    model.set_polygon([N, L, E, M])
    model.set_polygon([C, D, H, R])
    model.set_polygon([R, H, L, N])
    model.set_polygon([C, D, L, N])

    return model


if __name__ == "__main__":
    construct_0408_g2()
