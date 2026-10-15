"""Programmatic construction for Book I, Definitions Commentary (0187.g1).

Crelle and Frankland's illustration on Simson's definition of a plane:
In a triangle ABC, if AD joins vertex A to a point D on BC, and BE joins
vertex B to a point E on CA, then AD and BE must intersect at a point F.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0187_g1() -> Model:
    """Construct the triangle cevian intersection diagram (0187.g1)."""
    model = Model("0187.g1")

    # 1. Suppose a plane in which lies the triangle ABC.
    B = model.set_point(0, 0, classes=["given"], label="B")
    C = model.set_point(106, 0, classes=["given"], label="C")
    A = model.set_point(sp.Rational(417, 10), 51, classes=["given"], label="A")

    line_BC = model.construct_line(B, C)
    line_CA = model.construct_line(C, A)
    line_AB = model.construct_line(A, B)

    model.set_polygon([A, B, C])
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)

    # 2. Let AD join vertex A to any point D on BC, and BE join vertex B to any point E on CA.
    D = model.set_point(30, 0, classes=["given"], label="D")
    t_E = sp.Rational(11, 40)
    E = model.set_point(
        A.x + t_E * (C.x - A.x),
        A.y + t_E * (C.y - A.y),
        classes=["given"],
        label="E",
    )

    line_AD = model.construct_line(A, D)
    line_BE = model.construct_line(B, E)

    # 3. AD, BE must intersect, say at F.
    # Intersection of line AD and line BE:
    s_F = sp.Rational(1917, 3383)
    F = model.set_point(
        A.x + s_F * (D.x - A.x),
        A.y + s_F * (D.y - A.y),
        label="F",
    )

    # Collinear sections and sub-segments
    model.set_section([B, D, C])
    model.set_segment(B, D)
    model.set_segment(D, C)

    model.set_section([C, E, A])
    model.set_segment(C, E)
    model.set_segment(E, A)

    model.set_section([A, F, D])
    model.set_segment(A, F)
    model.set_segment(F, D)
    model.set_segment(A, D)

    model.set_section([B, F, E])
    model.set_segment(B, F)
    model.set_segment(F, E)
    model.set_segment(B, E)

    # Sub-polygons formed by the cevians
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([B, C, E])
    model.set_polygon([B, A, E])
    model.set_polygon([A, B, F])

    return model


if __name__ == "__main__":
    construct_0187_g1()
