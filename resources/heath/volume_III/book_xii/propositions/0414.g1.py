"""Programmatic construction for Book XII, Proposition 12 (0414.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0414_g1() -> Model:
    """Construct the figure 0414.g1 using geometor.model."""
    model = Model("0414.g1")

    # First circle ABCD, center K, and apex L
    K = model.set_point(104.0, -146.0, label="K")
    L = model.set_point(38.0, -43.0, classes=["given"], label="L")
    A = model.set_point(104.0, -62.0, classes=["given"], label="A")
    B = model.set_point(20.0, -146.0, classes=["given"], label="B")
    C = model.set_point(104.0, -230.0, classes=["given"], label="C")
    D = model.set_point(188.0, -146.0, classes=["given"], label="D")
    T = model.set_point(44.6, -86.6, label="T")
    U = model.set_point(44.6, -205.4, label="U")
    V = model.set_point(163.4, -205.4, label="V")
    W = model.set_point(163.4, -86.6, label="W")

    model.construct_circle(K, A)
    model.set_segment(B, D)
    model.set_segment(B, K)
    model.set_segment(K, D)
    model.set_segment(K, L)
    model.set_segment(K, T)
    model.set_segment(L, B)
    model.set_segment(L, T)
    for p1, p2 in [(A, B), (B, C), (C, D), (D, A)]:
        model.set_segment(p1, p2)
    for p1, p2 in [(A, T), (T, B), (B, U), (U, C), (C, V), (V, D), (D, W), (W, A)]:
        model.set_segment(p1, p2)

    model.set_polygon([A, B, C, D])
    model.set_polygon([A, T, B, U, C, V, D, W])
    model.set_polygon([B, K, L])
    model.set_polygon([B, K, T])
    model.set_polygon([L, K, T])
    model.set_polygon([L, B, T])

    # Second circle EFGH, center M, and apex N
    M = model.set_point(331.0, -146.0, label="M")
    N = model.set_point(422.0, -25.0, classes=["given"], label="N")
    E = model.set_point(331.0, -50.0, classes=["given"], label="E")
    F = model.set_point(427.0, -146.0, classes=["given"], label="F")
    G = model.set_point(331.0, -242.0, classes=["given"], label="G")
    H = model.set_point(235.0, -146.0, classes=["given"], label="H")
    P = model.set_point(398.88, -78.12, label="P")
    Q = model.set_point(398.88, -213.88, label="Q")
    R = model.set_point(263.12, -213.88, label="R")
    S = model.set_point(263.12, -78.12, label="S")

    model.construct_circle(M, E)
    model.set_segment(F, H)
    model.set_segment(F, M)
    model.set_segment(M, H)
    model.set_segment(M, N)
    model.set_segment(M, P)
    model.set_segment(N, F)
    model.set_segment(N, P)
    for p1, p2 in [(E, F), (F, G), (G, H), (H, E)]:
        model.set_segment(p1, p2)
    for p1, p2 in [(E, P), (P, F), (F, Q), (Q, G), (G, R), (R, H), (H, S), (S, E)]:
        model.set_segment(p1, p2)

    model.set_polygon([E, F, G, H])
    model.set_polygon([E, P, F, Q, G, R, H, S])
    model.set_polygon([E, P, F])
    model.set_polygon([F, Q, G])
    model.set_polygon([G, R, H])
    model.set_polygon([H, S, E])
    model.set_polygon([F, M, N])
    model.set_polygon([F, M, P])
    model.set_polygon([N, M, P])
    model.set_polygon([N, F, P])

    return model


if __name__ == "__main__":
    construct_0414_g1()
