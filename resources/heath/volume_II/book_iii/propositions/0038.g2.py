"""Programmatic construction for Book III, Proposition 12 Commentary 5 Case 3 (0038.g2).

Two intersecting circles where OO' < r, so O' lies between O and L.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0038_g2() -> Model:
    """Construct the figure 0038.g2 using geometor.model."""
    model = Model("0038.g2")

    # Centres O and O' and diameter endpoints M and L of circle O
    O = model.set_point(0, 0, classes=["given"], label="O")
    O_prime = model.set_point(22, 0, classes=["given"], label="O'")
    M = model.set_point(-59, 0, label="M")
    L = model.set_point(59, 0, label="L")

    # Circles O and O'
    model.construct_circle(O, L)
    P_prime = model.set_point(-46, 0, classes=["auxiliary"])
    model.construct_circle(O_prime, P_prime)

    # Line of centres [ M L ]
    model.construct_line(M, L)

    # Intersections A and B of the two circles
    x_int = sp.Rational(-659, 44)
    y_int = sp.sqrt(59**2 - x_int**2)
    A = model.set_point(x_int, y_int, label="A")
    B = model.set_point(x_int, -y_int, label="B")

    # Segments
    model.set_segment(M, O)
    model.set_segment(O, O_prime)
    model.set_segment(O_prime, L)
    model.set_segment(O, L)
    model.set_segment(M, O_prime)
    model.set_segment(M, L)
    model.set_segment(A, B)

    return model


if __name__ == "__main__":
    construct_0038_g2()
