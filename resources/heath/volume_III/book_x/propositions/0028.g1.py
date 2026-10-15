"""Programmatic construction for Book X, Proposition 5 (0028.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0028_g1() -> Model:
    """Construct the magnitude/number bars A, B, C, D, E for Book X, Proposition 5 (0028.g1)."""
    model = Model("0028.g1")

    # Single-letter magnitudes A, B, C and numbers D, E
    A_l = model.set_point(18.0, -25.5, classes=["given"], label="A")
    A_r = model.set_point(144.0, -25.5, label="A_r")

    B_l = model.set_point(186.0, -25.5, classes=["given"], label="B")
    B_r = model.set_point(267.0, -25.5, label="B_r")

    C_l = model.set_point(302.0, -26.5, label="C")
    C_r = model.set_point(344.0, -26.5, label="C_r")

    D_l = model.set_point(100.0, -49.5, label="D")
    D_r = model.set_point(162.0, -49.5, label="D_r")

    E_l = model.set_point(108.0, -73.5, label="E")
    E_r = model.set_point(141.0, -73.5, label="E_r")

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_0028_g1()
