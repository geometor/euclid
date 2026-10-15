"""Programmatic construction for Book VII, Proposition 15 (0321.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0321_g1() -> Model:
    """Construct the figure 0321.g1 using geometor.model."""
    model = Model("0321.g1")

    # Single-letter horizontal unit segment A
    A_l = model.set_point(24.0, -21.0, classes=["given"], label="A")
    A_r = model.set_point(62.0, -21.0, label="A_r")

    # Horizontal number segment BC (divided at G and H)
    B = model.set_point(109.0, -23.0, classes=["given"], label="B")
    G = model.set_point(150.0, -23.0, label="G")
    H = model.set_point(191.0, -23.0, label="H")
    C = model.set_point(232.0, -23.0, classes=["given"], label="C")

    # Single-letter horizontal number segment D
    D_l = model.set_point(99.0, -49.0, classes=["given"], label="D")
    D_r = model.set_point(177.0, -49.0, label="D_r")

    # Horizontal number segment EF (divided at K and L)
    E = model.set_point(14.0, -75.0, classes=["given"], label="E")
    K = model.set_point(96.0, -75.0, label="K")
    L = model.set_point(178.0, -75.0, label="L")
    F = model.set_point(260.0, -75.0, classes=["given"], label="F")

    # Base lines
    model.construct_line(B, C)
    model.construct_line(E, F)

    # Whole and subdivided segments
    model.set_segment(A_l, A_r)
    model.set_segment(B, C)
    model.set_segment(B, G)
    model.set_segment(G, H)
    model.set_segment(H, C)
    model.set_segment(B, H)
    model.set_segment(G, C)

    model.set_segment(D_l, D_r)
    model.set_segment(E, F)
    model.set_segment(E, K)
    model.set_segment(K, L)
    model.set_segment(L, F)
    model.set_segment(E, L)
    model.set_segment(K, F)

    # Collinear sections
    model.set_section([B, G, H])
    model.set_section([G, H, C])
    model.set_section([E, K, L])
    model.set_section([K, L, F])

    return model


if __name__ == "__main__":
    construct_0321_g1()
