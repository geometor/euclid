"""Programmatic construction for Book XI, Proposition 23 Lemma (0322.g1).

On diameter AB describe semicircle ABC, fit chord AC equal to LO, and join CB
so that angle ACB is right and AB^2 - AC^2 = CB^2.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0322_g1() -> Model:
    """Construct the Lemma figure for Book XI, Proposition 23 using geometor.model."""
    model = Model("0322.g1")

    A = model.set_point(-1, 0, classes=["given"], label="A")
    B = model.set_point(1, 0, classes=["given"], label="B")
    O = model.set_point(0, 0, label="O")
    C = model.set_point(0, 1, label="C")

    # Semicircle on AB (modeled via circle centered at midpoint O through A)
    model.construct_circle(O, A)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Right triangle ACB
    model.set_polygon([A, C, B])

    # Right angle ACB
    model.set_wedge(C, A, A, B)

    return model


if __name__ == "__main__":
    construct_0322_g1()
