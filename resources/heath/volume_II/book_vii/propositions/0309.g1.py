"""Programmatic construction for Book VII, Proposition 4 (0309.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0309_g1() -> Model:
    """Construct the figure 0309.g1 using geometor.model."""
    model = Model("0309.g1")

    # Single-letter vertical number segment A
    A_t = model.set_point(22.0, -10.0, classes=["given"], label="A")
    A_b = model.set_point(22.0, -159.0, label="A_b")

    # Vertical number segment BC (divided at E and F)
    B = model.set_point(54.0, -69.0, classes=["given"], label="B")
    E = model.set_point(54.0, -99.0, label="E")
    F = model.set_point(54.0, -129.0, label="F")
    C = model.set_point(54.0, -159.0, classes=["given"], label="C")

    # Single-letter vertical number segment D
    D_t = model.set_point(83.0, -129.0, classes=["given"], label="D")
    D_b = model.set_point(83.0, -159.0, label="D_b")

    # Base line
    model.construct_line(B, C)

    # Whole and subdivided segments
    model.set_segment(A_t, A_b)
    model.set_segment(B, C)
    model.set_segment(B, E)
    model.set_segment(E, F)
    model.set_segment(F, C)
    model.set_segment(B, F)
    model.set_segment(E, C)
    model.set_segment(D_t, D_b)

    # Collinear sections
    model.set_section([B, E, F])
    model.set_section([B, F, C])
    model.set_section([E, F, C])

    return model


if __name__ == "__main__":
    construct_0309_g1()
