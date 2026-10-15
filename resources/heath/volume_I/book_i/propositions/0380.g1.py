"""Programmatic construction for Proposition 47 Commentary (0380.g1).

Pappus' extension of Book I, Proposition 47 to arbitrary triangles and
parallelograms described on any two sides.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0380_g1() -> Model:
    """Construct Pappus' extension figure (0380.g1) using geometor.model."""
    model = Model("0380.g1")

    A = model.set_point(32.5, -209, classes=["given"], label="A")
    B = model.set_point(135, -100, classes=["given"], label="B")
    C = model.set_point(192, -209, classes=["given"], label="C")
    D = model.set_point(21.5, -165, label="D")
    E = model.set_point(126.5, -60, label="E")
    F = model.set_point(245, -191, label="F")
    G = model.set_point(188, -84, label="G")
    H = model.set_point(159, -25, label="H")
    K = model.set_point(102.5, -209, label="K")
    L = model.set_point(55, -134.5, label="L")
    M = model.set_point(214.5, -134.5, label="M")
    N = model.set_point(127, -134.5, label="N")

    # Polygons: triangle ABC and parallelograms ABED, BCFG, ALHB, MCBH, ALMC, LAKN, NKCM
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, E, D])
    model.set_polygon([B, C, F, G])
    model.set_polygon([A, L, H, B])
    model.set_polygon([M, C, B, H])
    model.set_polygon([A, L, M, C])
    model.set_polygon([L, A, K, N])
    model.set_polygon([N, K, C, M])

    # Segments
    for p1, p2 in [
        (A, C), (A, K), (K, C),
        (A, B), (B, C),
        (D, A), (E, B), (D, H), (D, L), (L, E), (E, H), (D, E),
        (B, G), (C, F), (H, F), (H, G), (G, M), (M, F), (F, G),
        (H, K), (H, B), (B, N), (N, K), (B, K),
        (A, L), (C, M), (L, M), (L, N), (N, M),
    ]:
        model.set_segment(p1, p2)

    # Angles
    model.set_wedge(A, B, B, C)  # < B A C )
    model.set_wedge(A, L, L, B)  # < L A B )
    model.set_wedge(A, L, L, C)  # < L A C )
    model.set_wedge(H, D, D, B)  # < D H B ) / < B H D )

    return model


if __name__ == "__main__":
    construct_0380_g1()
