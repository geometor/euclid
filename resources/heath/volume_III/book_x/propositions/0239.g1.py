"""Programmatic construction for Book X, Proposition 108 (0239.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0239_g1() -> Model:
    """Construct the figure 0239.g1 using geometor.model."""
    model = Model("0239.g1")

    # Top rectangle AEB-CD
    A = model.set_point(85.5, -19.0, classes=["given"], label="A")
    E = model.set_point(170.0, -19.0, label="E")
    B = model.set_point(195.5, -19.0, classes=["given"], label="B")
    C = model.set_point(85.5, -113.5, classes=["given"], label="C")
    D = model.set_point(170.0, -113.5, label="D")
    B_b = model.set_point(195.5, -113.5, label="B_b")

    # Bottom rectangle H_t-L-G / H-K-F
    H_t = model.set_point(18.0, -143.5, label="H_t")
    L = model.set_point(187.5, -143.5, label="L")
    G = model.set_point(275.0, -143.5, classes=["given"], label="G")
    H = model.set_point(18.0, -190.5, label="H")
    K = model.set_point(187.5, -190.5, label="K")
    F = model.set_point(275.0, -190.5, classes=["given"], label="F")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, B_b)
    model.construct_line(A, C)
    model.construct_line(E, D)
    model.construct_line(B, B_b)

    model.construct_line(H_t, G)
    model.construct_line(H, F)
    model.construct_line(H_t, H)
    model.construct_line(L, K)
    model.construct_line(G, F)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(A, C)
    model.set_segment(E, D)
    model.set_segment(B, B_b)
    model.set_segment(C, D)
    model.set_segment(D, B_b)
    model.set_segment(C, B_b)

    model.set_segment(F, G)
    model.set_segment(L, K)
    model.set_segment(H_t, H)
    model.set_segment(H, F)
    model.set_segment(H, K)
    model.set_segment(K, F)
    model.set_segment(H_t, G)
    model.set_segment(H_t, L)
    model.set_segment(L, G)

    # Sections
    model.set_section([A, E, B])
    model.set_section([H, K, F])

    # Polygons (rectangles)
    model.set_polygon([A, B, B_b, C])  # BC
    model.set_polygon([E, B, B_b, D])  # BD
    model.set_polygon([A, E, D, C])    # EC
    model.set_polygon([H_t, G, F, H])  # GH
    model.set_polygon([L, G, F, K])    # GK
    model.set_polygon([H_t, L, K, H])  # LH

    return model


if __name__ == "__main__":
    construct_0239_g1()
