"""Programmatic construction for Book IV, Proposition 12 (0108.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0108_g2() -> Model:
    """Construct the figure 0108.g2 (Circumscribed regular pentagon) using geometor.model."""
    model = Model("0108.g2")

    # Points (y-inverted for standard mathematical coordinates)
    F = model.set_point(104.00, -113.00, classes=["given"], label="F")
    A = model.set_point(67.56, -62.84, classes=["given"], label="A")
    B = model.set_point(45.03, -132.16, classes=["given"], label="B")
    C = model.set_point(104.00, -175.00, classes=["given"], label="C")
    D = model.set_point(162.97, -132.16, classes=["given"], label="D")
    E = model.set_point(140.44, -62.84, classes=["given"], label="E")

    G = model.set_point(104.00, -36.36, label="G")
    H = model.set_point(31.11, -89.32, label="H")
    K = model.set_point(58.95, -175.00, label="K")
    L = model.set_point(149.05, -175.00, label="L")
    M = model.set_point(176.89, -89.32, label="M")

    # Given circle ABCDE
    model.construct_circle(F, C)

    # Segments
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(K, L)
    model.set_segment(L, M)
    model.set_segment(M, G)
    model.set_segment(H, B)
    model.set_segment(B, K)
    model.set_segment(K, C)
    model.set_segment(C, L)
    model.set_segment(L, D)
    model.set_segment(F, B)
    model.set_segment(F, K)
    model.set_segment(F, C)
    model.set_segment(F, L)
    model.set_segment(F, D)

    # Collinear sections
    model.set_section([G, A, H])
    model.set_section([H, B, K])
    model.set_section([K, C, L])
    model.set_section([L, D, M])
    model.set_section([M, E, G])

    # Polygons
    model.set_polygon([G, H, K, L, M])
    model.set_polygon([F, B, K])
    model.set_polygon([F, K, C])
    model.set_polygon([F, L, C])
    model.set_polygon([F, D, L])

    # Angles (wedges)
    model.set_wedge(F, C, C, K)
    model.set_wedge(F, C, C, L)
    model.set_wedge(F, B, B, K)
    model.set_wedge(F, D, D, L)
    model.set_wedge(B, F, F, K)
    model.set_wedge(K, F, F, C)
    model.set_wedge(B, F, F, C)
    model.set_wedge(C, F, F, L)
    model.set_wedge(L, F, F, D)
    model.set_wedge(C, F, F, D)
    model.set_wedge(B, K, K, F)
    model.set_wedge(F, K, K, C)
    model.set_wedge(B, K, K, C)
    model.set_wedge(F, L, L, C)
    model.set_wedge(D, L, L, C)
    model.set_wedge(K, H, H, G)
    model.set_wedge(H, G, G, M)
    model.set_wedge(G, M, M, L)

    return model


if __name__ == "__main__":
    construct_0108_g2()
