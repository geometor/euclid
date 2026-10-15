"""Programmatic construction for Book VII, Proposition 21 (0328.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0328_g1() -> Model:
    """Construct the figure 0328.g1 using geometor.model."""
    model = Model("0328.g1")

    # Single-letter vertical number segments A, B, C, D, E
    A_t = model.set_point(22.0, -10.0, classes=["given"], label="A")
    A_b = model.set_point(22.0, -114.0, label="A_b")

    B_t = model.set_point(49.0, -16.0, classes=["given"], label="B")
    B_b = model.set_point(49.0, -89.0, label="B_b")

    C_t = model.set_point(128.0, -15.0, classes=["given"], label="C")
    C_b = model.set_point(128.0, -70.0, label="C_b")

    D_t = model.set_point(152.0, -12.0, classes=["given"], label="D")
    D_b = model.set_point(152.0, -54.0, label="D_b")

    E_t = model.set_point(198.0, -17.0, classes=["given"], label="E")
    E_b = model.set_point(198.0, -43.0, label="E_b")

    # Number segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)
    model.set_segment(D_t, D_b)
    model.set_segment(E_t, E_b)

    return model


if __name__ == "__main__":
    construct_0328_g1()
