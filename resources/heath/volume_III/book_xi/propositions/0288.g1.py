"""Programmatic construction for Book XI, Proposition 6 (Legendre's Proof, 0288.g1).

Let AB, CD be both perpendicular to the same plane MN. Through D draw EDF, in
the plane MN, at right angles to BD, and make ED equal to DF.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0288_g1() -> Model:
    """Construct the figure for Book XI, Proposition 6 (Legendre's Proof) using geometor.model."""
    model = Model("0288.g1")

    # Plane MN boundary corners
    M = model.set_point(sp.Rational(-27, 81), sp.Rational(27, 81), label="M")
    P2 = model.set_point(sp.Rational(142, 81), sp.Rational(27, 81), label="P2")
    N = model.set_point(sp.Rational(129, 81), sp.Rational(-62, 81), label="N")
    P4 = model.set_point(sp.Rational(-42, 81), sp.Rational(-62, 81), label="P4")

    # 1. Let AB, CD be both perpendicular to the same plane MN.
    B = model.set_point(0, 0, classes=["given"], label="B")
    A = model.set_point(0, 1, classes=["given"], label="A")
    D = model.set_point(sp.Rational(86, 81), sp.Rational(-27, 81), classes=["given"], label="D")
    C = model.set_point(sp.Rational(86, 81), sp.Rational(84, 81), classes=["given"], label="C")

    # 2. Through D draw EDF in the plane MN at right angles to BD, with ED = DF.
    E = model.set_point(sp.Rational(65, 81), sp.Rational(-52, 81), label="E")
    F = model.set_point(sp.Rational(105, 81), 0, label="F")

    # Collinear line EDF
    model.construct_line(E, F)
    model.set_section([E, D, F])
    model.set_segment(E, D)
    model.set_segment(D, F)
    model.set_segment(E, F)

    # Segments
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(B, D)
    model.set_segment(B, E)
    model.set_segment(B, F)
    model.set_segment(A, E)
    model.set_segment(A, D)
    model.set_segment(A, F)
    model.set_segment(C, E)
    model.set_segment(C, F)

    # Plane MN boundary
    model.set_segment(M, P2)
    model.set_segment(P2, N)
    model.set_segment(N, P4)
    model.set_segment(P4, M)
    model.set_polygon([M, P2, N, P4])

    # Triangles compared in the proof
    model.set_polygon([B, D, E])
    model.set_polygon([B, D, F])
    model.set_polygon([A, B, E])
    model.set_polygon([A, B, F])
    model.set_polygon([A, E, D])
    model.set_polygon([A, F, D])
    model.set_polygon([A, B, D])

    return model


if __name__ == "__main__":
    construct_0288_g1()
