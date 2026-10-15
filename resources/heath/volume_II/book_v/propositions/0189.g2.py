"""Programmatic construction for Book V, Proposition 24 (0189.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0189_g2() -> Model:
    """Construct the figure 0189.g2 for Book V, Proposition 24 using geometor.model."""
    model = Model("0189.g2")

    # First subdivided magnitude AG divided at B
    A = model.set_point(30.00, -38.00, classes=["given"], label="A")
    B = model.set_point(160.00, -38.00, classes=["given"], label="B")
    G = model.set_point(252.00, -38.00, classes=["given"], label="G")

    # Standalone magnitude C
    C_1 = model.set_point(30.00, -62.00, classes=["given"], label="C_1")
    C_2 = model.set_point(125.00, -62.00, classes=["given"], label="C_2")

    # Second subdivided magnitude DH divided at E
    D = model.set_point(30.00, -84.00, classes=["given"], label="D")
    E = model.set_point(136.00, -84.00, classes=["given"], label="E")
    H = model.set_point(211.00, -84.00, classes=["given"], label="H")

    # Standalone magnitude F
    F_1 = model.set_point(30.00, -108.00, classes=["given"], label="F_1")
    F_2 = model.set_point(104.00, -108.00, classes=["given"], label="F_2")

    # Base lines
    model.construct_line(A, G)
    model.construct_line(D, H)

    # Whole and subdivided segments
    model.set_segment(A, G)
    model.set_segment(A, B)
    model.set_segment(B, G)

    model.set_segment(C_1, C_2)

    model.set_segment(D, H)
    model.set_segment(D, E)
    model.set_segment(E, H)

    model.set_segment(F_1, F_2)

    # Collinear sections
    model.set_section([A, B, G])
    model.set_section([D, E, H])

    return model


if __name__ == "__main__":
    construct_0189_g2()
