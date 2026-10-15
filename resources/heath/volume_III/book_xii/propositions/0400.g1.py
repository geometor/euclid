"""Programmatic construction for Book XII, Proposition 8 (0400.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0400_g1() -> Model:
    """Construct the figure 0400.g1 using geometor.model."""
    model = Model("0400.g1")

    # First parallelepiped BGML and pyramid ABCG
    A = model.set_point(25.0, -67.0, classes=["given"], label="A")
    B = model.set_point(16.0, -144.0, classes=["given"], label="B")
    C = model.set_point(113.0, -144.0, classes=["given"], label="C")
    M = model.set_point(122.0, -67.0, label="M")
    K = model.set_point(44.0, -37.0, label="K")
    G = model.set_point(35.0, -114.0, classes=["given"], label="G")
    N = model.set_point(132.0, -114.0, label="N")
    L = model.set_point(141.0, -37.0, label="L")

    # Second parallelepiped EHQP and pyramid DEFH
    D = model.set_point(288.0, -67.0, classes=["given"], label="D")
    E = model.set_point(275.0, -175.0, classes=["given"], label="E")
    F = model.set_point(412.0, -175.0, classes=["given"], label="F")
    Q = model.set_point(425.0, -67.0, label="Q")
    O = model.set_point(318.0, -22.0, label="O")
    H = model.set_point(305.0, -130.0, classes=["given"], label="H")
    R = model.set_point(442.0, -130.0, label="R")
    P = model.set_point(455.0, -22.0, label="P")

    # Edges of first parallelepiped and pyramid
    for p1, p2 in [
        (A, B), (B, C), (C, M), (M, A),
        (K, G), (G, N), (N, L), (L, K),
        (A, K), (B, G), (C, N), (M, L),
        (A, C), (A, G), (G, C),
    ]:
        model.set_segment(p1, p2)

    # Edges of second parallelepiped and pyramid
    for p1, p2 in [
        (D, E), (E, F), (F, Q), (Q, D),
        (O, H), (H, R), (R, P), (P, O),
        (D, O), (E, H), (F, R), (Q, P),
        (D, F), (D, H), (H, F),
    ]:
        model.set_segment(p1, p2)

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([B, C, M, A])
    model.set_polygon([B, C, N, G])
    model.set_polygon([B, G, K, A])
    model.set_polygon([E, F, Q, D])
    model.set_polygon([E, F, R, H])
    model.set_polygon([E, H, O, D])

    return model


if __name__ == "__main__":
    construct_0400_g1()
