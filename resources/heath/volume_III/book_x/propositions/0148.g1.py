"""Programmatic construction for Book X, Proposition 65 (0148.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0148_g1() -> Model:
    """Construct the figure 0148.g1 using geometor.model."""
    model = Model("0148.g1")

    # Side of the sum of two medial areas AB divided at C
    A = model.set_point(48.0, -132.5, classes=["given"], label="A")
    C = model.set_point(134.0, -132.5, classes=["given"], label="C")
    B = model.set_point(180.0, -132.5, classes=["given"], label="B")

    # Parallelogram DF applied to rational straight line DE, divided by KH, ML, NO
    D = model.set_point(19.5, -19.5, classes=["given"], label="D")
    K = model.set_point(97.5, -19.5, label="K")
    M = model.set_point(119.5, -19.5, label="M")
    N = model.set_point(164.5, -19.5, label="N")
    G = model.set_point(207.5, -19.5, label="G")

    E = model.set_point(19.5, -112.5, classes=["given"], label="E")
    H = model.set_point(97.5, -112.5, label="H")
    L = model.set_point(119.5, -112.5, label="L")
    O = model.set_point(164.5, -112.5, label="O")
    F = model.set_point(207.5, -112.5, label="F")

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
    construct_0148_g1()
