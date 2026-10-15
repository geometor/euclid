"""Programmatic construction for Book XI, Proposition 8 (Legendre's Alternative, 0293.g1).

(1) Let AB be a perpendicular to the plane MN and EF a line situated in that
plane; if from B, the foot of the perpendicular, BD be drawn perpendicular to
EF, and AD be joined, AD will be perpendicular to EF.
(2) If AB is perpendicular to the plane MN, every straight line CD parallel to
AB will be perpendicular to the same plane.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0293_g1() -> Model:
    """Construct the figure for Book XI, Proposition 8 (Legendre's Alternative) using geometor.model."""
    model = Model("0293.g1")

    # Plane MN boundary corners
    M = model.set_point(sp.Rational(-28, 64), sp.Rational(21, 64), label="M")
    P2 = model.set_point(sp.Rational(137, 64), sp.Rational(21, 64), label="P2")
    N = model.set_point(sp.Rational(123, 64), sp.Rational(-64, 64), label="N")
    P4 = model.set_point(sp.Rational(-42, 64), sp.Rational(-64, 64), label="P4")

    # 1. Let AB be perpendicular to the plane MN and CD parallel to AB.
    B = model.set_point(0, 0, classes=["given"], label="B")
    A = model.set_point(0, 1, classes=["given"], label="A")
    D = model.set_point(sp.Rational(91, 64), sp.Rational(-31, 64), classes=["given"], label="D")
    C = model.set_point(sp.Rational(91, 64), sp.Rational(62, 64), classes=["given"], label="C")

    # 2. Draw EF perpendicular to BD in the plane MN, with DE = DF.
    E = model.set_point(sp.Rational(72, 64), sp.Rational(-57, 64), label="E")
    F = model.set_point(sp.Rational(107, 64), sp.Rational(-5, 64), label="F")

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

    # Plane MN boundary
    model.set_segment(M, P2)
    model.set_segment(P2, N)
    model.set_segment(N, P4)
    model.set_segment(P4, M)
    model.set_polygon([M, P2, N, P4])

    # Triangles and planes in the proof
    model.set_polygon([B, D, E])
    model.set_polygon([B, D, F])
    model.set_polygon([A, B, E])
    model.set_polygon([A, B, F])
    model.set_polygon([A, D, E])
    model.set_polygon([A, D, F])
    model.set_polygon([A, D, B])

    return model


if __name__ == "__main__":
    construct_0293_g1()
