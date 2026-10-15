"""Programmatic construction for Book V, Proposition 2 (0145.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0145_g1() -> Model:
    """Construct the figure 0145.g1 using geometor.model."""
    model = Model("0145.g1")

    # Points on AG (divided at B) and DH (divided at E)
    A = model.set_point(26.0, -27.0, classes=["given"], label="A")
    B = model.set_point(134.0, -27.0, classes=["given"], label="B")
    G = model.set_point(206.0, -27.0, classes=["given"], label="G")

    D = model.set_point(26.0, -81.0, classes=["given"], label="D")
    E = model.set_point(176.0, -81.0, classes=["given"], label="E")
    H = model.set_point(276.0, -81.0, classes=["given"], label="H")

    # Single-letter magnitudes C and F
    C_l = model.set_point(26.0, -57.0, classes=["given"], label="C")
    C_r = model.set_point(62.0, -57.0, label="C_r")
    F_l = model.set_point(26.0, -109.0, classes=["given"], label="F")
    F_r = model.set_point(76.0, -109.0, label="F_r")

    # Base lines
    model.construct_line(A, G)
    model.construct_line(D, H)

    # Whole and subdivided segments
    model.set_segment(A, G)
    model.set_segment(A, B)
    model.set_segment(B, G)
    model.set_segment(D, H)
    model.set_segment(D, E)
    model.set_segment(E, H)
    model.set_segment(C_l, C_r)
    model.set_segment(F_l, F_r)

    # Collinear sections
    model.set_section([A, B, G])
    model.set_section([D, E, H])

    return model


if __name__ == "__main__":
    construct_0145_g1()
