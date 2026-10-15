"""Programmatic construction for Book III, Proposition 12 Commentary 2 (0036.g2).

Two circles where OO' < r' - r and the lesser circle O is entirely within the greater O'.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0036_g2() -> Model:
    """Construct the figure 0036.g2 using geometor.model."""
    model = Model("0036.g2")

    # Centres O (inner) and O' (outer)
    O = model.set_point(0, 0, classes=["given"], label="O")
    O_prime = model.set_point(21, 0, classes=["given"], label="O'")

    # Intersections A and A' of ray O'O with circles O and O'
    A = model.set_point(-31, 0, label="A")
    A_prime = model.set_point(-52, 0, label="A'")

    # Circles O and O'
    model.construct_circle(O, A)
    model.construct_circle(O_prime, A_prime)

    # Line through centres [ O' A' ]
    model.construct_line(O_prime, A_prime)

    # Collinear segments along A'-A-O-O'
    model.set_segment(A_prime, A)
    model.set_segment(A, O)
    model.set_segment(O, O_prime)
    model.set_segment(A, O_prime)
    model.set_segment(A_prime, O)
    model.set_segment(A_prime, O_prime)
    model.set_section([A_prime, A, O_prime])
    model.set_section([A, O, O_prime])

    return model


if __name__ == "__main__":
    construct_0036_g2()
