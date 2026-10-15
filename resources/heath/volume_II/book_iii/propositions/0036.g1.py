"""Programmatic construction for Book III, Proposition 12 Commentary 1 (0036.g1).

Two circles external to one another where OO' > r + r'.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0036_g1() -> Model:
    """Construct the figure 0036.g1 using geometor.model."""
    model = Model("0036.g1")

    # Centres O and O'
    O = model.set_point(0, 0, classes=["given"], label="O")
    O_prime = model.set_point(150, 0, classes=["given"], label="O'")

    # Radii points A on circle O and A' on circle O'
    A = model.set_point(64, 0, label="A")
    A_prime = model.set_point(102, 0, classes=["auxiliary"], label="A'")

    # Circles O and O'
    model.construct_circle(O, A)
    model.construct_circle(O_prime, A_prime)

    # Line of centres [ O O' ]
    model.construct_line(O, O_prime)

    # Point B on circumference of circle O and point C internal to circle O
    B = model.set_point(50, -39, label="B")
    C = model.set_point(-16, 30, label="C")
    D = model.set_point(62, 16, label="D")

    # Segments
    model.set_segment(O, A)
    model.set_segment(A, A_prime)
    model.set_segment(A_prime, O_prime)
    model.set_segment(A, O_prime)
    model.set_segment(O, O_prime)
    model.set_segment(O_prime, B)
    model.set_segment(O, C)
    model.set_segment(O_prime, C)
    model.set_segment(C, D)
    model.set_segment(D, O_prime)
    model.set_polygon([O, C, O_prime])

    return model


if __name__ == "__main__":
    construct_0036_g1()
