"""Programmatic construction for Book X, Proposition 50 (0110.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0110_g1() -> Model:
    """Construct the figure 0110.g1 using geometor.model."""
    model = Model("0110.g1")

    # Single-letter magnitude segments E, K, D
    E_l = model.set_point(17.0, -31.5, classes=["given"], label="E")
    E_r = model.set_point(89.0, -31.5, label="E_r")

    K_l = model.set_point(123.0, -20.5, classes=["given"], label="K")
    K_r = model.set_point(182.0, -20.5, label="K_r")

    D_l = model.set_point(252.0, -41.0, classes=["given"], label="D")
    D_r = model.set_point(321.0, -41.0, label="D_r")

    # Number line AB divided at C
    A = model.set_point(221.0, -20.5, classes=["given"], label="A")
    C = model.set_point(297.0, -20.5, classes=["given"], label="C")
    B = model.set_point(343.0, -20.5, classes=["given"], label="B")

    # Line FH divided at G
    F = model.set_point(20.0, -58.5, classes=["given"], label="F")
    G = model.set_point(123.0, -58.5, classes=["given"], label="G")
    H = model.set_point(190.0, -58.5, classes=["given"], label="H")

    # Base lines
    model.construct_line(E_l, E_r)
    model.construct_line(K_l, K_r)
    model.construct_line(A, B)
    model.construct_line(D_l, D_r)
    model.construct_line(F, H)

    # Segments
    model.set_segment(E_l, E_r)
    model.set_segment(K_l, K_r)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(D_l, D_r)
    model.set_segment(F, H)
    model.set_segment(F, G)
    model.set_segment(G, H)

    # Collinear sections
    model.set_section([A, C, B])
    model.set_section([F, G, H])

    return model


if __name__ == "__main__":
    construct_0110_g1()
