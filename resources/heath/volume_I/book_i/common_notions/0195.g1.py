"""Programmatic construction for Book I, Definitions Commentary (0195.g1).

Veronese's definition of an angle as a part of a cluster of rays bounded by two
rays (left sub-figure: vertex V with bounding rays Va, Vb and internal rays),
and of a flat angle whose bounding rays VA, VB are opposite (right sub-figure:
line AB with vertex V, ray VC, and semicircular cluster of rays).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0195_g1() -> Model:
    """Construct Veronese's angle and flat angle diagram (0195.g1)."""
    model = Model("0195.g1")

    # 1. Left sub-figure: Angle < a O b ) with vertex O (labeled V in diagram) and sides a, b
    O = model.set_point(64, 110, classes=["given"], label="O")
    a = model.set_point(38, 16, classes=["given"], label="a")
    b = model.set_point(90, 16, classes=["given"], label="b")

    model.construct_line(O, a)
    model.construct_line(O, b)
    model.set_segment(O, a)
    model.set_segment(O, b)
    model.set_polygon([O, a, b])
    model.set_wedge(O, a, a, b)

    # 2. Right sub-figure: Flat angle < A V B ) with opposite rays VA, VB and ray VC
    V = model.set_point(241, 106, classes=["given"], label="V")
    A = model.set_point(145, 106, classes=["given"], label="A")
    B = model.set_point(338, 106, classes=["given"], label="B")
    C = model.set_point(288, 188, classes=["given"], label="C")

    model.construct_line(A, B)
    model.construct_line(V, C)

    model.set_section([A, V, B])
    model.set_segment(A, V)
    model.set_segment(V, B)
    model.set_segment(A, B)
    model.set_segment(V, C)

    model.set_wedge(V, B, B, C)
    model.set_wedge(V, A, C, A)
    model.set_wedge(V, B, B, A)

    return model


if __name__ == "__main__":
    construct_0195_g1()
