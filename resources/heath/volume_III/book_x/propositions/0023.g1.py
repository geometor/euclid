"""Programmatic construction for Book X, Proposition 2 commentary (0023.g1)."""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0023_g1() -> Model:
    """Construct Chrystal's square ABCD with FE perpendicular to AC (0023.g1)."""
    model = Model("0023.g1")

    # Vertices of square ABCD (B top-left, A top-right, C bottom-left, D bottom-right)
    B = model.set_point(19.0, -21.0, classes=["given"], label="B")
    A = model.set_point(161.0, -21.0, classes=["given"], label="A")
    C = model.set_point(19.0, -163.0, classes=["given"], label="C")
    D = model.set_point(161.0, -163.0, classes=["given"], label="D")

    # Point F on AC such that AF = AB = 142
    a = 142.0
    F = model.set_point(
        161.0 - a / math.sqrt(2.0),
        -21.0 - a / math.sqrt(2.0),
        label="F",
    )

    # Point E on BC such that FE is perpendicular to AC
    d = a * math.sqrt(2.0)
    a1 = d - a
    d1 = a1 * math.sqrt(2.0)
    E = model.set_point(19.0, -163.0 + d1, label="E")

    # Fourth vertex G of smaller square CFEG
    G = model.set_point(19.0 - (60.59 - 19.0), -121.41, label="G")

    # Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, C])
    model.set_polygon([A, B, E, F])
    model.set_polygon([C, F, E])
    model.set_polygon([C, F, E, G])

    # Sides and diagonal segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)
    model.set_segment(B, E)
    model.set_segment(E, C)
    model.set_segment(A, F)
    model.set_segment(F, C)
    model.set_segment(A, C)
    model.set_segment(F, E)
    model.set_segment(E, G)
    model.set_segment(G, C)

    # Collinear sections
    model.set_section([B, E, C])
    model.set_section([A, F, C])

    # Angle wedges
    model.set_wedge(A, F, F, E)
    model.set_wedge(C, F, F, E)

    return model


if __name__ == "__main__":
    construct_0023_g1()
