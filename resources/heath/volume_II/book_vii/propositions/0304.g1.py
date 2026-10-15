"""Programmatic construction for Book VII, Proposition 2 (0304.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0304_g1() -> Model:
    """Construct the figure 0304.g1 using geometor.model."""
    model = Model("0304.g1")

    # Vertical number segment AB (divided at E)
    A = model.set_point(23.0, -12.0, classes=["given"], label="A")
    E = model.set_point(23.0, -43.0, label="E")
    B = model.set_point(23.0, -129.0, classes=["given"], label="B")

    # Vertical number segment CD (divided at F)
    C = model.set_point(59.0, -43.0, classes=["given"], label="C")
    F = model.set_point(59.0, -60.0, label="F")
    D = model.set_point(59.0, -129.0, classes=["given"], label="D")

    # Single-letter number segment G
    G_t = model.set_point(93.0, -73.0, classes=["given"], label="G")
    G_b = model.set_point(93.0, -113.0, label="G_b")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Whole and subdivided segments on AB
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)

    # Whole and subdivided segments on CD
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)

    # Single-letter segment G
    model.set_segment(G_t, G_b)

    # Collinear sections
    model.set_section([A, E, B])
    model.set_section([C, F, D])

    return model


if __name__ == "__main__":
    construct_0304_g1()
