"""Programmatic construction for Book X, Proposition 102 (0231.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0231_g1() -> Model:
    """Construct the figure 0231.g1 using geometor.model."""
    model = Model("0231.g1")

    # Top line AG divided at B
    A = model.set_point(121.0, -18.5, classes=["given"], label="A")
    B = model.set_point(208.0, -18.5, classes=["given"], label="B")
    G = model.set_point(259.0, -18.5, classes=["given"], label="G")

    # Top edge of applied rectangles: C - F - N - K - M
    C = model.set_point(16.5, -53.5, classes=["given"], label="C")
    F = model.set_point(131.0, -53.5, label="F")
    N = model.set_point(241.5, -53.5, label="N")
    K = model.set_point(310.5, -53.5, label="K")
    M = model.set_point(352.5, -53.5, label="M")

    # Bottom edge of applied rectangles: D - E - O - H - L
    D = model.set_point(16.5, -117.0, classes=["given"], label="D")
    E = model.set_point(131.0, -117.0, label="E")
    O = model.set_point(241.5, -117.0, label="O")
    H = model.set_point(310.5, -117.0, label="H")
    L = model.set_point(352.5, -117.0, label="L")

    # Base lines
    model.construct_line(A, G)
    model.construct_line(C, M)
    model.construct_line(D, L)
    model.construct_line(C, D)
    model.construct_line(F, E)
    model.construct_line(N, O)
    model.construct_line(K, H)
    model.construct_line(M, L)

    # Segments on AG
    model.set_segment(A, G)
    model.set_segment(A, B)
    model.set_segment(B, G)
    model.set_section([A, B, G])

    # Vertical segments
    model.set_segment(C, D)
    model.set_segment(F, E)
    model.set_segment(N, O)
    model.set_segment(K, H)
    model.set_segment(M, L)

    # Top horizontal segments
    model.set_segment(C, M)
    model.set_segment(C, K)
    model.set_segment(C, N)
    model.set_segment(C, F)
    model.set_segment(F, M)
    model.set_segment(F, K)
    model.set_segment(F, N)
    model.set_segment(N, M)
    model.set_segment(N, K)
    model.set_segment(K, M)

    # Bottom horizontal segments
    model.set_segment(D, L)
    model.set_segment(D, H)
    model.set_segment(D, O)
    model.set_segment(D, E)
    model.set_segment(E, L)
    model.set_segment(E, H)
    model.set_segment(E, O)
    model.set_segment(O, L)
    model.set_segment(O, H)
    model.set_segment(H, L)

    # Sections
    model.set_section([C, F, M])
    model.set_section([C, K, M])
    model.set_section([F, N, M])

    # Polygons (rectangles)
    model.set_polygon([C, F, E, D])  # CE
    model.set_polygon([C, K, H, D])  # CH
    model.set_polygon([K, M, L, H])  # KL
    model.set_polygon([C, M, L, D])  # CL
    model.set_polygon([F, M, L, E])  # FL
    model.set_polygon([F, N, O, E])  # FO
    model.set_polygon([N, M, L, O])  # NL
    model.set_polygon([N, K, H, O])  # NH

    return model


if __name__ == "__main__":
    construct_0231_g1()
