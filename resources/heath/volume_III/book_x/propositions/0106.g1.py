"""Programmatic construction for Book X, Proposition 48 (0106.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0106_g1() -> Model:
    """Construct the figure 0106.g1 using geometor.model."""
    model = Model("0106.g1")

    # Single-letter magnitude segments D and H
    D_l = model.set_point(15.0, -21.0, classes=["given"], label="D")
    D_r = model.set_point(91.0, -21.0, label="D_r")

    H_l = model.set_point(145.0, -20.5, classes=["given"], label="H")
    H_r = model.set_point(207.0, -20.5, label="H_r")

    # Line EG divided at F
    E = model.set_point(23.0, -55.5, classes=["given"], label="E")
    F = model.set_point(125.0, -55.5, classes=["given"], label="F")
    G = model.set_point(191.0, -55.5, classes=["given"], label="G")

    # Number line AB divided at C
    A = model.set_point(91.0, -87.5, classes=["given"], label="A")
    C = model.set_point(167.0, -87.5, classes=["given"], label="C")
    B = model.set_point(212.0, -87.5, classes=["given"], label="B")

    # Base lines
    model.construct_line(D_l, D_r)
    model.construct_line(H_l, H_r)
    model.construct_line(E, G)
    model.construct_line(A, B)

    # Segments
    model.set_segment(D_l, D_r)
    model.set_segment(H_l, H_r)
    model.set_segment(E, G)
    model.set_segment(E, F)
    model.set_segment(F, G)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Collinear sections
    model.set_section([E, F, G])
    model.set_section([A, C, B])

    return model


if __name__ == "__main__":
    construct_0106_g1()
