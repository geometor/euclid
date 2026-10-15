"""Programmatic construction for Book I, Postulate 2 Note — Zeno and Posidonius (0213.g1).

Proof recorded by Proclus (and criticised by Zeno) that two straight lines AC, AD
cannot have a common segment AB, using perpendiculars BE and BF at B.
"""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0213_g1() -> Model:
    """Construct the figure for 0213.g1 using geometor.model."""
    model = Model("0213.g1")

    # Common segment AB and straight line AC
    A = model.set_point(25.0, -102.0, classes=["given"], label="A")
    B = model.set_point(92.0, -102.0, classes=["given"], label="B")
    C = model.set_point(165.0, -102.0, label="C")

    # Supposed second continuation BD at angle 17 degrees
    r = 79.0
    theta = math.radians(17.0)
    D = model.set_point(
        round(92.0 + r * math.cos(theta), 2),
        round(-102.0 + r * math.sin(theta), 2),
        label="D",
    )

    # Perpendiculars BE to AC and BF to AD
    E = model.set_point(92.0, -23.0, label="E")
    F = model.set_point(
        round(92.0 - r * math.sin(theta), 2),
        round(-102.0 + r * math.cos(theta), 2),
        label="F",
    )

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(A, D)
    model.set_segment(B, E)
    model.set_segment(B, F)

    model.set_section([A, B, C])
    model.set_section([A, B, D])

    return model


if __name__ == "__main__":
    construct_0213_g1()
