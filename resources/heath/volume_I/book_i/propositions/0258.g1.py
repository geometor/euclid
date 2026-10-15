"""Programmatic construction for Book I, Proposition 2 (0258.g1).

To place at a given point (as an extremity) a straight line equal to a given straight line.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0258_g1() -> Model:
    """Construct the figure for Book I, Proposition 2 using geometor.model."""
    model = Model("0258.g1")

    # 1. Let A be the given point, and BC the given straight line.
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(1, 0, classes=["given"], label="B")
    C = model.set_point(sp.Rational(3, 2), sp.sqrt(3), classes=["given"], label="C")
    model.set_segment(B, C)

    # 2. From A to B let the straight line AB be joined [Post. 1]
    model.set_segment(A, B)

    # 3. On AB let the equilateral triangle DAB be constructed [I. 1]
    D = model.set_point(sp.Rational(1, 2), sp.sqrt(3) / 2, label="D")
    model.set_segment(D, A)
    model.set_segment(D, B)
    model.set_polygon([D, A, B])

    # 4. Let the straight lines AE, BF be produced in a straight line with DA, DB [Post. 2]
    model.construct_line(D, A)
    model.construct_line(D, B)

    # 5. With centre B and distance BC let the circle CGH be described [Post. 3]
    model.construct_circle(B, C)

    # Distance BC = sqrt((3/2 - 1)^2 + (sqrt(3))^2) = sqrt(1/4 + 3) = sqrt(13)/2
    r_BC = sp.sqrt(13) / 2
    # Unit direction along DB (from D(1/2, sqrt(3)/2) through B(1, 0)): (1/2, -sqrt(3)/2)
    G = model.set_point(
        B.x + r_BC * sp.Rational(1, 2),
        B.y - r_BC * sp.sqrt(3) / 2,
        label="G",
    )
    H = model.set_point(B.x - r_BC, B.y, label="H")

    # 6. With centre D and distance DG let the circle GKL be described [Post. 3]
    model.construct_circle(D, G)
    r_DG = 1 + r_BC

    # Unit direction along DA (from D(1/2, sqrt(3)/2) through A(0, 0)): (-1/2, -sqrt(3)/2)
    L = model.set_point(
        D.x - r_DG * sp.Rational(1, 2),
        D.y - r_DG * sp.sqrt(3) / 2,
        label="L",
    )
    K = model.set_point(D.x - r_DG, D.y, label="K")

    # Ray endpoints E (beyond L on DA produced) and F (beyond G on DB produced)
    r_DE = r_DG + sp.Rational(1, 2)
    E = model.set_point(
        D.x - r_DE * sp.Rational(1, 2),
        D.y - r_DE * sp.sqrt(3) / 2,
        label="E",
    )
    F = model.set_point(
        D.x + r_DE * sp.Rational(1, 2),
        D.y - r_DE * sp.sqrt(3) / 2,
        label="F",
    )

    # 7. Collinear sections and referenced segments
    model.set_section([D, A, L])
    model.set_section([D, B, G])

    model.set_segment(A, L)
    model.set_segment(B, G)
    model.set_segment(D, L)
    model.set_segment(D, G)
    model.set_segment(A, E)
    model.set_segment(B, F)

    return model


if __name__ == "__main__":
    construct_0258_g1()
