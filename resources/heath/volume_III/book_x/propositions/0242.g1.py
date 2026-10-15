"""Programmatic construction for Book X, Proposition 110 (0242.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0242_g1() -> Model:
    """Construct the figure 0242.g1 using geometor.model."""
    model = Model("0242.g1")

    # Left rectangle B-E-C_t / A-D-C
    B = model.set_point(22.0, -48.0, classes=["given"], label="B")
    E = model.set_point(93.5, -48.0, label="E")
    C_t = model.set_point(134.5, -48.0, label="C_t")
    A = model.set_point(22.0, -130.5, classes=["given"], label="A")
    D = model.set_point(93.5, -130.5, label="D")
    C = model.set_point(134.5, -130.5, classes=["given"], label="C")

    # Right rectangle F-K-H / G-L-H_b
    F = model.set_point(277.0, -18.5, classes=["given"], label="F")
    K = model.set_point(315.0, -18.5, label="K")
    H = model.set_point(336.5, -18.5, label="H")
    G = model.set_point(277.0, -177.5, classes=["given"], label="G")
    L = model.set_point(315.0, -177.5, label="L")
    H_b = model.set_point(336.5, -177.5, label="H_b")

    # Base lines
    model.construct_line(B, C_t)
    model.construct_line(A, C)
    model.construct_line(B, A)
    model.construct_line(E, D)
    model.construct_line(C_t, C)

    model.construct_line(F, H)
    model.construct_line(G, H_b)
    model.construct_line(F, G)
    model.construct_line(K, L)
    model.construct_line(H, H_b)

    # Segments
    model.set_segment(B, A)
    model.set_segment(E, D)
    model.set_segment(C_t, C)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(B, E)
    model.set_segment(E, C_t)
    model.set_segment(B, C_t)

    model.set_segment(F, G)
    model.set_segment(K, L)
    model.set_segment(H, H_b)
    model.set_segment(F, H)
    model.set_segment(F, K)
    model.set_segment(K, H)
    model.set_segment(G, L)
    model.set_segment(L, H_b)
    model.set_segment(G, H_b)

    # Sections
    model.set_section([A, D, C])
    model.set_section([F, K, H])

    # Polygons (rectangles)
    model.set_polygon([B, C_t, C, A])  # BC
    model.set_polygon([B, E, D, A])    # BD
    model.set_polygon([E, C_t, C, D])  # EC
    model.set_polygon([F, H, H_b, G])  # GH
    model.set_polygon([F, K, L, G])    # GK / FL
    model.set_polygon([K, H, H_b, L])  # LH

    return model


if __name__ == "__main__":
    construct_0242_g1()
