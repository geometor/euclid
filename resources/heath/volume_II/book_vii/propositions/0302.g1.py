"""Programmatic construction for Book VII, Proposition 1 (0302.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0302_g1() -> Model:
    """Construct the figure 0302.g1 using geometor.model."""
    model = Model("0302.g1")

    # Vertical number segment AB (divided at H and F)
    A = model.set_point(24.0, -21.0, classes=["given"], label="A")
    H = model.set_point(24.0, -31.0, label="H")
    F = model.set_point(24.0, -48.0, label="F")
    B = model.set_point(24.0, -152.0, classes=["given"], label="B")

    # Vertical number segment CD (divided at G)
    C = model.set_point(63.0, -48.0, classes=["given"], label="C")
    G = model.set_point(63.0, -60.0, label="G")
    D = model.set_point(63.0, -152.0, classes=["given"], label="D")

    # Single-letter number segment E
    E_t = model.set_point(101.0, -118.0, classes=["given"], label="E")
    E_b = model.set_point(101.0, -151.0, label="E_b")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Whole and subdivided segments on AB
    model.set_segment(A, B)
    model.set_segment(A, H)
    model.set_segment(H, F)
    model.set_segment(F, B)
    model.set_segment(A, F)
    model.set_segment(H, B)

    # Whole and subdivided segments on CD
    model.set_segment(C, D)
    model.set_segment(C, G)
    model.set_segment(G, D)

    # Single-letter segment E
    model.set_segment(E_t, E_b)

    # Collinear sections
    model.set_section([A, H, F])
    model.set_section([A, F, B])
    model.set_section([H, F, B])
    model.set_section([C, G, D])

    return model


if __name__ == "__main__":
    construct_0302_g1()
