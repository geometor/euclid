"""Programmatic construction for Book II, Proposition 10 — Pappus's theorem Case II (0415.g3).

Sum of the squares on two sides of a triangle equals twice the square on half
the base together with twice the square on the median (altitude on base produced).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0415_g3() -> Model:
    """Construct figure 0415.g3 for Pappus's median theorem (Case II)."""
    model = Model("0415.g3")

    # Base BC with midpoint D, and BC produced to altitude foot E
    B = model.set_point(0, 0, classes=["given"], label="B")
    D = model.set_point(3, 0, label="D")
    C = model.set_point(6, 0, classes=["given"], label="C")
    E = model.set_point(sp.Rational(15, 2), 0, label="E")
    A = model.set_point(sp.Rational(15, 2), 4, classes=["given"], label="A")

    model.construct_line(B, E)

    # Segments
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(C, E)
    model.set_segment(B, C)
    model.set_segment(D, E)
    model.set_segment(B, E)
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(A, E)

    # Triangles
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, E])
    model.set_polygon([A, D, E])
    model.set_polygon([A, C, E])

    return model


if __name__ == "__main__":
    construct_0415_g3()
