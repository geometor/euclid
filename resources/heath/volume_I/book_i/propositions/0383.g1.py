"""Programmatic construction for Proposition 48 Commentary (0383.g1).

Proclus and Heron's alternative proof by contradiction of Book I, Proposition 48
using Book I, Proposition 7.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0383_g1() -> Model:
    """Construct Proclus/Heron alternative proof figure (0383.g1) using geometor.model."""
    model = Model("0383.g1")

    A = model.set_point(108, -28, classes=["given"], label="A")
    C = model.set_point(26, -86, classes=["given"], label="C")
    B = model.set_point(150, -86, classes=["given"], label="B")
    D = model.set_point(131, -96, label="D")
    E = model.set_point(175, -52, label="E")

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, C])
    model.set_polygon([A, E, C])

    # Segments
    for p1, p2 in [(A, C), (A, B), (B, C), (A, D), (D, C), (A, E), (E, C)]:
        model.set_segment(p1, p2)

    # Angles
    model.set_wedge(A, C, C, B)  # < C A B )
    model.set_wedge(A, C, C, D)  # < C A D )
    model.set_wedge(A, C, C, E)  # < C A E )

    return model


if __name__ == "__main__":
    construct_0383_g1()
