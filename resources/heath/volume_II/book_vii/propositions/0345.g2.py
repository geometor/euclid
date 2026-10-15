"""Programmatic construction for Book VII, Proposition 36, Case 1 (0345.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0345_g2() -> Model:
    """Construct the figure 0345.g2 using geometor.model."""
    model = Model("0345.g2")

    # Given numbers A, B, C
    A_l = model.set_point(21.0, -14.0, classes=["given"], label="A")
    A_r = model.set_point(82.0, -14.0, label="A_r")

    B_l = model.set_point(22.0, -38.0, classes=["given"], label="B")
    B_r = model.set_point(86.0, -38.0, label="B_r")

    C_l = model.set_point(22.0, -60.0, classes=["given"], label="C")
    C_r = model.set_point(105.0, -60.0, label="C_r")

    # Least number D measured by A, B and lesser number E
    D_l = model.set_point(20.0, -84.0, classes=["given"], label="D")
    D_r = model.set_point(163.0, -84.0, label="D_r")

    E_l = model.set_point(20.0, -106.0, classes=["given"], label="E")
    E_r = model.set_point(135.0, -106.0, label="E_r")

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)

    return model


if __name__ == "__main__":
    construct_0345_g2()
