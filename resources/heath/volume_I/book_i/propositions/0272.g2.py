"""Programmatic construction for Book I, Proposition 7 (0272.g2).

Given two straight lines constructed on a straight line (from its extremities)
and meeting in a point, there cannot be constructed on the same straight line
(from its extremities), and on the same side of it, two other straight lines
meeting in another point and equal to the former two respectively, namely each
to that which has the same extremity with it.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0272_g2() -> Model:
    """Construct the figure for Book I, Proposition 7 using geometor.model."""
    model = Model("0272.g2")

    # 1. Given base AB and two pairs of straight lines AC, CB and AD, DB meeting at C and D
    A = model.set_point(13, -112, classes=["given"], label="A")
    B = model.set_point(134, -112, classes=["given"], label="B")
    C = model.set_point(100, -26, label="C")
    D = model.set_point(126, -38, label="D")

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(A, D)
    model.set_segment(D, B)

    # 2. Let CD be joined [Post. 1]
    model.set_segment(C, D)

    # 3. Triangles ABC, ABD, ACD, BCD
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, C, D])
    model.set_polygon([B, C, D])

    return model


if __name__ == "__main__":
    construct_0272_g2()
