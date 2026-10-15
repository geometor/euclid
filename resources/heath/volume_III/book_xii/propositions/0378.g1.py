"""Programmatic construction for Book XII, Proposition 2 Commentary (0378.g1).

Exhaustion of a circular segment ACB by inscribed triangle ACB and tangent
rectangle ABED.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0378_g1() -> Model:
    """Construct the figure 0378.g1 using geometor.model."""
    model = Model("0378.g1")

    # Circle center O and top midpoint C of arc ACB
    O = model.set_point(91.0, -108.0, label="O")
    C = model.set_point(91.0, -38.0, classes=["given"], label="C")

    # Chord endpoints A, B and tangent rectangle corners D, E
    A = model.set_point(54.94, -48.0, classes=["given"], label="A")
    B = model.set_point(127.06, -48.0, classes=["given"], label="B")
    D = model.set_point(54.94, -38.0, label="D")
    E = model.set_point(127.06, -38.0, label="E")

    # Circle
    model.construct_circle(O, C)

    # Segments
    for p1, p2 in [
        (A, B), (D, E), (D, C), (C, E),
        (A, D), (B, E), (A, C), (C, B),
    ]:
        model.set_segment(p1, p2)

    # Polygons
    model.set_polygon([A, B, E, D])
    model.set_polygon([A, C, B])

    # Angles
    model.set_wedge(C, E, E, B)
    model.set_wedge(A, C, C, B)
    model.set_wedge(B, C, C, A)

    return model


if __name__ == "__main__":
    construct_0378_g1()
