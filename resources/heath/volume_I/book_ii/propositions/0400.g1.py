"""Programmatic construction for Book II, Proposition 6 (0400.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0400_g1() -> Model:
    """Construct the figure for 0400.g1 (II.6) using geometor.model."""
    model = Model("0400.g1")

    # 1. Points
    A = model.set_point(18.5, -29.5, classes=["given"], label="A")
    C = model.set_point(112.5, -29.5, classes=["given"], label="C")
    B = model.set_point(207.5, -29.5, classes=["given"], label="B")
    D = model.set_point(244.5, -29.5, classes=["given"], label="D")

    K = model.set_point(18.5, -68.5, label="K")
    L = model.set_point(112.5, -68.5, label="L")
    H = model.set_point(207.5, -68.5, label="H")
    M = model.set_point(244.5, -68.5, label="M")

    E = model.set_point(112.5, -164.5, label="E")
    G = model.set_point(207.5, -164.5, label="G")
    F = model.set_point(244.5, -164.5, label="F")

    # Gnomon markers
    N = model.set_point(160.0, -49.0, label="N")
    O = model.set_point(225.0, -50.0, label="O")
    P = model.set_point(226.0, -116.0, label="P")

    # 2. Segments
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(B, D)
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(A, D)

    model.set_segment(K, L)
    model.set_segment(L, H)
    model.set_segment(H, M)
    model.set_segment(K, H)
    model.set_segment(L, M)
    model.set_segment(K, M)

    model.set_segment(E, G)
    model.set_segment(G, F)
    model.set_segment(E, F)

    model.set_segment(A, K)
    model.set_segment(C, L)
    model.set_segment(L, E)
    model.set_segment(C, E)
    model.set_segment(B, H)
    model.set_segment(H, G)
    model.set_segment(B, G)
    model.set_segment(D, M)
    model.set_segment(M, F)
    model.set_segment(D, F)

    model.set_segment(D, H)
    model.set_segment(H, E)
    model.set_segment(D, E)

    # 3. Collinear Sections
    model.set_section([A, C, B])
    model.set_section([C, B, D])
    model.set_section([A, B, D])
    model.set_section([K, L, H])
    model.set_section([L, H, M])
    model.set_section([E, G, F])
    model.set_section([C, L, E])
    model.set_section([B, H, G])
    model.set_section([D, M, F])
    model.set_section([D, H, E])

    # 4. Polygons (Rectangles, Squares, Gnomon)
    model.set_polygon([C, E, F, D])
    model.set_polygon([A, C, L, K])
    model.set_polygon([C, L, H, B])
    model.set_polygon([B, H, M, D])
    model.set_polygon([C, L, M, D])
    model.set_polygon([A, K, M, D])
    model.set_polygon([L, E, G, H])
    model.set_polygon([H, G, F, M])
    model.set_polygon([C, D, F, G, H, L])
    model.set_polygon([N, O, P])

    return model


if __name__ == "__main__":
    construct_0400_g1()
