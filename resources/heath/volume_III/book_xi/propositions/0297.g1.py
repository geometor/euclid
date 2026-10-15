"""Programmatic construction for Book XI, Proposition 11 Alternative Method (0297.g1).

Construction of a perpendicular to a given plane MN from a point A either
outside the plane (first figure) or in the plane (second figure).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0297_g1() -> Model:
    """Construct the figure for Book XI, Proposition 11 (Alternative Method) using geometor.model."""
    model = Model("0297.g1")

    # First figure (point A outside the plane MN)
    A = model.set_point(0, 1, classes=["given"], label="A")
    H = model.set_point(0, 0, label="H")
    F = model.set_point(sp.Rational(-52, 73), 0, label="F")
    D = model.set_point(sp.Rational(61, 73), 0, label="D")
    G = model.set_point(sp.Rational(100, 73), 0, label="G")
    E = model.set_point(sp.Rational(25, 73), sp.Rational(61, 73), label="E")

    B = model.set_point(sp.Rational(44, 73), sp.Rational(-23, 73), label="B")
    C = model.set_point(sp.Rational(78, 73), sp.Rational(29, 73), label="C")
    K = model.set_point(sp.Rational(-13, 73), sp.Rational(-21, 73), label="K")
    L = model.set_point(sp.Rational(18, 73), sp.Rational(28, 73), label="L")

    M = model.set_point(sp.Rational(-96, 73), sp.Rational(-33, 73), label="M")
    N = model.set_point(sp.Rational(156, 73), sp.Rational(46, 73), label="N")

    # Collinear sections and segments
    model.construct_line(F, G)
    model.set_section([F, H, D])
    model.set_section([H, D, G])
    model.set_segment(F, H)
    model.set_segment(H, D)
    model.set_segment(D, G)
    model.set_segment(F, D)
    model.set_segment(F, G)

    model.construct_line(B, C)
    model.set_section([B, D, C])
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(B, C)

    model.construct_line(K, L)
    model.set_section([K, H, L])
    model.set_segment(K, H)
    model.set_segment(H, L)
    model.set_segment(K, L)

    model.set_segment(A, H)
    model.set_segment(A, D)
    model.set_segment(D, E)

    # Planes AG and MN
    model.set_polygon([A, D, E])
    model.set_polygon([F, G, D, H])

    return model


if __name__ == "__main__":
    construct_0297_g1()
