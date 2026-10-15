"""Programmatic construction for Book I, I.43 (0355.g2).

Proclus' commentary on I.43: overlapping parallelograms about the diameter.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0355_g2() -> Model:
    """Construct the figure for 0355.g2 (I.43) using geometor.model."""
    model = Model("0355.g2")

    # 1. Points
    A = model.set_point(45, -26, classes=["given"], label="A")
    B = model.set_point(17, -101, classes=["given"], label="B")
    C = model.set_point(157, -101, classes=["given"], label="C")
    D = model.set_point(185, -26, classes=["given"], label="D")
    E = model.set_point(27.5, -73, label="E")
    F = model.set_point(131, -26, label="F")
    G = model.set_point(178.3, -44, label="G")
    H = model.set_point(46, -101, label="H")
    K = model.set_point(67.3, -44, label="K")
    L = model.set_point(56.5, -73, label="L")
    M = model.set_point(113.5, -73, label="M")
    N = model.set_point(124.3, -44, label="N")

    # 3. Segments
    model.set_segment(A, D)
    model.set_segment(A, F)
    model.set_segment(F, D)
    model.set_segment(K, G)
    model.set_segment(K, N)
    model.set_segment(N, G)
    model.set_segment(E, M)
    model.set_segment(E, L)
    model.set_segment(L, M)
    model.set_segment(B, C)
    model.set_segment(B, H)
    model.set_segment(H, C)
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(K, H)
    model.set_segment(K, L)
    model.set_segment(L, H)
    model.set_segment(F, M)
    model.set_segment(F, N)
    model.set_segment(N, M)
    model.set_segment(D, C)
    model.set_segment(D, G)
    model.set_segment(G, C)
    model.set_segment(A, C)
    model.set_segment(K, M)

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C, D])
    model.set_polygon([F, N, G, D])
    model.set_polygon([E, B, H, L])
    model.set_polygon([A, E, M, F])
    model.set_polygon([K, H, C, G])
    model.set_polygon([K, L, M, N])
    model.set_polygon([L, M, N])
    model.set_polygon([K, M, N])

    return model


if __name__ == "__main__":
    construct_0355_g2()
