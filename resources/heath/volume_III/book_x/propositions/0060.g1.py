"""Programmatic construction for Book X, Proposition 25 (0060.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0060_g1() -> Model:
    """Construct the figure 0060.g1 using geometor.model."""
    model = Model("0060.g1")

    # Left composite figure: square AD, rectangle AC, square BE (also called CO)
    A = model.set_point(94.0, -18.5, classes=["given"], label="A")
    B = model.set_point(94.0, -93.0, classes=["given"], label="B")
    C = model.set_point(140.0, -93.0, classes=["given"], label="C")
    D = model.set_point(19.0, -93.0, label="D")
    O = model.set_point(94.0, -139.0, label="O")
    E = model.set_point(140.0, -139.0, label="E")
    D_t = model.set_point(19.0, -18.5, label="D_t")
    C_t = model.set_point(140.0, -18.5, label="C_t")

    # Right composite figure: rectangles GH, MK (HN), NL on FG
    F = model.set_point(194.5, -18.0, classes=["given"], label="F")
    G = model.set_point(256.0, -18.0, classes=["given"], label="G")
    H = model.set_point(194.5, -112.5, label="H")
    M = model.set_point(256.0, -112.5, label="M")
    K = model.set_point(194.5, -165.5, label="K")
    N = model.set_point(256.0, -165.5, label="N")
    L = model.set_point(194.5, -198.5, label="L")
    L_r = model.set_point(256.0, -198.5, label="L_r")

    # Base lines
    model.construct_line(D_t, C_t)
    model.construct_line(D, C)
    model.construct_line(O, E)
    model.construct_line(D_t, D)
    model.construct_line(A, O)
    model.construct_line(C_t, E)

    model.construct_line(F, L)
    model.construct_line(G, L_r)
    model.construct_line(F, G)
    model.construct_line(H, M)
    model.construct_line(K, N)
    model.construct_line(L, L_r)

    # Segments on left figure
    model.set_segment(A, B)
    model.set_segment(B, O)
    model.set_segment(A, O)
    model.set_segment(D, B)
    model.set_segment(B, C)
    model.set_segment(D, C)
    model.set_segment(O, E)
    model.set_segment(C, E)
    model.set_segment(D_t, D)
    model.set_segment(D_t, C_t)
    model.set_segment(C_t, E)

    # Segments on right figure
    model.set_segment(F, G)
    model.set_segment(H, M)
    model.set_segment(K, N)
    model.set_segment(L, L_r)
    model.set_segment(F, H)
    model.set_segment(H, K)
    model.set_segment(K, L)
    model.set_segment(F, K)
    model.set_segment(H, L)
    model.set_segment(F, L)
    model.set_segment(G, L_r)

    # Collinear sections
    model.set_section([A, B, O])
    model.set_section([D, B, C])
    model.set_section([F, H, K])
    model.set_section([H, K, L])
    model.set_section([F, H, L])

    # Polygons
    model.set_polygon([A, B, D, D_t])
    model.set_polygon([A, B, C, C_t])
    model.set_polygon([B, C, E, O])
    model.set_polygon([F, G, M, H])
    model.set_polygon([H, M, N, K])
    model.set_polygon([K, N, L_r, L])

    return model


if __name__ == "__main__":
    construct_0060_g1()
