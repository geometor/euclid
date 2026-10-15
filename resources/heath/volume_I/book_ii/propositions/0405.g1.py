"""Programmatic construction for Book II, Proposition 8 commentary (0405.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0405_g1() -> Model:
    """Construct the figure for 0405.g1 (II.8 alternate proof) using geometor.model."""
    model = Model("0405.g1")

    # 1. Points
    D = model.set_point(26.0, -28.0, classes=["given"], label="D")
    A = model.set_point(69.0, -28.0, classes=["given"], label="A")
    C = model.set_point(136.0, -28.0, classes=["given"], label="C")
    B = model.set_point(179.0, -28.0, classes=["given"], label="B")

    L = model.set_point(69.0, -71.0, label="L")
    M = model.set_point(136.0, -71.0, label="M")
    G = model.set_point(179.0, -71.0, label="G")

    K = model.set_point(26.0, -138.0, label="K")
    P = model.set_point(69.0, -138.0, label="P")
    N = model.set_point(136.0, -138.0, label="N")

    F = model.set_point(26.0, -181.0, label="F")
    H = model.set_point(136.0, -181.0, label="H")
    E = model.set_point(179.0, -181.0, label="E")

    # 2. Segments
    model.set_segment(D, A)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(D, C)
    model.set_segment(A, B)
    model.set_segment(D, B)

    model.set_segment(B, G)
    model.set_segment(G, E)
    model.set_segment(B, E)

    model.set_segment(E, H)
    model.set_segment(H, F)
    model.set_segment(E, F)

    model.set_segment(F, K)
    model.set_segment(K, D)
    model.set_segment(F, D)

    # Pinwheel internal segments: ALP, HNM, GML, KPN
    model.set_segment(A, L)
    model.set_segment(L, P)
    model.set_segment(A, P)

    model.set_segment(H, N)
    model.set_segment(N, M)
    model.set_segment(H, M)

    model.set_segment(G, M)
    model.set_segment(M, L)
    model.set_segment(G, L)

    model.set_segment(K, P)
    model.set_segment(P, N)
    model.set_segment(K, N)

    # 3. Collinear Sections
    model.set_section([D, A, B])
    model.set_section([A, C, B])
    model.set_section([A, L, P])
    model.set_section([H, N, M])
    model.set_section([G, M, L])
    model.set_section([K, P, N])

    # 4. Polygons (Outer square, inner square, 4 pinwheel rectangles)
    model.set_polygon([B, E, F, D])
    model.set_polygon([L, M, N, P])
    model.set_polygon([A, B, G, L])
    model.set_polygon([D, A, P, K])
    model.set_polygon([K, N, H, F])
    model.set_polygon([M, G, E, H])

    return model


if __name__ == "__main__":
    construct_0405_g1()
