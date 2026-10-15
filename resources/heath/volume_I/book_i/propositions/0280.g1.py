"""Programmatic construction for Book I, Proposition 9 Note — Conchoid Trisection (0280.g1).

Pappus' explanation of trisecting an acute angle ABC by means of the conchoid of
Nicomedes: completing rectangle FBCA, producing FA to E so that BE intercepts
DE = 2 * AB, and joining A to the midpoint G of DE.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0280_g1() -> Model:
    """Construct the figure for 0280.g1 using geometor.model."""
    model = Model("0280.g1")

    # 1. Acute angle ABC and perpendicular AC to BC, completed to parallelogram FBCA
    F = model.set_point(135, -22, label="F")
    A = model.set_point(191, -22, classes=["given"], label="A")
    E = model.set_point(414, -22, label="E")
    B = model.set_point(135, -123, classes=["given"], label="B")
    C = model.set_point(191, -123, classes=["given"], label="C")
    D = model.set_point(191, -103, label="D")
    G = model.set_point(304, -62, label="G")

    model.construct_line(F, E)
    model.set_section([F, A, E])
    model.set_segment(F, A)
    model.set_segment(A, E)
    model.set_segment(F, E)

    model.set_section([A, D, C])
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(A, C)

    model.set_segment(F, B)
    model.set_segment(B, C)
    model.set_segment(A, B)

    # Transversal B-D-G-E and midpoint connector AG
    model.set_section([B, D, G])
    model.set_section([D, G, E])
    model.set_segment(B, D)
    model.set_segment(D, G)
    model.set_segment(G, E)
    model.set_segment(D, E)
    model.set_segment(B, G)
    model.set_segment(B, E)
    model.set_segment(A, G)

    # Polygons
    model.set_polygon([F, B, C, A])
    model.set_polygon([F, B, A])
    model.set_polygon([A, B, C])
    model.set_polygon([A, G, E])
    model.set_polygon([A, D, G])
    model.set_polygon([A, B, G])

    return model


if __name__ == "__main__":
    construct_0280_g1()
