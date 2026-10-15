"""Programmatic construction for Book I, Common Notions commentary (0253.g2).

Intersections of two circles, Proof of Theorem via Dedekind's Postulate.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0253_g2() -> Model:
    """Construct the figure for 0253.g2 using geometor.model."""
    model = Model("0253.g2")

    # Centres O, O', diameter endpoints B, A of C, points P, Q, M, M' on semicircle APQB
    O = model.set_point(105, -106, classes=["given"], label="O")
    Op = model.set_point(228, -106, classes=["given"], label="O'")
    B = model.set_point(27, -106, classes=["given"], label="B")
    A = model.set_point(183, -106, classes=["given"], label="A")
    P = model.set_point(135, -34, classes=["given"], label="P")
    Q = model.set_point(81, -31.8, classes=["given"], label="Q")
    M = model.set_point(171.6, -65.5, classes=["given"], label="M")
    Mp = model.set_point(160, -50.8, classes=["given"], label="M'")
    Cp_pt = model.set_point(293, -106, classes=["given"], label="C'")

    # Circles C and C' and line of centres
    model.construct_circle(O, A)
    model.construct_circle(Op, Cp_pt)
    model.construct_line(B, Cp_pt)

    # Segments
    model.set_segment(B, O)
    model.set_segment(O, A)
    model.set_segment(A, Op)
    model.set_segment(O, Op)
    model.set_segment(B, A)
    model.set_segment(O, P)
    model.set_segment(O, Q)
    model.set_segment(Op, P)
    model.set_segment(Op, Q)
    model.set_segment(Op, M)
    model.set_segment(Op, Mp)
    model.set_segment(M, Mp)
    model.set_section([B, O, A])
    model.set_section([O, A, Op])

    # Polygons
    model.set_polygon([O, Op, P])
    model.set_polygon([O, Op, Q])
    model.set_polygon([Op, M, Mp])

    # Angles and Semicircle Arc
    model.set_wedge(O, Op, Op, P)
    model.set_wedge(O, Op, Op, Q)
    model.set_wedge(O, A, A, B)

    return model


if __name__ == "__main__":
    construct_0253_g2()
