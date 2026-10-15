"""Programmatic construction for Book X, Proposition 73 (0162.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0162_g1() -> Model:
    """Construct the figure 0162.g1 using geometor.model."""
    model = Model("0162.g1")

    # Rational straight line AB with rational straight line BC subtracted, leaving apotome AC
    A = model.set_point(17.0, -19.0, classes=["given"], label="A")
    C = model.set_point(72.0, -19.0, classes=["given"], label="C")
    B = model.set_point(169.0, -19.0, classes=["given"], label="B")

    # Base line
    model.construct_line(A, B)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Section
    model.set_section([A, C, B])

    return model


if __name__ == "__main__":
    construct_0162_g1()
