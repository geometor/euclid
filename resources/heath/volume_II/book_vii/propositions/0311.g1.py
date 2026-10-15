"""Programmatic construction for Book VII, Proposition 6 (0311.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0311_g1() -> Model:
    """Construct the figure 0311.g1 using geometor.model."""
    model = Model("0311.g1")

    # Vertical number segment AB (divided at G)
    A = model.set_point(12.0, -47.0, classes=["given"], label="A")
    G = model.set_point(12.0, -83.5, label="G")
    B = model.set_point(12.0, -120.0, classes=["given"], label="B")

    # Single-letter vertical number segment C
    C_t = model.set_point(42.0, -10.0, classes=["given"], label="C")
    C_b = model.set_point(42.0, -120.0, label="C_b")

    # Vertical number segment DE (divided at H)
    D = model.set_point(98.0, -64.0, classes=["given"], label="D")
    H = model.set_point(98.0, -91.5, label="H")
    E = model.set_point(98.0, -119.0, classes=["given"], label="E")

    # Single-letter vertical number segment F
    F_t = model.set_point(129.0, -32.0, classes=["given"], label="F")
    F_b = model.set_point(129.0, -120.0, label="F_b")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(D, E)

    # Whole and subdivided segments
    model.set_segment(A, B)
    model.set_segment(A, G)
    model.set_segment(G, B)
    model.set_segment(C_t, C_b)
    model.set_segment(D, E)
    model.set_segment(D, H)
    model.set_segment(H, E)
    model.set_segment(F_t, F_b)

    # Collinear sections
    model.set_section([A, G, B])
    model.set_section([D, H, E])

    return model


if __name__ == "__main__":
    construct_0311_g1()
