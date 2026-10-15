"""Programmatic construction for Book XII, Proposition 6 (0396.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0396_g1() -> Model:
    """Construct the figure 0396.g1 using geometor.model."""
    model = Model("0396.g1")

    # First pyramid M-ABCDE
    M = model.set_point(96.0, -29.0, classes=["given"], label="M")
    A = model.set_point(128.0, -192.0, classes=["given"], label="A")
    B = model.set_point(147.0, -130.0, classes=["given"], label="B")
    C = model.set_point(60.0, -113.0, classes=["given"], label="C")
    D = model.set_point(21.0, -158.0, classes=["given"], label="D")
    E = model.set_point(62.0, -220.0, classes=["given"], label="E")

    # Second pyramid N-FGHKL
    N = model.set_point(227.0, -18.0, classes=["given"], label="N")
    F = model.set_point(259.0, -224.0, classes=["given"], label="F")
    G = model.set_point(375.0, -181.0, classes=["given"], label="G")
    H = model.set_point(290.0, -108.0, classes=["given"], label="H")
    K = model.set_point(225.0, -108.0, classes=["given"], label="K")
    L = model.set_point(195.0, -149.0, classes=["given"], label="L")

    # Segments of first pyramid
    for pt in [A, B, C, D, E]:
        model.set_segment(M, pt)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, A)
    model.set_segment(A, C)
    model.set_segment(A, D)

    # Segments of second pyramid
    for pt in [F, G, H, K, L]:
        model.set_segment(N, pt)
    model.set_segment(F, G)
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(K, L)
    model.set_segment(L, F)
    model.set_segment(F, H)
    model.set_segment(F, K)

    # Polygons
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B, C])
    model.set_polygon([A, C, D])
    model.set_polygon([A, D, E])

    model.set_polygon([F, G, H, K, L])
    model.set_polygon([F, G, H])
    model.set_polygon([F, H, K])
    model.set_polygon([F, K, L])

    return model


if __name__ == "__main__":
    construct_0396_g1()
