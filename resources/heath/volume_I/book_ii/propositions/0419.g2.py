"""Programmatic construction for Book II, Proposition 12 converse (0419.g2).

Heron's converse of Book II, Proposition 12: In any triangle, if the square on
one of the sides is greater than the squares on the other two sides, the angle
contained by the latter is obtuse.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0419_g2() -> Model:
    """Construct the figure for 0419.g2 using geometor.model."""
    model = Model("0419.g2")

    # Triangle ABC with angle BAC obtuse, and AD perpendicular to AC with AD = AB
    A = model.set_point(0, 0, classes=["given"], label="A")
    C = model.set_point(7, 0, classes=["given"], label="C")
    B = model.set_point(-2, sp.sqrt(12), classes=["given"], label="B")
    D = model.set_point(0, 4, label="D")

    # Segments
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, D)
    model.set_segment(D, C)

    # Triangles BAC and DAC
    model.set_polygon([A, B, C])
    model.set_polygon([D, A, C])

    # Angles BAC and DAC
    model.set_wedge(A, B, B, C)
    model.set_wedge(A, D, D, C)

    return model


if __name__ == "__main__":
    construct_0419_g2()
