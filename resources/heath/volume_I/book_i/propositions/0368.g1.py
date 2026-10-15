"""Programmatic construction for Proposition 47 Commentary (0368.g1).

Bretschneider and Hankel dissection proof comparing (a + b)^2 partitioned into
a^2 + b^2 + 2ab against (a + b)^2 partitioned into c^2 + 4(ab/2).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0368_g1() -> Model:
    """Construct the two dissection squares of 0368.g1 using geometor.model."""
    model = Model("0368.g1")

    # Left Figure: Square ABCD of side (a + b) partitioned at K
    A = model.set_point(26, -34, classes=["given"], label="A")
    E = model.set_point(132, -34, label="E")
    B = model.set_point(181, -34, classes=["given"], label="B")
    H = model.set_point(26, -83, label="H")
    K = model.set_point(132, -83, label="K")
    F = model.set_point(181, -83, label="F")
    D = model.set_point(26, -189, classes=["given"], label="D")
    G = model.set_point(132, -189, label="G")
    C = model.set_point(181, -189, classes=["given"], label="C")

    model.set_polygon([A, B, C, D])
    model.set_polygon([H, K, G, D])  # Square a^2
    model.set_polygon([E, B, F, K])  # Square b^2
    model.set_polygon([A, E, K, H])  # Top-left rectangle ab
    model.set_polygon([K, F, C, G])  # Bottom-right rectangle ab
    model.set_polygon([A, E, K])
    model.set_polygon([A, H, K])
    model.set_polygon([K, F, C])
    model.set_polygon([K, G, C])

    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, A),
        (A, E), (E, B), (B, F), (F, C), (C, G), (G, D), (D, H), (H, A),
        (E, G), (E, K), (K, G), (H, F), (H, K), (K, F),
        (A, K), (K, C),
    ]:
        model.set_segment(p1, p2)

    # Right Figure: Square PQRS of side (a + b) with inner tilted square TUVW of side c
    P = model.set_point(283, -34, classes=["given"], label="P")
    T = model.set_point(389, -34, label="T")
    Q = model.set_point(438, -34, classes=["given"], label="Q")
    U = model.set_point(438, -140, label="U")
    R = model.set_point(438, -189, classes=["given"], label="R")
    V = model.set_point(332, -189, label="V")
    S = model.set_point(283, -189, classes=["given"], label="S")
    W = model.set_point(283, -83, label="W")

    model.set_polygon([P, Q, R, S])
    model.set_polygon([T, U, V, W])  # Inner square c^2
    model.set_polygon([P, T, W])
    model.set_polygon([T, Q, U])
    model.set_polygon([U, R, V])
    model.set_polygon([W, V, S])

    for p1, p2 in [
        (P, Q), (Q, R), (R, S), (S, P),
        (P, T), (T, Q), (Q, U), (U, R), (R, V), (V, S), (S, W), (W, P),
        (T, U), (U, V), (V, W), (W, T),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0368_g1()
