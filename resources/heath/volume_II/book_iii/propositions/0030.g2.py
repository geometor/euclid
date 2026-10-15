"""Programmatic construction for Book III, Proposition 11 (0030.g2).

If two circles ABC, ADE touch one another internally at A, and their centres F
and G be taken, the straight line joining their centres and produced will fall
on the point of contact A (reductio ad absurdum via line FGH).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0030_g2() -> Model:
    """Construct the figure 0030.g2 for Book III, Proposition 11."""
    model = Model("0030.g2")

    # Outer circle ABC with centre F at origin and radius 1
    F = model.set_point(0, 0, classes=["given"], label="F")
    H = model.set_point(0, 1, label="H")
    B = model.set_point(1, 0, label="B")
    C = model.set_point(sp.Rational(-1, 3), -sp.Rational(2, 3) * sp.sqrt(2), label="C")
    model.construct_circle(F, H)

    # Point of internal contact A on the upper-left circumference
    A = model.set_point(sp.Rational(-4, 5), sp.Rational(3, 5), classes=["given"], label="A")

    # Inner circle ADE touching ABC internally at A, with radius 5/7
    r_in = sp.Rational(5, 7)
    C_in = model.set_point((1 - r_in) * A.x, (1 - r_in) * A.y)
    model.construct_circle(C_in, A)

    # Hypothetical centre G on vertical line FH, and intersection D of FH with ADE
    G = model.set_point(0, sp.Rational(16, 49), classes=["given"], label="G")
    model.construct_line(F, H)
    y_D = C_in.y + sp.sqrt(r_in**2 - C_in.x**2)
    D = model.set_point(0, y_D, label="D")
    E = model.set_point(C_in.x, C_in.y - r_in, label="E")

    # Collinear segments along F-G-D-H
    model.set_segment(F, G)
    model.set_segment(G, D)
    model.set_segment(D, H)
    model.set_segment(F, D)
    model.set_segment(G, H)
    model.set_segment(F, H)
    model.set_section([F, G, D])
    model.set_section([G, D, H])
    model.set_section([F, G, H])

    # Radii AF and AG, and triangle AFG
    model.set_segment(A, F)
    model.set_segment(A, G)
    model.set_polygon([A, F, G])

    return model


if __name__ == "__main__":
    construct_0030_g2()
