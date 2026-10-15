"""Programmatic construction for Book III, Proposition 12 Commentary 5 Case 2 (0038.g1).

Two intersecting circles where OO' = r, so the circumference of circle O
passes through O' (L coincides with O').
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0038_g1() -> Model:
    """Construct the figure 0038.g1 using geometor.model."""
    model = Model("0038.g1")

    # Centres O and O' (where L coincides with O' at distance r = 58)
    O = model.set_point(0, 0, classes=["given"], label="O")
    O_prime = model.set_point(58, 0, classes=["given"], label="O'")
    L = model.set_point(58, 0, label="L")
    M = model.set_point(-58, 0, label="M")

    # Circles O and O'
    model.construct_circle(O, L)
    P_prime = model.set_point(-9, 0, classes=["auxiliary"])
    model.construct_circle(O_prime, P_prime)

    # Line of centres [ M O' ]
    model.construct_line(M, O_prime)

    # Intersections A and B of the two circles
    x_int = sp.Rational(2239, 116)
    y_int = sp.sqrt(58**2 - x_int**2)
    A = model.set_point(x_int, y_int, label="A")
    B = model.set_point(x_int, -y_int, label="B")

    # Segments
    model.set_segment(M, O)
    model.set_segment(O, O_prime)
    model.set_segment(M, O_prime)
    model.set_segment(A, B)

    return model


if __name__ == "__main__":
    construct_0038_g1()
