"""Programmatic construction for Book I, I.44 (0356.g1).

To a given straight line to apply, in a given rectilineal angle, a parallelogram equal to a given triangle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0356_g1() -> Model:
    """Construct the figure for 0356.g1 (I.44) using geometor.model."""
    model = Model("0356.g1")

    # 1. Points
    H = model.set_point(225, -20, label="H")
    G = model.set_point(338, -20, label="G")
    F = model.set_point(375, -20, label="F")
    A = model.set_point(204, -96, classes=["given"], label="A")
    B = model.set_point(316, -96, classes=["given"], label="B")
    E = model.set_point(353, -96, label="E")
    L = model.set_point(196, -121, label="L")
    M = model.set_point(308, -121, label="M")
    K = model.set_point(345, -121, label="K")
    C1 = model.set_point(36, -23, classes=["given"], label="C1")
    C2 = model.set_point(10, -97, classes=["given"], label="C2")
    C3 = model.set_point(89, -97, classes=["given"], label="C3")
    D = model.set_point(184, -76, classes=["given"], label="D")
    D1 = model.set_point(176, -23, label="D1")
    D2 = model.set_point(129, -109, label="D2")

    # 3. Segments
    model.set_segment(C1, C2)
    model.set_segment(C2, C3)
    model.set_segment(C3, C1)
    model.set_segment(D, D1)
    model.set_segment(D, D2)
    model.set_segment(H, F)
    model.set_segment(H, G)
    model.set_segment(F, G)
    model.set_segment(A, E)
    model.set_segment(A, B)
    model.set_segment(B, E)
    model.set_segment(L, K)
    model.set_segment(L, M)
    model.set_segment(M, K)
    model.set_segment(H, L)
    model.set_segment(A, H)
    model.set_segment(A, L)
    model.set_segment(G, M)
    model.set_segment(B, G)
    model.set_segment(B, M)
    model.set_segment(F, K)
    model.set_segment(E, F)
    model.set_segment(E, K)
    model.set_segment(H, K)
    model.set_segment(H, B)
    model.set_segment(B, K)

    # 4. Collinear Sections
    model.set_section([H, G, F])
    model.set_section([A, B, E])
    model.set_section([L, M, K])
    model.set_section([H, A, L])
    model.set_section([G, B, M])
    model.set_section([F, E, K])
    model.set_section([H, B, K])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([C1, C2, C3])
    model.set_polygon([B, E, F, G])
    model.set_polygon([A, B, M, L])
    model.set_polygon([H, A, B, G])
    model.set_polygon([B, M, K, E])
    model.set_polygon([H, L, K, F])

    # 6. Angles (Wedges)
    model.set_wedge(D, D1, D1, D2)
    model.set_wedge(B, E, E, G)
    model.set_wedge(H, A, A, F)
    model.set_wedge(F, H, H, E)
    model.set_wedge(H, B, B, G)
    model.set_wedge(F, G, G, E)
    model.set_wedge(B, A, A, M)

    return model


if __name__ == "__main__":
    construct_0356_g1()
