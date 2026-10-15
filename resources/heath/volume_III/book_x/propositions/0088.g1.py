"""Programmatic construction for Book X, Proposition 37 (0088.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0088_g1() -> Model:
    """Construct the figure 0088.g1 using geometor.model."""
    model = Model("0088.g1")

    # Straight line AC divided into medial straight lines AB, BC
    A = model.set_point(16.0, -20.0, classes=["given"], label="A")
    B = model.set_point(145.0, -20.0, classes=["given"], label="B")
    C = model.set_point(242.0, -20.0, classes=["given"], label="C")

    model.construct_line(A, C)

    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)

    model.set_section([A, B, C])

    return model


if __name__ == "__main__":
    construct_0088_g1()
