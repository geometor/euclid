"""Programmatic construction for Book III, Proposition 14 (0041.g1).

In a circle equal straight lines are equally distant from the centre,
and those which are equally distant from the centre are equal to one another.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0041_g1() -> Model:
    """Construct the figure 0041.g1 using geometor.model."""
    model = Model("0041.g1")

    # Centre E of circle ABDC with radius 62
    E = model.set_point(0, 0, classes=["given"], label="E")

    # Equal chords AB and CD at distance 36 from centre E
    h = sp.sqrt(62**2 - 36**2)
    G = model.set_point(36, 0, label="G")
    D = model.set_point(36, h, label="D")
    C = model.set_point(36, -h, label="C")

    # Circle ABDC
    model.construct_circle(E, D)

    # Chord AB rotated by -135 degrees so EF has length 36
    inv_sqrt2 = sp.sqrt(2) / 2
    F = model.set_point(-36 * inv_sqrt2, -36 * inv_sqrt2, label="F")
    B = model.set_point((-36 - h) * inv_sqrt2, (-36 + h) * inv_sqrt2, label="B")
    A = model.set_point((-36 + h) * inv_sqrt2, (-36 - h) * inv_sqrt2, label="A")

    # Chords AB and CD and their half-segments
    model.set_segment(B, F)
    model.set_segment(F, A)
    model.set_segment(A, B)
    model.set_section([A, F, B])

    model.set_segment(D, G)
    model.set_segment(G, C)
    model.set_segment(C, D)
    model.set_section([C, G, D])

    # Perpendiculars EF, EG and radii AE, EC
    model.set_segment(E, F)
    model.set_segment(E, G)
    model.set_segment(A, E)
    model.set_segment(E, C)

    # Right triangles EFA and EGC
    model.set_polygon([E, F, A])
    model.set_polygon([E, G, C])

    return model


if __name__ == "__main__":
    construct_0041_g1()
