"""Programmatic construction for Book VII, Proposition 18 (0324.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0324_g1() -> Model:
    """Construct the figure 0324.g1 using geometor.model."""
    model = Model("0324.g1")

    # Single-letter horizontal number segments C, A, B, D, E
    C_l = model.set_point(23.0, -14.0, classes=["given"], label="C")
    C_r = model.set_point(58.0, -14.0, label="C_r")

    A_l = model.set_point(101.0, -14.0, classes=["given"], label="A")
    A_r = model.set_point(181.0, -14.0, label="A_r")

    B_l = model.set_point(102.0, -35.0, classes=["given"], label="B")
    B_r = model.set_point(217.0, -35.0, label="B_r")

    D_l = model.set_point(102.0, -55.0, classes=["given"], label="D")
    D_r = model.set_point(197.0, -55.0, label="D_r")

    E_l = model.set_point(102.0, -80.0, classes=["given"], label="E")
    E_r = model.set_point(245.0, -80.0, label="E_r")

    # Number segments
    model.set_segment(C_l, C_r)
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_0324_g1()
