"""Programmatic construction for Book X, Proposition 32 (0076.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0076_g1() -> Model:
    """Construct the figure 0076.g1 using geometor.model."""
    model = Model("0076.g1")

    # Rational straight lines A, B, C
    A_l = model.set_point(32.0, -19.5, classes=["given"], label="A")
    A_r = model.set_point(157.0, -19.5, label="A_r")

    B_l = model.set_point(31.0, -52.5, classes=["given"], label="B")
    B_r = model.set_point(142.0, -52.5, label="B_r")

    C_l = model.set_point(31.0, -84.5, classes=["given"], label="C")
    C_r = model.set_point(115.0, -84.5, label="C_r")

    # Medial straight lines D, E
    D_l = model.set_point(214.0, -38.5, label="D")
    D_r = model.set_point(333.0, -38.5, label="D_r")

    E_l = model.set_point(214.0, -70.5, label="E")
    E_r = model.set_point(294.0, -70.5, label="E_r")

    for p_l, p_r in [(A_l, A_r), (B_l, B_r), (C_l, C_r), (D_l, D_r), (E_l, E_r)]:
        model.construct_line(p_l, p_r)
        model.set_segment(p_l, p_r)

    return model


if __name__ == "__main__":
    construct_0076_g1()
