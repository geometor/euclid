"""Programmatic construction for Book II, Proposition 13 right-triangle case (0421.g1).

Right-angled triangle ABC reducing Book II, Proposition 13 to I. 47.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0421_g1() -> Model:
    """Construct the figure for 0421.g1 using geometor.model."""
    model = Model("0421.g1")

    B = model.set_point(0, 0, classes=["given"], label="B")
    C = model.set_point(4, 0, classes=["given"], label="C")
    A = model.set_point(4, 3, classes=["given"], label="A")

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_polygon([A, B, C])

    model.set_wedge(B, C, C, A)
    model.set_wedge(C, A, A, B)

    return model


if __name__ == "__main__":
    construct_0421_g1()
