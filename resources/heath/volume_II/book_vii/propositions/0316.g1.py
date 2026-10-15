"""Programmatic construction for Book VII, Proposition 10 (0316.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0316_g1() -> Model:
    """Construct the figure 0316.g1 using geometor.model."""
    model = Model("0316.g1")

    # Vertical number segment AB (divided at G)
    A = model.set_point(24.0, -63.0, classes=["given"], label="A")
    G = model.set_point(24.0, -101.0, label="G")
    B = model.set_point(24.0, -140.0, classes=["given"], label="B")

    # Single-letter vertical number segment C
    C_t = model.set_point(52.0, -27.0, classes=["given"], label="C")
    C_b = model.set_point(52.0, -136.0, label="C_b")

    # Vertical number segment DE (divided at H)
    D = model.set_point(91.0, -55.0, classes=["given"], label="D")
    H = model.set_point(91.0, -97.0, label="H")
    E = model.set_point(91.0, -140.0, classes=["given"], label="E")

    # Single-letter vertical number segment F
    F_t = model.set_point(120.0, -11.0, classes=["given"], label="F")
    F_b = model.set_point(120.0, -141.0, label="F_b")

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
    construct_0316_g1()
