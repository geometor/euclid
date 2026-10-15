"""Programmatic construction for Book VII, Proposition 24 (0331.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0331_g1() -> Model:
    """Construct the figure 0331.g1 using geometor.model."""
    model = Model("0331.g1")

    # Single-letter vertical number segments A, B, C, D, E, F
    A_t = model.set_point(15.0, -11.0, classes=["given"], label="A")
    A_b = model.set_point(15.0, -108.0, label="A_b")

    B_t = model.set_point(39.0, -10.0, classes=["given"], label="B")
    B_b = model.set_point(39.0, -87.0, label="B_b")

    C_t = model.set_point(60.0, -11.0, classes=["given"], label="C")
    C_b = model.set_point(60.0, -124.0, label="C_b")

    D_t = model.set_point(86.0, -10.0, classes=["given"], label="D")
    D_b = model.set_point(86.0, -160.0, label="D_b")

    E_t = model.set_point(109.0, -13.0, classes=["given"], label="E")
    E_b = model.set_point(109.0, -91.0, label="E_b")

    F_t = model.set_point(136.0, -16.0, classes=["given"], label="F")
    F_b = model.set_point(136.0, -80.0, label="F_b")

    # Number segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)
    model.set_segment(D_t, D_b)
    model.set_segment(E_t, E_b)
    model.set_segment(F_t, F_b)

    return model


if __name__ == "__main__":
    construct_0331_g1()
