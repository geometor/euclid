"""Programmatic construction for Book II, Proposition 13 converse (0422.g2).

Heron's converse of Book II, Proposition 13: In any triangle in which the
square on one of the sides is less than the squares on the other two sides,
the angle contained by the latter sides is acute.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0422_g2() -> Model:
    """Construct the figure for 0422.g2 using geometor.model."""
    model = Model("0422.g2")

    # Triangle ABC with BD perpendicular to BC and BD = BA
    B = model.set_point(0, 0, classes=["given"], label="B")
    C = model.set_point(4, 0, classes=["given"], label="C")
    A = model.set_point(1, sp.sqrt(24), classes=["given"], label="A")
    D = model.set_point(0, 5, label="D")

    # Segments
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(B, A)
    model.set_segment(A, C)

    # Triangles DBC and ABC
    model.set_polygon([D, B, C])
    model.set_polygon([A, B, C])

    # Angles DBC and ABC
    model.set_wedge(B, C, C, D)
    model.set_wedge(B, C, C, A)

    return model


if __name__ == "__main__":
    construct_0422_g2()
