"""Programmatic construction for Book II, Proposition 10 — Pappus's theorem Case I (0415.g2).

Sum of the squares on two sides of a triangle equals twice the square on half
the base together with twice the square on the median (altitude inside base).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0415_g2() -> Model:
    """Construct figure 0415.g2 for Pappus's median theorem (Case I)."""
    model = Model("0415.g2")

    # Base BC with midpoint D and altitude foot E between D and C
    B = model.set_point(0, 0, classes=["given"], label="B")
    D = model.set_point(3, 0, label="D")
    E = model.set_point(sp.Rational(9, 2), 0, label="E")
    C = model.set_point(6, 0, classes=["given"], label="C")
    A = model.set_point(sp.Rational(9, 2), 4, classes=["given"], label="A")

    # Segments
    model.set_segment(B, D)
    model.set_segment(D, E)
    model.set_segment(E, C)
    model.set_segment(B, E)
    model.set_segment(D, C)
    model.set_segment(B, C)
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(A, E)
    model.set_segment(A, C)

    # Triangles
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, E])
    model.set_polygon([A, D, E])
    model.set_polygon([A, E, C])

    return model


if __name__ == "__main__":
    construct_0415_g2()
