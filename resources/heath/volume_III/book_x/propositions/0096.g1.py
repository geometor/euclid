"""Programmatic construction for Book X, Proposition 42 (0096.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0096_g1() -> Model:
    """Construct the figure 0096.g1 using geometor.model."""
    model = Model("0096.g1")

    # Binomial straight line AB divided at C and D
    A = model.set_point(15.0, -20.0, classes=["given"], label="A")
    D = model.set_point(121.0, -20.0, label="D")
    C = model.set_point(166.0, -20.0, classes=["given"], label="C")
    B = model.set_point(241.0, -20.0, classes=["given"], label="B")

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
    model.set_section([A, D, C])
    model.set_section([D, C, B])

    return model


if __name__ == "__main__":
    construct_0096_g1()
