"""Programmatic construction for Book VII, Proposition 36, Case 2 (0346.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0346_g1() -> Model:
    """Construct the figure 0346.g1 using geometor.model."""
    model = Model("0346.g1")

    # Given numbers A, B, C
    A_l = model.set_point(22.0, -15.0, classes=["given"], label="A")
    A_r = model.set_point(81.0, -15.0, label="A_r")

    B_l = model.set_point(22.0, -40.0, classes=["given"], label="B")
    B_r = model.set_point(99.0, -40.0, label="B_r")

    C_l = model.set_point(23.0, -62.0, classes=["given"], label="C")
    C_r = model.set_point(109.0, -62.0, label="C_r")

    # Least number D measured by A, B; least number E measured by C, D; and lesser number F
    D_l = model.set_point(23.0, -87.0, classes=["given"], label="D")
    D_r = model.set_point(116.0, -87.0, label="D_r")

    E_l = model.set_point(22.0, -110.0, classes=["given"], label="E")
    E_r = model.set_point(159.0, -110.0, label="E_r")

    F_l = model.set_point(23.0, -136.0, classes=["given"], label="F")
    F_r = model.set_point(134.0, -136.0, label="F_r")

    # Segments
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)
    model.set_segment(D_l, D_r)
    model.set_segment(E_l, E_r)
    model.set_segment(F_l, F_r)

    return model


if __name__ == "__main__":
    construct_0346_g1()
