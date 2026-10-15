"""Programmatic construction for Book IX, Proposition 14 (0409.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0409_g1() -> Model:
    """Construct the figure 0409.g1 using geometor.model."""
    model = Model("0409.g1")

    # Left column: single-letter horizontal number segments A, E, F
    A_l = model.set_point(32.0, -20.0, classes=["given"], label="A")
    A_r = model.set_point(174.0, -20.0, label="A_r")

    E_l = model.set_point(31.0, -42.5, classes=["given"], label="E")
    E_r = model.set_point(101.0, -42.5, label="E_r")

    F_l = model.set_point(34.0, -71.5, classes=["given"], label="F")
    F_r = model.set_point(94.0, -71.5, label="F_r")

    # Right column: single-letter horizontal number segments B, C, D
    B_l = model.set_point(263.0, -19.5, classes=["given"], label="B")
    B_r = model.set_point(289.0, -19.5, label="B_r")

    C_l = model.set_point(263.0, -42.5, classes=["given"], label="C")
    C_r = model.set_point(305.0, -42.5, label="C_r")

    D_l = model.set_point(263.0, -60.5, classes=["given"], label="D")
    D_r = model.set_point(317.0, -60.5, label="D_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_0409_g1()
