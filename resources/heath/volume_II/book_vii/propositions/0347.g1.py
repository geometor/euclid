"""Programmatic construction for Book VII, Proposition 37 (0347.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0347_g1() -> Model:
    """Construct the figure 0347.g1 using geometor.model."""
    model = Model("0347.g1")

    # Number A, measuring number B, unit-count C, and unit D
    A_l = model.set_point(23.0, -14.0, classes=["given"], label="A")
    A_r = model.set_point(153.0, -14.0, label="A_r")

    B_l = model.set_point(22.0, -39.0, classes=["given"], label="B")
    B_r = model.set_point(68.0, -39.0, label="B_r")

    C_l = model.set_point(23.0, -66.0, classes=["given"], label="C")
    C_r = model.set_point(90.0, -66.0, label="C_r")

    D_l = model.set_point(24.0, -88.0, classes=["given"], label="D")
    D_r = model.set_point(48.0, -88.0, label="D_r")

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_0347_g1()
