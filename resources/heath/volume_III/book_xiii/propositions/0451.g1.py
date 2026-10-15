"""Programmatic construction for Book XIII, Proposition 3 Commentary (0451.g1).

Alternative figure based on Book II, Proposition 11 showing BD^2 = 5 CD^2.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0451_g1() -> Model:
    """Construct the alternative figure 0451.g1 using geometor.model."""
    model = Model("0451.g1")

    B = model.set_point(22.0, -25.0, label="B")
    T = model.set_point(110.0, -25.0, label="T")
    C = model.set_point(22.0, -120.0, classes=["given"], label="C")
    E = model.set_point(110.0, -120.0, classes=["given"], label="E")
    F = model.set_point(158.0, -120.0, classes=["given"], label="F")
    D = model.set_point(22.0, -184.0, label="D")
    A = model.set_point(22.0, -248.0, classes=["given"], label="A")
    H = model.set_point(110.0, -248.0, label="H")
    G = model.set_point(158.0, -248.0, label="G")

    model.set_segment(B, A)
    model.set_segment(B, D)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_segment(C, D)
    model.set_segment(D, A)
    model.set_segment(C, F)
    model.set_segment(C, E)
    model.set_segment(E, F)
    model.set_segment(B, T)
    model.set_segment(T, H)
    model.set_segment(T, E)
    model.set_segment(E, H)
    model.set_segment(F, G)
    model.set_segment(A, G)
    model.set_segment(A, H)
    model.set_segment(H, G)
    model.set_segment(D, F)

    model.set_polygon([B, T, E, C])
    model.set_polygon([C, F, G, A])
    model.set_polygon([C, E, H, A])
    model.set_polygon([E, F, G, H])
    model.set_polygon([C, D, F])

    return model


if __name__ == "__main__":
    construct_0451_g1()
