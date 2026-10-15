"""Programmatic construction for Book XII, Proposition 17 (0429.g1).

Two concentric spheres about center A, with great circle BCDE in the outer
sphere, circle FGH in the inner sphere, perpendicular semicircles BOD and KON,
and polyhedral facets KBPS, SPQT, TQRU, URO.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0429_g1() -> Model:
    """Construct the figure 0429.g1 using geometor.model."""
    model = Model("0429.g1")

    # Center A and main poles/diameters
    A = model.set_point(250.0, -252.5, classes=["given"], label="A")
    O = model.set_point(250.0, -23.5, classes=["given"], label="O")
    B = model.set_point(479.0, -252.5, classes=["given"], label="B")
    D = model.set_point(21.0, -252.5, classes=["given"], label="D")

    # Inner sphere circle FGH points
    G = model.set_point(386.0, -252.5, classes=["given"], label="G")
    H = model.set_point(281.9, -205.0, classes=["given"], label="H")
    F = model.set_point(218.1, -300.0, classes=["given"], label="F")

    # Equatorial ellipse BCDE points
    C = model.set_point(312.0, -160.1, classes=["given"], label="C")
    E = model.set_point(188.0, -344.9, classes=["given"], label="E")
    M = model.set_point(265.0, -348.3, classes=["given"], label="M")
    L = model.set_point(340.0, -340.8, classes=["given"], label="L")
    K = model.set_point(412.4, -320.2, classes=["given"], label="K")
    N = model.set_point(87.6, -184.8, classes=["given"], label="N")

    # Quadrant BO points
    R = model.set_point(337.6, -40.9, classes=["given"], label="R")
    Q = model.set_point(411.9, -90.6, classes=["given"], label="Q")
    P = model.set_point(461.6, -164.9, classes=["given"], label="P")

    # Quadrant KO points
    U = model.set_point(331.0, -51.2, classes=["given"], label="U")
    T = model.set_point(388.0, -118.9, classes=["given"], label="T")
    S = model.set_point(416.8, -207.2, classes=["given"], label="S")

    # Foot of perpendiculars and auxiliary points V, W, Z, X
    V = model.set_point(461.6, -252.5, classes=["given"], label="V")
    W = model.set_point(401.6, -315.7, classes=["given"], label="W")
    Z = model.set_point(456.0, -252.5, classes=["given"], label="Z")
    X = model.set_point(445.0, -232.0, classes=["given"], label="X")

    # Concentric spheres / circles
    model.construct_circle(A, B)
    model.construct_circle(A, G)

    # Segments
    for p1, p2 in [
        (D, A), (A, G), (G, Z), (Z, V), (V, B),
        (D, B), (A, B), (A, V), (B, V), (D, Z), (B, Z), (A, Z),
        (C, H), (H, A), (A, F), (F, E), (C, E),
        (N, A), (A, W), (W, K), (A, K), (K, N),
        (A, O),
        (B, K), (K, L), (L, M), (M, E),
        (B, P), (P, Q), (Q, R), (R, O),
        (K, S), (S, T), (T, U), (U, O),
        (S, P), (T, Q), (U, R),
        (P, V), (S, W), (W, V),
        (A, X), (B, X), (K, X),
        (K, Z), (K, D),
    ]:
        model.set_segment(p1, p2)

    # Polyhedral facets
    model.set_polygon([K, B, P, S])
    model.set_polygon([S, P, Q, T])
    model.set_polygon([T, Q, R, U])
    model.set_polygon([U, R, O])

    return model


if __name__ == "__main__":
    construct_0429_g1()
