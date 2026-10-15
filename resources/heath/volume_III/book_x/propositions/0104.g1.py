"""Programmatic construction for Book X, Proposition 47 (0104.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0104_g1() -> Model:
    """Construct the figure 0104.g1 using geometor.model."""
    model = Model("0104.g1")

    # Side of the sum of two medial areas AB (vertical on left) divided at D and C
    A = model.set_point(26.0, -21.0, classes=["given"], label="A")
    D = model.set_point(26.0, -139.0, label="D")
    C = model.set_point(26.0, -173.0, classes=["given"], label="C")
    B = model.set_point(26.0, -224.0, classes=["given"], label="B")

    # Rectangular parallelogram EK applied to rational straight line EF
    E = model.set_point(69.0, -19.0, classes=["given"], label="E")
    M = model.set_point(187.0, -19.0, label="M")
    H = model.set_point(212.5, -19.0, label="H")
    N = model.set_point(306.0, -19.0, label="N")
    F = model.set_point(69.0, -195.0, classes=["given"], label="F")
    L = model.set_point(187.0, -195.0, label="L")
    G = model.set_point(212.5, -195.0, label="G")
    K = model.set_point(306.0, -195.0, label="K")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(E, N)
    model.construct_line(F, K)
    model.construct_line(E, F)
    model.construct_line(M, L)
    model.construct_line(H, G)
    model.construct_line(N, K)

    # Segments on AB
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(D, C)
    model.set_segment(D, B)
    model.set_segment(C, B)

    # Segments on rectangle EK
    model.set_segment(E, F)
    model.set_segment(M, L)
    model.set_segment(H, G)
    model.set_segment(N, K)
    model.set_segment(E, N)
    model.set_segment(E, M)
    model.set_segment(E, H)
    model.set_segment(M, H)
    model.set_segment(M, N)
    model.set_segment(H, N)
    model.set_segment(F, K)
    model.set_segment(F, L)
    model.set_segment(F, G)
    model.set_segment(L, G)
    model.set_segment(L, K)
    model.set_segment(G, K)

    # Sections
    model.set_section([A, C, B])
    model.set_section([A, D, B])
    model.set_section([E, H, N])
    model.set_section([E, M, N])
    model.set_section([F, G, K])
    model.set_section([F, L, K])

    # Polygons: EK, EG, HK/GN, EL, MK, MG
    model.set_polygon([E, F, K, N])
    model.set_polygon([E, F, G, H])
    model.set_polygon([H, G, K, N])
    model.set_polygon([E, F, L, M])
    model.set_polygon([M, L, K, N])
    model.set_polygon([M, L, G, H])

    return model


if __name__ == "__main__":
    construct_0104_g1()
