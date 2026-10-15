"""Programmatic construction for Book I, Definitions Commentary (0189.g1).

Bolyai and Lobachewsky's proof of Simson's plane property from the congruence
theorems: AB is perpendicular at its midpoint C to two plane generators CM, CN,
and P is any point on the straight line MN.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0189_g1() -> Model:
    """Construct the Bolyai-Lobachewsky plane generator diagram (0189.g1)."""
    model = Model("0189.g1")

    # 1. Axis AB with midpoint C
    C = model.set_point(0, 0, classes=["given"], label="C")
    A = model.set_point(0, 83, classes=["given"], label="A")
    B = model.set_point(0, -83, classes=["given"], label="B")

    model.construct_line(A, B)
    model.set_section([A, C, B])
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(A, B)

    # 2. Generators CM, CN and point P on the straight line MN
    N = model.set_point(147, 23, classes=["given"], label="N")
    M = model.set_point(109, -39, classes=["given"], label="M")
    t_P = sp.Rational(9, 19)
    P = model.set_point(
        M.x + t_P * (N.x - M.x),
        M.y + t_P * (N.y - M.y),
        label="P",
    )

    model.construct_line(M, N)
    model.set_section([M, P, N])
    model.set_segment(M, P)
    model.set_segment(P, N)
    model.set_segment(M, N)

    # 3. Generators from C and edges from A and B to M, P, N
    for pt in (M, P, N):
        model.set_segment(C, pt)
        model.set_segment(A, pt)
        model.set_segment(B, pt)

    # 4. Five pairs of congruent triangles compared in the proof
    model.set_polygon([A, C, M])
    model.set_polygon([B, C, M])
    model.set_polygon([A, C, N])
    model.set_polygon([B, C, N])
    model.set_polygon([A, M, N])
    model.set_polygon([B, M, N])
    model.set_polygon([A, M, P])
    model.set_polygon([B, M, P])
    model.set_polygon([A, C, P])
    model.set_polygon([B, C, P])

    return model


if __name__ == "__main__":
    construct_0189_g1()
