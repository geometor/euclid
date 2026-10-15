"""Programmatic construction for Book V, Proposition 10 (0161.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0161_g1() -> Model:
    """Construct the figure 0161.g1 for Book V, Proposition 10 using geometor.model."""
    model = Model("0161.g1")

    # Standalone magnitudes A, B, C
    A_1 = model.set_point(35.0, -16.0, classes=["given"], label="A_1")
    A_2 = model.set_point(199.0, -16.0, classes=["given"], label="A_2")
    B_1 = model.set_point(235.0, -16.0, classes=["given"], label="B_1")
    B_2 = model.set_point(341.0, -16.0, classes=["given"], label="B_2")
    C_1 = model.set_point(129.0, -42.0, classes=["given"], label="C_1")
    C_2 = model.set_point(270.0, -42.0, classes=["given"], label="C_2")

    model.set_segment(A_1, A_2)
    model.set_segment(B_1, B_2)
    model.set_segment(C_1, C_2)

    return model


if __name__ == "__main__":
    construct_0161_g1()
