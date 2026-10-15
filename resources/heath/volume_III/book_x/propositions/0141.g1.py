"""Programmatic construction for Book X, Proposition 62 (0141.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0141_g1() -> Model:
    """Construct the figure 0141.g1 using geometor.model."""
    model = Model("0141.g1")

    # Second bimedial straight line AB divided into its medials at C
    A = model.set_point(56.0, -136.5, classes=["given"], label="A")
    C = model.set_point(144.0, -136.5, classes=["given"], label="C")
    B = model.set_point(192.0, -136.5, classes=["given"], label="B")

    # Parallelogram DF applied to rational straight line DE, divided by KH, ML, NO
    D = model.set_point(23.5, -18.5, classes=["given"], label="D")
    K = model.set_point(102.0, -18.5, label="K")
    M = model.set_point(124.5, -18.5, label="M")
    N = model.set_point(169.5, -18.5, label="N")
    G = model.set_point(214.5, -18.5, label="G")

    E = model.set_point(23.5, -112.0, classes=["given"], label="E")
    H = model.set_point(102.0, -112.0, label="H")
    L = model.set_point(124.5, -112.0, label="L")
    O = model.set_point(169.5, -112.0, label="O")
    F = model.set_point(214.5, -112.0, label="F")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(D, G)
    model.construct_line(E, F)
    model.construct_line(D, E)
    model.construct_line(K, H)
    model.construct_line(M, L)
    model.construct_line(N, O)
    model.construct_line(G, F)

    # Segments on AB
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Segments on DEFG
    model.set_segment(D, G)
    model.set_segment(D, K)
    model.set_segment(D, M)
    model.set_segment(D, N)
    model.set_segment(K, M)
    model.set_segment(K, N)
    model.set_segment(K, G)
    model.set_segment(M, N)
    model.set_segment(M, G)
    model.set_segment(N, G)

    model.set_segment(E, F)
    model.set_segment(E, H)
    model.set_segment(E, L)
    model.set_segment(E, O)
    model.set_segment(H, L)
    model.set_segment(H, O)
    model.set_segment(H, F)
    model.set_segment(L, O)
    model.set_segment(L, F)
    model.set_segment(O, F)

    model.set_segment(D, E)
    model.set_segment(K, H)
    model.set_segment(M, L)
    model.set_segment(N, O)
    model.set_segment(G, F)

    # Sections
    model.set_section([A, C, B])
    model.set_section([D, K, M])
    model.set_section([D, M, G])
    model.set_section([M, N, G])

    # Polygons
    model.set_polygon([D, E, F, G])
    model.set_polygon([D, E, H, K])
    model.set_polygon([K, H, L, M])
    model.set_polygon([D, E, L, M])
    model.set_polygon([M, L, F, G])
    model.set_polygon([M, L, O, N])
    model.set_polygon([N, O, F, G])

    return model


if __name__ == "__main__":
    construct_0141_g1()
