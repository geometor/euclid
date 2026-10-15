"""Programmatic construction for Book XIII, Proposition 6 (0454.g1).

If a rational straight line be cut in extreme and mean ratio, each of the
segments is the irrational straight line called apotome.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0454_g1() -> Model:
    """Construct the figure for Book XIII, Proposition 6 using geometor.model."""
    model = Model("0454.g1")

    D = model.set_point(12.0, -26.0, classes=["given"], label="D")
    A = model.set_point(78.0, -26.0, classes=["given"], label="A")
    C = model.set_point(156.0, -26.0, classes=["given"], label="C")
    B = model.set_point(211.0, -26.0, classes=["given"], label="B")

    model.construct_line(D, B)
    model.set_segment(D, B)
    model.set_segment(D, C)
    model.set_segment(D, A)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    return model


if __name__ == "__main__":
    construct_0454_g1()
