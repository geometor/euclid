"""Programmatic construction for Book XIII, Proposition 2 Commentary (0449.g1).

Alternative figure based on Book II, Proposition 11 showing rect. CD, DB = CB^2.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0449_g1() -> Model:
    """Construct the alternative figure 0449.g1 using geometor.model."""
    model = Model("0449.g1")

    C = model.set_point(23.0, -107.0, classes=["given"], label="C")
    B = model.set_point(114.0, -107.0, classes=["given"], label="B")
    D = model.set_point(170.0, -107.0, classes=["given"], label="D")
    R = model.set_point(23.0, -16.0, label="R")
    T = model.set_point(114.0, -16.0, label="T")
    A = model.set_point(23.0, -180.5, label="A")
    K = model.set_point(23.0, -254.0, label="K")
    E = model.set_point(114.0, -254.0, label="E")
    G = model.set_point(170.0, -254.0, label="G")

    model.set_segment(C, D)
    model.set_segment(C, B)
    model.set_segment(B, D)
    model.set_segment(R, K)
    model.set_segment(R, A)
    model.set_segment(R, C)
    model.set_segment(C, A)
    model.set_segment(A, K)
    model.set_segment(C, K)
    model.set_segment(R, T)
    model.set_segment(T, E)
    model.set_segment(T, B)
    model.set_segment(B, E)
    model.set_segment(D, G)
    model.set_segment(K, G)
    model.set_segment(K, E)
    model.set_segment(E, G)
    model.set_segment(A, D)

    model.set_polygon([R, T, B, C])
    model.set_polygon([R, T, E, K])
    model.set_polygon([C, D, G, K])
    model.set_polygon([C, B, E, K])
    model.set_polygon([B, D, G, E])
    model.set_polygon([A, C, D])

    return model


if __name__ == "__main__":
    construct_0449_g1()
