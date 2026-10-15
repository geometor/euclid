"""Programmatic construction for Book II, Proposition 3 (0392.g1).

If a straight line be cut at random, the rectangle contained by the whole and
one of the segments is equal to the rectangle contained by the segments and the
square on the aforesaid segment.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0392_g1() -> Model:
    """Construct the figure for Book II, Proposition 3 using geometor.model."""
    model = Model("0392.g1")

    # Straight line AB cut at random at C
    A = model.set_point(18.5, -29.5, classes=["given"], label="A")
    C = model.set_point(71.5, -29.5, classes=["given"], label="C")
    B = model.set_point(173.5, -29.5, classes=["given"], label="B")

    model.construct_line(A, B)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Square CDEB described on CB [I. 46], ED drawn through to F, and AF parallel to CD/BE [I. 31]
    F = model.set_point(18.5, -129.5, label="F")
    D = model.set_point(71.5, -129.5, label="D")
    E = model.set_point(173.5, -129.5, label="E")

    model.construct_line(E, F)
    model.set_segment(F, E)
    model.set_segment(F, D)
    model.set_segment(D, E)

    model.set_segment(A, F)
    model.set_segment(C, D)
    model.set_segment(B, E)

    # Whole rectangle ABEF (AE), rectangle ACDF (AD), and square CDEB (CE / DB)
    model.set_polygon([A, B, E, F])
    model.set_polygon([A, C, D, F])
    model.set_polygon([C, B, E, D])

    return model


if __name__ == "__main__":
    construct_0392_g1()
