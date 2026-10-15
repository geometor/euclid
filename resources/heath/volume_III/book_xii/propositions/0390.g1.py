"""Programmatic construction for Book XII, Proposition 5 (0390.g1).

Two pyramids ABCG and DEFH of the same height with triangular bases ABC and
DEF and vertices G and H, each divided into two pyramids and two prisms, and
solid magnitude W.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0390_g1() -> Model:
    """Construct the figure 0390.g1 using geometor.model."""
    model = Model("0390.g1")

    # Left pyramid ABCG
    G = model.set_point(95.0, -24.0, classes=["given"], label="G")
    A = model.set_point(23.0, -192.0, classes=["given"], label="A")
    B = model.set_point(88.0, -232.0, classes=["given"], label="B")
    C = model.set_point(178.0, -192.0, classes=["given"], label="C")
    K = model.set_point(55.5, -212.0, label="K")
    O = model.set_point(133.0, -212.0, label="O")
    L = model.set_point(100.5, -192.0, label="L")
    P = model.set_point(66.2, -91.2, label="P")
    M = model.set_point(92.2, -107.2, label="M")
    N = model.set_point(128.2, -91.2, label="N")

    # Solid W parallelepiped vertices and label center
    W1 = model.set_point(164.0, -22.0, label="W1")
    W2 = model.set_point(292.0, -22.0, label="W2")
    W3 = model.set_point(292.0, -98.0, label="W3")
    W4 = model.set_point(164.0, -98.0, label="W4")
    W5 = model.set_point(185.0, -54.0, label="W5")
    W6 = model.set_point(313.0, -54.0, label="W6")
    W7 = model.set_point(313.0, -130.0, label="W7")
    W8 = model.set_point(185.0, -130.0, label="W8")
    W = model.set_point(238.5, -76.0, classes=["given"], label="W")

    # Right pyramid DEFH
    H = model.set_point(437.0, -24.0, classes=["given"], label="H")
    D = model.set_point(286.0, -192.0, classes=["given"], label="D")
    E = model.set_point(364.0, -232.0, classes=["given"], label="E")
    F = model.set_point(494.0, -192.0, classes=["given"], label="F")
    Q = model.set_point(325.0, -212.0, label="Q")
    V = model.set_point(429.0, -212.0, label="V")
    R = model.set_point(390.0, -192.0, label="R")
    S = model.set_point(376.6, -91.2, label="S")
    T = model.set_point(407.8, -107.2, label="T")
    U = model.set_point(459.8, -91.2, label="U")

    # Left segments
    for p1, p2 in [
        (G, A), (G, P), (P, A),
        (G, B), (G, M), (M, B),
        (G, C), (G, N), (N, C),
        (A, B), (A, K), (K, B),
        (B, C), (B, O), (O, C),
        (C, A), (C, L), (L, A),
        (P, M), (M, N), (N, P),
        (K, L), (L, O),
        (P, K), (P, L), (M, O),
    ]:
        model.set_segment(p1, p2)

    # Solid W segments
    for p1, p2 in [
        (W1, W2), (W2, W3), (W3, W4), (W4, W1),
        (W5, W6), (W6, W7), (W7, W8), (W8, W5),
        (W1, W5), (W2, W6), (W3, W7), (W4, W8),
    ]:
        model.set_segment(p1, p2)

    # Right segments
    for p1, p2 in [
        (H, D), (H, S), (S, D),
        (H, E), (H, T), (T, E),
        (H, F), (H, U), (U, F),
        (D, E), (D, Q), (Q, E),
        (E, F), (E, V), (V, F),
        (F, D), (F, R), (R, D),
        (S, T), (T, U), (U, S),
        (Q, R), (R, V),
        (S, Q), (S, R), (T, V),
    ]:
        model.set_segment(p1, p2)

    # Polygons
    for poly in [
        [A, B, C], [L, O, C], [P, M, N], [K, B, O, L],
        [D, E, F], [R, V, F], [S, T, U], [Q, E, V, R],
        [W1, W2, W6, W7, W8, W4],
    ]:
        model.set_polygon(poly)

    return model


if __name__ == "__main__":
    construct_0390_g1()
