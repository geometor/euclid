"""Programmatic construction for Book IX, Proposition 35 (0426.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0426_g1() -> Model:
    """Construct the figure 0426.g1 using geometor.model."""
    model = Model("0426.g1")

    # Single-letter number segment A
    A_l = model.set_point(235.0, -13.0, classes=["given"], label="A")
    A_r = model.set_point(265.0, -13.0, label="A_r")

    # Subdivided number segment BC (divided at G)
    B = model.set_point(205.0, -28.5, classes=["given"], label="B")
    G = model.set_point(235.0, -28.5, label="G")
    C = model.set_point(265.0, -28.5, classes=["given"], label="C")

    # Single-letter number segment D
    D_l = model.set_point(176.0, -53.0, classes=["given"], label="D")
    D_r = model.set_point(267.0, -53.0, label="D_r")

    # Subdivided number segment EF (divided at L, K, H)
    E = model.set_point(15.0, -78.0, classes=["given"], label="E")
    L = model.set_point(176.0, -78.0, label="L")
    K = model.set_point(205.0, -78.0, label="K")
    H = model.set_point(235.0, -78.0, label="H")
    F = model.set_point(266.0, -78.0, classes=["given"], label="F")

    # Base lines for subdivided segments
    model.construct_line(B, C)
    model.construct_line(E, F)

    # Standalone segments A and D
    model.set_segment(A_l, A_r)
    model.set_segment(D_l, D_r)

    # Whole and subdivided segments on BC
    model.set_segment(B, C)
    model.set_segment(B, G)
    model.set_segment(G, C)

    # Whole and subdivided segments on EF
    model.set_segment(E, F)
    model.set_segment(E, L)
    model.set_segment(E, K)
    model.set_segment(E, H)
    model.set_segment(L, K)
    model.set_segment(L, H)
    model.set_segment(L, F)
    model.set_segment(K, H)
    model.set_segment(K, F)
    model.set_segment(H, F)

    # Collinear sections
    model.set_section([B, G, C])
    model.set_section([E, L, F])
    model.set_section([E, H, F])
    model.set_section([L, K, F])
    model.set_section([K, H, F])

    return model


if __name__ == "__main__":
    construct_0426_g1()
