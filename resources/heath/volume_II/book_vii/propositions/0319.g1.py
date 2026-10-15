"""Programmatic construction for Book VII, Proposition 13 (0319.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0319_g1() -> Model:
    """Construct the figure 0319.g1 using geometor.model."""
    model = Model("0319.g1")

    # Single-letter vertical number segments A, B, C, D
    A_t = model.set_point(24.0, -13.0, classes=["given"], label="A")
    A_b = model.set_point(24.0, -108.0, label="A_b")

    B_t = model.set_point(54.0, -14.0, classes=["given"], label="B")
    B_b = model.set_point(54.0, -73.0, label="B_b")

    C_t = model.set_point(80.0, -13.0, classes=["given"], label="C")
    C_b = model.set_point(80.0, -86.0, label="C_b")

    D_t = model.set_point(112.0, -58.0, classes=["given"], label="D")
    D_b = model.set_point(112.0, -104.0, label="D_b")

    # Number segments
    model.set_segment(A_t, A_b)
    model.set_segment(B_t, B_b)
    model.set_segment(C_t, C_b)
    model.set_segment(D_t, D_b)

    return model


if __name__ == "__main__":
    construct_0319_g1()
