"""Programmatic construction for Book XII, Proposition 11 (0410.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0410_g1() -> Model:
    """Construct the figure 0410.g1 using geometor.model."""
    model = Model("0410.g1")

    # First circle ABCD and axis KL
    K = model.set_point(122.0, -120.0, label="K")
    L = model.set_point(214.0, -58.0, label="L")
    A = model.set_point(30.0, -120.0, classes=["given"], label="A")
    B = model.set_point(122.0, -212.0, classes=["given"], label="B")
    C = model.set_point(214.0, -120.0, classes=["given"], label="C")
    D = model.set_point(122.0, -28.0, classes=["given"], label="D")
    T = model.set_point(56.95, -54.95, label="T")
    U = model.set_point(56.95, -185.05, label="U")
    V = model.set_point(187.05, -185.05, label="V")
    W = model.set_point(187.05, -54.95, label="W")

    model.construct_circle(K, A)
    model.set_segment(A, C)
    model.set_segment(K, L)
    for p1, p2 in [(A, B), (B, C), (C, D), (D, A)]:
        model.set_segment(p1, p2)
    for p1, p2 in [(D, T), (T, A), (A, U), (U, B), (B, V), (V, C), (C, W), (W, D)]:
        model.set_segment(p1, p2)

    model.set_polygon([A, B, C, D])
    model.set_polygon([D, T, A, U, B, V, C, W])

    # Second circle EFGH and axis MN
    M = model.set_point(336.0, -128.0, label="M")
    N = model.set_point(426.0, -68.0, label="N")
    E = model.set_point(258.0, -128.0, classes=["given"], label="E")
    F = model.set_point(336.0, -206.0, classes=["given"], label="F")
    G = model.set_point(414.0, -128.0, classes=["given"], label="G")
    H = model.set_point(336.0, -50.0, classes=["given"], label="H")
    P = model.set_point(280.85, -72.85, label="P")
    Q = model.set_point(280.85, -183.15, label="Q")
    R = model.set_point(391.15, -183.15, label="R")
    S = model.set_point(391.15, -72.85, label="S")

    model.construct_circle(M, E)
    model.set_segment(E, G)
    model.set_segment(M, N)
    for p1, p2 in [(E, F), (F, G), (G, H), (H, E)]:
        model.set_segment(p1, p2)
    for p1, p2 in [(H, P), (P, E), (E, Q), (Q, F), (F, R), (R, G), (G, S), (S, H)]:
        model.set_segment(p1, p2)

    model.set_polygon([E, F, G, H])
    model.set_polygon([H, P, E, Q, F, R, G, S])
    model.set_polygon([H, P, E])
    model.set_polygon([E, Q, F])
    model.set_polygon([F, R, G])
    model.set_polygon([G, S, H])

    return model


if __name__ == "__main__":
    construct_0410_g1()
