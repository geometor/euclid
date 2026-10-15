"""Programmatic construction for Book IV, Proposition 3 (0089.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0089_g1() -> Model:
    """Construct the figure 0089.g1 using geometor.model."""
    model = Model("0089.g1")

    # Points (y-inverted for standard mathematical coordinates)
    K = model.set_point(153.00, -104.00, label="K")
    A = model.set_point(125.30, -68.54, label="A")
    B = model.set_point(192.73, -82.87, label="B")
    C = model.set_point(153.00, -149.00, label="C")
    L = model.set_point(22.31, -149.00, label="L")
    M = model.set_point(167.56, -35.52, label="M")
    N = model.set_point(227.89, -149.00, label="N")

    # Given triangle DEF and extended line HG
    D = model.set_point(320.00, -43.00, classes=["given"], label="D")
    E = model.set_point(247.94, -99.30, classes=["given"], label="E")
    F = model.set_point(218.00, -43.00, classes=["given"], label="F")
    G = model.set_point(265.78, -132.85, label="G")
    H = model.set_point(209.55, -27.11, label="H")

    # Circle ABC
    model.construct_circle(K, A)

    # Construction lines
    model.construct_line(L, M)
    model.construct_line(M, N)
    model.construct_line(N, L)
    model.construct_line(H, G)

    # Segments
    model.set_segment(L, M)
    model.set_segment(M, N)
    model.set_segment(N, L)
    model.set_segment(L, A)
    model.set_segment(A, M)
    model.set_segment(M, B)
    model.set_segment(B, N)
    model.set_segment(N, C)
    model.set_segment(C, L)
    model.set_segment(K, A)
    model.set_segment(K, B)
    model.set_segment(K, C)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, D)
    model.set_segment(E, G)
    model.set_segment(F, H)
    model.set_segment(H, G)

    # Collinear sections
    model.set_section([L, A, M])
    model.set_section([M, B, N])
    model.set_section([N, C, L])
    model.set_section([H, F, E])
    model.set_section([F, E, G])

    # Polygons
    model.set_polygon([L, M, N])
    model.set_polygon([D, E, F])
    model.set_polygon([A, M, B, K])

    # Angles (wedges)
    model.set_wedge(K, B, B, A)
    model.set_wedge(K, B, B, C)
    model.set_wedge(K, C, C, A)
    model.set_wedge(A, K, K, M)
    model.set_wedge(B, K, K, M)
    model.set_wedge(M, A, A, B)
    model.set_wedge(N, L, L, B)
    model.set_wedge(L, M, M, N)
    model.set_wedge(E, D, D, G)
    model.set_wedge(E, D, D, F)
    model.set_wedge(F, D, D, H)
    model.set_wedge(F, D, D, E)
    model.set_wedge(D, E, E, F)

    return model


if __name__ == "__main__":
    construct_0089_g1()
