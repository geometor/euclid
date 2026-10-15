"""Programmatic construction for Book I, Postulate 1 Note — Proclus' Proof (0210.g1).

Proclus' attempted proof that two straight lines cannot enclose a space, using a
circle with centre B and radius BA meeting the produced lines ACBF and ADBE in F and E.
"""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0210_g1() -> Model:
    """Construct the figure for 0210.g1 using geometor.model."""
    model = Model("0210.g1")

    # Centre B and point A on the circumference
    B = model.set_point(86.5, -85.0, classes=["given"], label="B")
    A = model.set_point(27.5, -85.0, classes=["given"], label="A")
    model.set_segment(A, B)

    # Circle with centre B and distance AB
    model.construct_circle(B, A)

    # Points C and D on the two supposed straight lines between A and B
    C = model.set_point(57.0, -77.0, label="C")
    D = model.set_point(57.0, -93.0, label="D")

    # Points E and F where the produced lines meet the circle
    r = 59.0
    angle = math.radians(35.0)
    E = model.set_point(
        round(86.5 + r * math.cos(angle), 2),
        round(-85.0 + r * math.sin(angle), 2),
        label="E",
    )
    F = model.set_point(
        round(86.5 + r * math.cos(angle), 2),
        round(-85.0 - r * math.sin(angle), 2),
        label="F",
    )

    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(B, F)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(B, E)

    return model


if __name__ == "__main__":
    construct_0210_g1()
