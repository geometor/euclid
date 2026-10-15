"""Programmatic construction for Book X, Proposition 44 (0099.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0099_g1() -> Model:
    """Construct the figure 0099.g1 using geometor.model."""
    model = Model("0099.g1")

    # Second bimedial straight line AB divided at C and D
    A = model.set_point(125.0, -21.5, classes=["given"], label="A")
    D = model.set_point(228.0, -21.5, label="D")
    C = model.set_point(257.0, -21.5, classes=["given"], label="C")
    B = model.set_point(313.0, -21.5, classes=["given"], label="B")

    # Rectangular parallelogram EK applied to rational straight line EF
    E = model.set_point(19.0, -54.0, classes=["given"], label="E")
    M = model.set_point(217.5, -54.0, label="M")
    H = model.set_point(258.5, -54.0, label="H")
    N = model.set_point(407.0, -54.0, label="N")
    F = model.set_point(19.0, -145.5, classes=["given"], label="F")
    L = model.set_point(217.5, -145.5, label="L")
    G = model.set_point(258.5, -145.5, label="G")
    K = model.set_point(407.0, -145.5, label="K")

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

    # Polygons: EK, EG, HK, EL, MK, MG
    model.set_polygon([E, F, K, N])
    model.set_polygon([E, F, G, H])
    model.set_polygon([H, G, K, N])
    model.set_polygon([E, F, L, M])
    model.set_polygon([M, L, K, N])
    model.set_polygon([M, L, G, H])

    return model


if __name__ == "__main__":
    construct_0099_g1()
