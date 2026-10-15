"""Programmatic construction for Book XII, Proposition 4 (0387.g1).

Two pyramids ABCG and DEFH of the same height with triangular bases ABC and
DEF and vertices G and H, each divided into two equal and similar pyramids and
two equal prisms.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0387_g1() -> Model:
    """Construct the figure 0387.g1 using geometor.model."""
    model = Model("0387.g1")

    # Left pyramid ABCG
    G = model.set_point(97.0, -36.0, classes=["given"], label="G")
    A = model.set_point(25.0, -174.0, classes=["given"], label="A")
    B = model.set_point(99.0, -212.0, classes=["given"], label="B")
    C = model.set_point(186.0, -184.0, classes=["given"], label="C")
    K = model.set_point(62.0, -193.0, label="K")
    O = model.set_point(142.5, -198.0, label="O")
    L = model.set_point(105.5, -179.0, label="L")
    P = model.set_point(61.0, -105.0, label="P")
    M = model.set_point(98.0, -124.0, label="M")
    N = model.set_point(141.5, -110.0, label="N")

    # Right pyramid DEFH
    H = model.set_point(331.0, -24.0, classes=["given"], label="H")
    D = model.set_point(281.0, -174.0, classes=["given"], label="D")
    E = model.set_point(392.0, -224.0, classes=["given"], label="E")
    F = model.set_point(449.0, -174.0, classes=["given"], label="F")
    Q = model.set_point(336.5, -199.0, label="Q")
    V = model.set_point(420.5, -199.0, label="V")
    R = model.set_point(365.0, -174.0, label="R")
    S = model.set_point(306.0, -99.0, label="S")
    T = model.set_point(361.5, -124.0, label="T")
    U = model.set_point(390.0, -99.0, label="U")

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
    ]:
        model.set_polygon(poly)

    return model


if __name__ == "__main__":
    construct_0387_g1()
