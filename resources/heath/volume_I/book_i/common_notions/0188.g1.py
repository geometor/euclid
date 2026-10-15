"""Programmatic construction for Book I, Definitions Commentary (0188.g1).

W. Bolyai and Lobachewsky's construction of a perpendicular CD to diameter AB
in a circle of intersection k of two equal spheres: circumference is bisected at
A and B, arc ADB is bisected at D, and C is the midpoint of AB.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0188_g1() -> Model:
    """Construct the Bolyai-Lobachewsky circle diagram (0188.g1)."""
    model = Model("0188.g1")

    # 1. Circle k with center C and diameter AB dividing the circumference into halves
    C = model.set_point(0, 0, classes=["given"], label="C")
    A = model.set_point(-1, 0, classes=["given"], label="A")
    B = model.set_point(1, 0, classes=["given"], label="B")

    circle_k = model.construct_circle(C, A)
    line_AB = model.construct_line(A, B)

    model.set_section([A, C, B])
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(A, B)

    # 2. Arc ADB bisected at D, determining perpendicular CD to AB
    D = model.set_point(0, 1, label="D")
    E = model.set_point(0, -1, label="E")
    line_CD = model.construct_line(C, D)

    model.set_section([D, C, E])
    model.set_segment(C, D)
    model.set_segment(C, E)
    model.set_segment(D, E)

    # Semicircular arc ADB and quadrants AD, DB
    model.set_wedge(C, A, B, A)
    model.set_wedge(C, A, D, A)
    model.set_wedge(C, A, B, D)

    return model


if __name__ == "__main__":
    construct_0188_g1()
