"""Programmatic construction for Book X, Proposition 39 (0092.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0092_g1() -> Model:
    """Construct the figure 0092.g1 using geometor.model."""
    model = Model("0092.g1")

    # Straight line AC divided into straight lines AB, BC incommensurable in square
    A = model.set_point(17.0, -17.5, classes=["given"], label="A")
    B = model.set_point(135.0, -17.5, classes=["given"], label="B")
    C = model.set_point(215.0, -17.5, classes=["given"], label="C")

    model.construct_line(A, C)

    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)

    model.set_section([A, B, C])

    return model


if __name__ == "__main__":
    construct_0092_g1()
