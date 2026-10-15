"""Programmatic construction for Book I, Common Notions commentary (0252.g1).

Intersections of two circles, Lemma Case 1: Point A lies on O'O produced.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0252_g1() -> Model:
    """Construct the figure for 0252.g1 using geometor.model."""
    model = Model("0252.g1")

    # Centres O, O' and points A, B, X, Y on circle C
    O = model.set_point(80, -90, classes=["given"], label="O")
    Op = model.set_point(122, -90, classes=["given"], label="O'")
    A = model.set_point(25, -90, classes=["given"], label="A")
    B = model.set_point(135, -90, classes=["given"], label="B")
    Y = model.set_point(45, -47.6, classes=["given"], label="Y")
    X = model.set_point(107, -42.1, classes=["given"], label="X")
    Cp_pt = model.set_point(196, -90, classes=["given"], label="C'")

    # Circles C and C' and line of centres
    model.construct_circle(O, A)
    model.construct_circle(Op, Cp_pt)
    model.construct_line(A, B)

    # Segments and sections
    model.set_segment(A, O)
    model.set_segment(O, Op)
    model.set_segment(Op, B)
    model.set_segment(A, Op)
    model.set_segment(O, B)
    model.set_segment(A, B)
    model.set_segment(O, Y)
    model.set_segment(Op, Y)
    model.set_section([A, O, Op])
    model.set_section([O, Op, B])
    model.set_section([A, O, B])

    # Triangle OO'Y
    model.set_polygon([O, Op, Y])

    return model


if __name__ == "__main__":
    construct_0252_g1()
