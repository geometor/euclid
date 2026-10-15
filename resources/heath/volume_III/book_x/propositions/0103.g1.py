"""Programmatic construction for Book X, Proposition 46 (0103.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0103_g1() -> Model:
    """Construct the figure 0103.g1 using geometor.model."""
    model = Model("0103.g1")

    # Side of a rational plus a medial area AB divided at C and D
    A = model.set_point(18.0, -20.0, classes=["given"], label="A")
    D = model.set_point(75.0, -20.0, label="D")
    C = model.set_point(104.0, -20.0, classes=["given"], label="C")
    B = model.set_point(204.0, -20.0, classes=["given"], label="B")

    model.construct_line(A, B)

    # Whole and all sub-segments on AB
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(D, C)
    model.set_segment(D, B)
    model.set_segment(C, B)

    # Collinear sections on AB
    model.set_section([A, C, B])
    model.set_section([A, D, B])

    return model


if __name__ == "__main__":
    construct_0103_g1()
