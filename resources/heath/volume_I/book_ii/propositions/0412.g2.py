"""Programmatic construction for Book II, Proposition 10 divided line (0412.g2).

Divided straight line AB at C and D illustrating side and diagonal numbers.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0412_g2() -> Model:
    """Construct the divided straight line figure 0412.g2."""
    model = Model("0412.g2")

    # Straight line AB bisected at C and divided at D
    A = model.set_point(0, 0, classes=["given"], label="A")
    C = model.set_point(5, 0, classes=["given"], label="C")
    D = model.set_point(8, 0, classes=["given"], label="D")
    B = model.set_point(10, 0, classes=["given"], label="B")

    model.set_segment(A, C)
    model.set_segment(C, D)
    model.set_segment(D, B)
    model.set_segment(A, D)
    model.set_segment(C, B)
    model.set_segment(A, B)
    model.set_section([A, C, B])
    model.set_section([A, D, B])

    return model


if __name__ == "__main__":
    construct_0412_g2()
