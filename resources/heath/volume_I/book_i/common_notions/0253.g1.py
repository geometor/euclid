"""Programmatic construction for Book I, Common Notions commentary (0253.g1).

Intersections of two circles, Lemma Case 3: Point A lies on OO' produced.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0253_g1() -> Model:
    """Construct the figure for 0253.g1 using geometor.model."""
    model = Model("0253.g1")

    # Centres O, O' and points B, A, X, Y on circle C
    O = model.set_point(85, -120, classes=["given"], label="O")
    Op = model.set_point(125, -120, classes=["given"], label="O'")
    B = model.set_point(30, -120, classes=["given"], label="B")
    A = model.set_point(140, -120, classes=["given"], label="A")
    X = model.set_point(117, -75.3, classes=["given"], label="X")
    Y = model.set_point(33, -102, classes=["given"], label="Y")
    Cp_pt = model.set_point(203, -120, classes=["given"], label="C'")

    # Circles C and C' and line of centres
    model.construct_circle(O, A)
    model.construct_circle(Op, Cp_pt)
    model.construct_line(B, A)

    # Segments and sections
    model.set_segment(B, O)
    model.set_segment(O, Op)
    model.set_segment(Op, A)
    model.set_segment(O, A)
    model.set_segment(B, Op)
    model.set_segment(B, A)
    model.set_segment(O, X)
    model.set_segment(Op, X)
    model.set_section([B, O, A])
    model.set_section([O, Op, A])

    # Triangle OO'X
    model.set_polygon([O, Op, X])

    return model


if __name__ == "__main__":
    construct_0253_g1()
