"""Programmatic construction for Book X, Proposition 86 (0184.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0184_g1() -> Model:
    """Construct the figure 0184.g1 using geometor.model."""
    model = Model("0184.g1")

    # Single-letter magnitude segments A and H
    A_l = model.set_point(63.0, -18.0, classes=["given"], label="A")
    A_r = model.set_point(194.0, -18.0, label="A_r")

    H_l = model.set_point(38.0, -83.5, classes=["given"], label="H")
    H_r = model.set_point(168.0, -83.5, label="H_r")

    # Line BG divided at C
    B = model.set_point(24.0, -50.5, classes=["given"], label="B")
    C = model.set_point(68.0, -50.5, classes=["given"], label="C")
    G = model.set_point(242.0, -50.5, classes=["given"], label="G")

    # Number line ED divided at F
    E = model.set_point(54.0, -111.5, classes=["given"], label="E")
    F = model.set_point(105.0, -111.5, classes=["given"], label="F")
    D = model.set_point(196.0, -111.5, classes=["given"], label="D")

    # Base lines
    model.construct_line(A_l, A_r)
    model.construct_line(B, G)
    model.construct_line(H_l, H_r)
    model.construct_line(E, D)

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B, G)
    model.set_segment(B, C)
    model.set_segment(C, G)
    model.set_segment(H_l, H_r)
    model.set_segment(E, D)
    model.set_segment(E, F)
    model.set_segment(F, D)

    # Collinear sections
    model.set_section([B, C, G])
    model.set_section([E, F, D])

    return model


if __name__ == "__main__":
    construct_0184_g1()
