"""Programmatic construction for Book II, Proposition 2 (0390.g1).

If a straight line be cut at random, the rectangle contained by the whole and
both of the segments is equal to the square on the whole.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0390_g1() -> Model:
    """Construct the figure for Book II, Proposition 2 using geometor.model."""
    model = Model("0390.g1")

    # Straight line AB cut at random at C
    A = model.set_point(20.5, -29.5, classes=["given"], label="A")
    C = model.set_point(60.5, -29.5, classes=["given"], label="C")
    B = model.set_point(137.5, -29.5, classes=["given"], label="B")

    model.construct_line(A, B)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Square ADEB described on AB [I. 46], and parallel CF to AD/BE [I. 31]
    D = model.set_point(20.5, -146.5, label="D")
    F = model.set_point(60.5, -146.5, label="F")
    E = model.set_point(137.5, -146.5, label="E")

    model.set_segment(A, D)
    model.set_segment(B, E)
    model.set_segment(C, F)
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(F, E)

    # Square ADEB (AE) and sub-rectangles ACFD (AF) and CBEF (CE)
    model.set_polygon([A, D, E, B])
    model.set_polygon([A, C, F, D])
    model.set_polygon([C, B, E, F])

    return model


if __name__ == "__main__":
    construct_0390_g1()
