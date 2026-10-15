"""Programmatic construction for Book I, I.45 (0359.g1).

To construct, in a given rectilineal angle, a parallelogram equal to a given rectilineal figure.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0359_g1() -> Model:
    """Construct the figure for 0359.g1 (I.45) using geometor.model."""
    model = Model("0359.g1")

    # 1. Points
    A = model.set_point(31, -50, classes=["given"], label="A")
    D = model.set_point(149, -27, classes=["given"], label="D")
    B = model.set_point(149, -120, classes=["given"], label="B")
    C = model.set_point(230, -52, classes=["given"], label="C")
    E = model.set_point(244, -93, classes=["given"], label="E")
    E1 = model.set_point(266, -51, label="E1")
    E2 = model.set_point(295, -102, label="E2")
    F = model.set_point(385, -35, label="F")
    G = model.set_point(456, -35, label="G")
    L = model.set_point(498, -35, label="L")
    K = model.set_point(363, -117, label="K")
    H = model.set_point(434, -117, label="H")
    M = model.set_point(476, -117, label="M")

    # 3. Segments
    model.set_segment(A, D)
    model.set_segment(A, B)
    model.set_segment(D, C)
    model.set_segment(B, C)
    model.set_segment(D, B)
    model.set_segment(E, E1)
    model.set_segment(E, E2)
    model.set_segment(F, L)
    model.set_segment(F, G)
    model.set_segment(G, L)
    model.set_segment(K, M)
    model.set_segment(K, H)
    model.set_segment(H, M)
    model.set_segment(F, K)
    model.set_segment(G, H)
    model.set_segment(L, M)

    # 4. Collinear Sections
    model.set_section([F, G, L])
    model.set_section([K, H, M])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B, D])
    model.set_polygon([D, B, C])
    model.set_polygon([F, K, H, G])
    model.set_polygon([G, H, M, L])
    model.set_polygon([K, F, L, M])

    # 6. Angles (Wedges)
    model.set_wedge(E, E1, E1, E2)
    model.set_wedge(K, H, H, F)
    model.set_wedge(H, G, G, M)
    model.set_wedge(H, K, K, G)
    model.set_wedge(G, H, H, F)
    model.set_wedge(G, H, H, L)

    return model


if __name__ == "__main__":
    construct_0359_g1()
