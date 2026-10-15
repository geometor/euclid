"""Programmatic construction for Book XIII, Proposition 1 Commentary (0445.g1).

Alternative figure based on Book II, Proposition 11 showing SR^2 = 5 AR^2.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0445_g1() -> Model:
    """Construct the alternative figure 0445.g1 using geometor.model."""
    model = Model("0445.g1")

    A = model.set_point(23.0, -108.0, classes=["given"], label="A")
    C = model.set_point(113.0, -108.0, classes=["given"], label="C")
    B = model.set_point(168.0, -108.0, classes=["given"], label="B")
    S = model.set_point(23.0, -18.0, label="S")
    T = model.set_point(113.0, -18.0, label="T")
    R = model.set_point(23.0, -181.0, label="R")
    K = model.set_point(23.0, -254.0, label="K")
    G = model.set_point(113.0, -254.0, label="G")
    E = model.set_point(168.0, -254.0, label="E")

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(S, K)
    model.set_segment(S, R)
    model.set_segment(S, A)
    model.set_segment(A, R)
    model.set_segment(R, K)
    model.set_segment(A, K)
    model.set_segment(S, T)
    model.set_segment(T, G)
    model.set_segment(T, C)
    model.set_segment(C, G)
    model.set_segment(B, E)
    model.set_segment(K, E)
    model.set_segment(K, G)
    model.set_segment(G, E)
    model.set_segment(R, B)

    model.set_polygon([S, T, C, A])
    model.set_polygon([A, B, E, K])
    model.set_polygon([A, C, G, K])
    model.set_polygon([C, B, E, G])
    model.set_polygon([A, B, R])

    return model


if __name__ == "__main__":
    construct_0445_g1()
