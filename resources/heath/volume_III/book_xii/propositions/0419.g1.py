"""Programmatic construction for Book XII, Proposition 12 Commentary (0419.g1).

Two similar cones with base centers K, M, vertices L, N, and inscribed polygon
sides BT, FP forming partial pyramids L-BKT and N-FMP.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0419_g1() -> Model:
    """Construct the figure 0419.g1 using geometor.model."""
    model = Model("0419.g1")

    # Left cone base (center K = (105, -98), radius 68) and vertex L
    K = model.set_point(105.0, -98.0, classes=["given"], label="K")
    B = model.set_point(42.0, -72.5, classes=["given"], label="B")
    T = model.set_point(62.2, -45.2, classes=["given"], label="T")
    L = model.set_point(152.0, -26.0, classes=["given"], label="L")

    # Right cone base (center M = (320, -106), radius 50) and vertex N
    M = model.set_point(320.0, -106.0, classes=["given"], label="M")
    F = model.set_point(273.6, -87.3, classes=["given"], label="F")
    P = model.set_point(288.5, -67.2, classes=["given"], label="P")
    N = model.set_point(353.0, -52.0, classes=["given"], label="N")

    # Base circles
    model.construct_circle(K, B)
    model.construct_circle(M, F)

    # Left segments
    for p1, p2 in [
        (K, L), (B, T), (B, K), (T, K), (B, L), (T, L),
    ]:
        model.set_segment(p1, p2)

    # Right segments
    for p1, p2 in [
        (M, N), (F, P), (F, M), (P, M), (F, N), (P, N),
    ]:
        model.set_segment(p1, p2)

    # Triangles and partial pyramids
    model.set_polygon([B, K, L])
    model.set_polygon([F, M, N])
    model.set_polygon([T, K, L])
    model.set_polygon([P, M, N])
    model.set_polygon([B, K, T])
    model.set_polygon([F, M, P])
    model.set_polygon([B, L, T])
    model.set_polygon([F, N, P])
    model.set_polygon([B, K, T, L])
    model.set_polygon([F, M, P, N])

    # Angles BKT and FMP
    model.set_wedge(K, B, B, T)
    model.set_wedge(M, F, F, P)

    return model


if __name__ == "__main__":
    construct_0419_g1()
