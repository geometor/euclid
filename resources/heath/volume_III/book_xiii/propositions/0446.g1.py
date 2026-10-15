"""Programmatic construction for Book XIII, Proposition 1 Analysis (0446.g1).

Straight line AB divided in extreme and mean ratio at C, with AD = 1/2 AB.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0446_g1() -> Model:
    """Construct the figure 0446.g1 using geometor.model."""
    model = Model("0446.g1")

    D = model.set_point(23.0, -25.0, classes=["given"], label="D")
    A = model.set_point(86.0, -25.0, classes=["given"], label="A")
    C = model.set_point(166.0, -25.0, classes=["given"], label="C")
    B = model.set_point(215.0, -25.0, classes=["given"], label="B")

    model.construct_line(D, B)
    model.set_segment(D, B)
    model.set_segment(D, C)
    model.set_segment(D, A)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    return model


if __name__ == "__main__":
    construct_0446_g1()
