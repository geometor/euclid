"""Programmatic construction for Book VII, Proposition 3 (0306.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0306_g1() -> Model:
    """Construct the figure 0306.g1 using geometor.model."""
    model = Model("0306.g1")

    # Single-letter vertical number segments A, B, C, D, E, F
    A_t = model.set_point(29.0, -12.0, classes=["given"], label="A")
    A_b = model.set_point(29.0, -124.0, label="A_b")

    B_t = model.set_point(63.0, -41.0, classes=["given"], label="B")
    B_b = model.set_point(63.0, -126.0, label="B_b")

    C_t = model.set_point(89.0, -75.0, classes=["given"], label="C")
    C_b = model.set_point(89.0, -124.0, label="C_b")

    D_t = model.set_point(129.0, -95.0, classes=["given"], label="D")
    D_b = model.set_point(129.0, -125.0, label="D_b")

    E_t = model.set_point(159.0, -98.0, classes=["given"], label="E")
    E_b = model.set_point(159.0, -120.0, label="E_b")

    F_t = model.set_point(183.0, -97.0, classes=["given"], label="F")
    F_b = model.set_point(183.0, -121.0, label="F_b")

    # Number segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)
    model.set_segment(D_t, D_b)
    model.set_segment(E_t, E_b)
    model.set_segment(F_t, F_b)

    return model


if __name__ == "__main__":
    construct_0306_g1()
