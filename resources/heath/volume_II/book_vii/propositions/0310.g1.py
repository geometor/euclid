"""Programmatic construction for Book VII, Proposition 5 (0310.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0310_g1() -> Model:
    """Construct the figure 0310.g1 using geometor.model."""
    model = Model("0310.g1")

    # Single-letter vertical number segment A
    A_t = model.set_point(25.0, -54.0, classes=["given"], label="A")
    A_b = model.set_point(25.0, -102.0, label="A_b")

    # Vertical number segment BC (divided at G)
    B = model.set_point(49.0, -12.0, classes=["given"], label="B")
    G = model.set_point(49.0, -60.0, label="G")
    C = model.set_point(49.0, -108.0, classes=["given"], label="C")

    # Single-letter vertical number segment D
    D_t = model.set_point(88.0, -62.0, classes=["given"], label="D")
    D_b = model.set_point(88.0, -97.0, label="D_b")

    # Vertical number segment EF (divided at H)
    E = model.set_point(116.0, -36.0, classes=["given"], label="E")
    H = model.set_point(116.0, -72.0, label="H")
    F = model.set_point(116.0, -108.0, classes=["given"], label="F")

    # Base lines
    model.construct_line(B, C)
    model.construct_line(E, F)

    # Whole and subdivided segments
    model.set_segment(A_t, A_b)
    model.set_segment(B, C)
    model.set_segment(B, G)
    model.set_segment(G, C)
    model.set_segment(D_t, D_b)
    model.set_segment(E, F)
    model.set_segment(E, H)
    model.set_segment(H, F)

    # Collinear sections
    model.set_section([B, G, C])
    model.set_section([E, H, F])

    return model


if __name__ == "__main__":
    construct_0310_g1()
