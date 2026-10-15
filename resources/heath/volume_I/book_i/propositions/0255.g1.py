"""Programmatic construction for Book I, Proposition 1 (0255.g1).

On a given finite straight line to construct an equilateral triangle.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0255_g1() -> Model:
    """Construct the figure for Book I, Proposition 1 using geometor.model."""
    model = Model("0255.g1")

    # 1. Let AB be the given finite straight line.
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(1, 0, classes=["given"], label="B")
    model.set_segment(A, B)

    # Extended horizontal line [ A B ] to determine circumference points D and E
    model.construct_line(A, B)

    # 2. With centre A and distance AB let the circle BCD be described [Post. 3]
    circle_BCD = model.construct_circle(A, B)

    # 3. With centre B and distance BA let the circle ACE be described [Post. 3]
    circle_ACE = model.construct_circle(B, A)

    # Label the upper intersection of circles ( A B ) and ( B A ) as C,
    # and the outer diameter intersections on [ A B ] as D and E.
    C = model.set_point(sp.Rational(1, 2), sp.sqrt(3) / 2, label="C")
    D = model.set_point(-1, 0, label="D")
    E = model.set_point(2, 0, label="E")

    # 4. From C to A, B let the straight lines CA, CB be joined [Post. 1]
    model.set_segment(C, A)
    model.set_segment(C, B)

    # 5. Therefore the triangle ABC is equilateral
    model.set_polygon([A, B, C])

    return model


if __name__ == "__main__":
    construct_0255_g1()
