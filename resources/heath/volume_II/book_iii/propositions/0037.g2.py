"""Programmatic construction for Book III, Proposition 12 Commentary 5 Case 1 (0037.g2).

Two intersecting circles where r' - r < OO' < r + r' and OO' >= r'.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0037_g2() -> Model:
    """Construct the figure 0037.g2 using geometor.model."""
    model = Model("0037.g2")

    # Centres O and O'
    O = model.set_point(0, 0, classes=["given"], label="O")
    O_prime = model.set_point(93, 0, classes=["given"], label="O'")

    # Extremities M and L of diameter ML of circle O along line of centres
    M = model.set_point(-61, 0, label="M")
    L = model.set_point(61, 0, label="L")

    # Circles O and O'
    model.construct_circle(O, L)
    P_prime = model.set_point(24, 0, classes=["auxiliary"])
    model.construct_circle(O_prime, P_prime)

    # Line through centres [ O' M ]
    model.construct_line(O_prime, M)

    # Intersections A and B of the two circles
    x_int = sp.Rational(7609, 186)
    y_int = sp.sqrt(61**2 - x_int**2)
    A = model.set_point(x_int, y_int, label="A")
    B = model.set_point(x_int, -y_int, label="B")

    # Segments
    model.set_segment(M, O)
    model.set_segment(O, L)
    model.set_segment(L, O_prime)
    model.set_segment(O, O_prime)
    model.set_segment(M, L)
    model.set_segment(M, O_prime)
    model.set_segment(A, B)

    return model


if __name__ == "__main__":
    construct_0037_g2()
