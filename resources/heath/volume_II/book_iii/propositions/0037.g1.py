"""Programmatic construction for Book III, Proposition 12 Commentary 3 (0037.g1).

Two circles touching externally where OO' = r + r'.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0037_g1() -> Model:
    """Construct the figure 0037.g1 using geometor.model."""
    model = Model("0037.g1")

    # Centres O and O' and point of contact A
    O = model.set_point(0, 0, classes=["given"], label="O")
    A = model.set_point(48, 0, label="A")
    O_prime = model.set_point(112, 0, classes=["given"], label="O'")

    # Circles O and O' touching externally at A
    model.construct_circle(O, A)
    model.construct_circle(O_prime, A)

    # Line of centres [ O O' ]
    model.construct_line(O, O_prime)

    # Point B on circle O and point C internal to circle O
    B = model.set_point(35, -33, label="B")
    C = model.set_point(-8, 28, label="C")
    D = model.set_point(45, 16, label="D")

    # Segments
    model.set_segment(O, A)
    model.set_segment(A, O_prime)
    model.set_segment(O, O_prime)
    model.set_segment(O_prime, B)
    model.set_segment(O, C)
    model.set_segment(C, D)
    model.set_segment(D, O_prime)
    model.set_segment(O_prime, C)
    model.set_polygon([O, C, O_prime])

    return model


if __name__ == "__main__":
    construct_0037_g1()
