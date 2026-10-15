"""Programmatic construction for Book I, Postulate 2 Note — Proclus' Proof (0211.g1).

Proclus' attempted proof that two straight lines cannot have a common segment AB,
using a circle with centre B and radius BA meeting AC and AD in C and D.
"""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0211_g1() -> Model:
    """Construct the figure for 0211.g1 using geometor.model."""
    model = Model("0211.g1")

    # Common segment AB and centre B
    A = model.set_point(40.5, -122.5, classes=["given"], label="A")
    B = model.set_point(116.5, -122.5, classes=["given"], label="B")
    model.set_segment(A, B)

    # Circle with centre B and radius BA
    r = 76.0
    model.construct_circle(B, A)

    # Diameter ABD (horizontal) and supposed second straight line ABC through B
    D = model.set_point(192.5, -122.5, label="D")
    angle_c = math.radians(25.0)
    C = model.set_point(
        round(116.5 + r * math.cos(angle_c), 2),
        round(-122.5 + r * math.sin(angle_c), 2),
        label="C",
    )

    # Point E on the upper circumference defining semi-circles AEC and AED
    angle_e = math.radians(125.0)
    E = model.set_point(
        round(116.5 + r * math.cos(angle_e), 2),
        round(-122.5 + r * math.sin(angle_e), 2),
        label="E",
    )

    model.set_segment(B, D)
    model.set_segment(A, D)
    model.set_segment(B, C)
    model.set_segment(A, C)
    model.set_section([A, B, D])
    model.set_section([A, B, C])

    return model


if __name__ == "__main__":
    construct_0211_g1()
