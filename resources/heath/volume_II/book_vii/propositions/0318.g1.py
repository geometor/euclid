"""Programmatic construction for Book VII, Proposition 12 (0318.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0318_g1() -> Model:
    """Construct the figure 0318.g1 using geometor.model."""
    model = Model("0318.g1")

    # Single-letter vertical number segments A, B, C, D
    A_t = model.set_point(26.0, -36.0, classes=["given"], label="A")
    A_b = model.set_point(26.0, -69.0, label="A_b")

    B_t = model.set_point(50.0, -34.0, classes=["given"], label="B")
    B_b = model.set_point(50.0, -69.0, label="B_b")

    C_t = model.set_point(72.0, -14.0, classes=["given"], label="C")
    C_b = model.set_point(72.0, -72.0, label="C_b")

    D_t = model.set_point(102.0, -10.0, classes=["given"], label="D")
    D_b = model.set_point(102.0, -73.0, label="D_b")

    # Number segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)
    model.set_segment(D_t, D_b)

    return model


if __name__ == "__main__":
    construct_0318_g1()
