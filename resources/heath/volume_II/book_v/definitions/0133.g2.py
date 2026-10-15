"""Programmatic construction for Book V, Definition 5 note (0133.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0133_g2() -> Model:
    """Construct the figure 0133.g2 using geometor.model."""
    model = Model("0133.g2")

    # Magnitude endpoints: A, B, C, D
    A_l = model.set_point(24.0, -28.0, classes=["given"], label="A")
    A_r = model.set_point(65.0, -28.0, label="A_r")
    B_l = model.set_point(24.0, -50.0, classes=["given"], label="B")
    B_r = model.set_point(150.0, -50.0, label="B_r")
    C_l = model.set_point(24.0, -73.0, classes=["given"], label="C")
    C_r = model.set_point(52.0, -73.0, label="C_r")
    D_l = model.set_point(24.0, -95.0, classes=["given"], label="D")
    D_r = model.set_point(110.0, -95.0, label="D_r")

    # Magnitude segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)

    return model


if __name__ == "__main__":
    construct_0133_g2()
