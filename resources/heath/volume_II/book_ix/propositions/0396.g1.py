"""Programmatic construction for Book IX, Proposition 8 (0396.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0396_g1() -> Model:
    """Construct the figure 0396.g1 using geometor.model."""
    model = Model("0396.g1")

    # Single-letter horizontal number segments A, B, C, D, E, F
    A_l = model.set_point(31.0, -20.5, classes=["given"], label="A")
    A_r = model.set_point(76.0, -20.5, label="A_r")

    B_l = model.set_point(33.0, -39.5, classes=["given"], label="B")
    B_r = model.set_point(88.0, -39.5, label="B_r")

    C_l = model.set_point(34.0, -58.5, classes=["given"], label="C")
    C_r = model.set_point(110.0, -58.5, label="C_r")

    D_l = model.set_point(34.0, -80.5, classes=["given"], label="D")
    D_r = model.set_point(128.0, -80.5, label="D_r")

    E_l = model.set_point(34.0, -102.5, classes=["given"], label="E")
    E_r = model.set_point(143.0, -102.5, label="E_r")

    F_l = model.set_point(35.0, -124.5, classes=["given"], label="F")
    F_r = model.set_point(165.0, -124.5, label="F_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)

    return model


if __name__ == "__main__":
    construct_0396_g1()
