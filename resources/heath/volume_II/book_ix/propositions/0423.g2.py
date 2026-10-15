"""Programmatic construction for Book IX, Proposition 31 (0423.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0423_g2() -> Model:
    """Construct the figure 0423.g2 using geometor.model."""
    model = Model("0423.g2")

    # Single-letter horizontal number segments A, B, C, D
    A_l = model.set_point(31.0, -19.5, classes=["given"], label="A")
    A_r = model.set_point(98.0, -19.5, label="A_r")

    B_l = model.set_point(33.0, -43.0, classes=["given"], label="B")
    B_r = model.set_point(147.0, -43.0, label="B_r")

    C_l = model.set_point(34.0, -65.5, classes=["given"], label="C")
    C_r = model.set_point(250.0, -65.5, label="C_r")

    D_l = model.set_point(34.0, -87.0, classes=["given"], label="D")
    D_r = model.set_point(60.0, -87.0, label="D_r")

    # Number segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_0423_g2()
