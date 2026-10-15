"""Programmatic construction for Book I, Common Notions commentary (0252.g2).

Intersections of two circles, Lemma Case 2: Point A lies on OO'.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0252_g2() -> Model:
    """Construct the figure for 0252.g2 using geometor.model."""
    model = Model("0252.g2")

    # Centres O, O' and points B, A, X, Y on circle C
    O = model.set_point(100, -118, classes=["given"], label="O")
    Op = model.set_point(202, -118, classes=["given"], label="O'")
    B = model.set_point(45, -118, classes=["given"], label="B")
    A = model.set_point(155, -118, classes=["given"], label="A")
    X = model.set_point(146, -88, classes=["given"], label="X")
    Y = model.set_point(76, -68.5, classes=["given"], label="Y")
    Cp_pt = model.set_point(277, -118, classes=["given"], label="C'")

    # Circles C and C' and line of centres
    model.construct_circle(O, A)
    model.construct_circle(Op, Cp_pt)
    model.construct_line(B, Op)

    # Segments and sections
    model.set_segment(B, O)
    model.set_segment(O, A)
    model.set_segment(A, Op)
    model.set_segment(O, Op)
    model.set_segment(B, A)
    model.set_segment(B, Op)
    model.set_segment(O, X)
    model.set_segment(Op, X)
    model.set_section([B, O, A])
    model.set_section([O, A, Op])

    # Triangle OO'X
    model.set_polygon([O, Op, X])

    return model


if __name__ == "__main__":
    construct_0252_g2()
