"""Programmatic construction for Book III, Proposition 11 Note (0032.g2).

Hypothesis (b) in Camerer/Heath's commentary on Book III, Proposition 11:
point of contact A lies outside the line of centres FG produced, and FG
produced meets the outer circle at H and the inner circle at D (with GD > GH),
cutting the outer circle at X between A and D.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0032_g2() -> Model:
    """Construct the figure 0032.g2 using geometor.model."""
    model = Model("0032.g2")

    # Outer circle with centre F(0, 0) and point of contact A(1, 0)
    F = model.set_point(0, 0, classes=["given"], label="F")
    A = model.set_point(1, 0, classes=["given"], label="A")
    model.construct_circle(F, A)

    # Line of centres F-G-H-D along direction (15/17, 8/17)
    ux, uy = sp.Rational(15, 17), sp.Rational(8, 17)
    G = model.set_point(sp.Rational(9, 20) * ux, sp.Rational(9, 20) * uy, classes=["given"], label="G")
    H = model.set_point(ux, uy, label="H")
    D = model.set_point(sp.Rational(6, 5) * ux, sp.Rational(6, 5) * uy, label="D")
    model.construct_line(F, D)

    # Point X on outer circle between H and A, and symmetric point Y across FD
    X = model.set_point(sp.Rational(24, 25), sp.Rational(7, 25), label="X")
    dot_X = X.x * ux + X.y * uy
    Y = model.set_point(2 * dot_X * ux - X.x, 2 * dot_X * uy - X.y, label="Y")

    # Collinear segments along F-G-H-D
    model.set_segment(F, G)
    model.set_segment(G, H)
    model.set_segment(H, D)
    model.set_segment(G, D)
    model.set_segment(F, H)
    model.set_segment(F, D)

    # Segments to A, X, Y
    model.set_segment(F, A)
    model.set_segment(G, A)
    model.set_segment(F, X)
    model.set_segment(G, X)
    model.set_segment(F, Y)
    model.set_segment(G, Y)

    return model


if __name__ == "__main__":
    construct_0032_g2()
