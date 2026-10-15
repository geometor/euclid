"""Programmatic construction for Book I, Common Notions commentary (0251.g1).

Dedekind's Postulate applied to the intersections of a straight line r with a circle C.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0251_g1() -> Model:
    """Construct the figure for 0251.g1 using geometor.model."""
    model = Model("0251.g1")

    # Circle center O and points on line r
    O = model.set_point(109, -84, classes=["given"], label="O")
    P = model.set_point(109, -39, classes=["given"], label="P")
    A = model.set_point(128, -39, classes=["given"], label="A")
    M = model.set_point(144, -39, classes=["given"], label="M")
    Mp = model.set_point(153, -39, classes=["given"], label="M'")
    R_pt = model.set_point(155.9, -39, classes=["given"], label="R")
    B = model.set_point(205, -39, classes=["given"], label="B")

    # Circle C and straight line r
    model.construct_circle(O, R_pt)
    model.construct_line(P, B)
    model.construct_line(O, P)

    # Perpendicular OP and obliques OA, OM, OM', OB
    model.set_segment(O, P)
    model.set_segment(O, A)
    model.set_segment(O, M)
    model.set_segment(O, Mp)
    model.set_segment(O, B)

    # Collinear segments on straight line r
    model.set_segment(P, A)
    model.set_segment(A, M)
    model.set_segment(M, Mp)
    model.set_segment(Mp, B)
    model.set_segment(A, B)
    model.set_segment(P, B)
    model.set_segment(P, M)

    # Sections on r
    model.set_section([P, A, B])
    model.set_section([P, M, B])
    model.set_section([P, M, Mp])

    # Polygons
    model.set_polygon([O, P, A])
    model.set_polygon([O, P, M])
    model.set_polygon([O, M, Mp])
    model.set_polygon([O, P, B])

    # Right angle at P
    model.set_wedge(P, O, O, B)

    return model


if __name__ == "__main__":
    construct_0251_g1()
