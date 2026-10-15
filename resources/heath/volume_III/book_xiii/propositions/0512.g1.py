"""Programmatic construction for Book XIII, Proposition 18 Lemma (0512.g1).

Equilateral and equiangular pentagon ABCDE inscribed in a circle with center F.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0512_g1() -> Model:
    """Construct the figure 0512.g1 using geometor.model."""
    model = Model("0512.g1")

    F = model.set_point(0, 0, classes=["given"], label="F")
    A = model.set_point(0, 1, classes=["given"], label="A")

    # Circumscribed circle ABCDE
    model.construct_circle(F, A)

    # Regular pentagon vertices A, B, C, D, E clockwise
    B = model.set_point(
        sp.sqrt(10 + 2 * sp.sqrt(5)) / 4,
        (sp.sqrt(5) - 1) / 4,
        classes=["constructed"],
        label="B",
    )
    C = model.set_point(
        sp.sqrt(10 - 2 * sp.sqrt(5)) / 4,
        -(sp.sqrt(5) + 1) / 4,
        classes=["constructed"],
        label="C",
    )
    D = model.set_point(
        -sp.sqrt(10 - 2 * sp.sqrt(5)) / 4,
        -(sp.sqrt(5) + 1) / 4,
        classes=["constructed"],
        label="D",
    )
    E = model.set_point(
        -sp.sqrt(10 + 2 * sp.sqrt(5)) / 4,
        (sp.sqrt(5) - 1) / 4,
        classes=["constructed"],
        label="E",
    )

    # Pentagon ABCDE and central triangles
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([F, A, B])
    model.set_polygon([F, B, C])
    model.set_polygon([F, C, D])
    model.set_polygon([F, D, E])
    model.set_polygon([F, E, A])

    # Pentagon edges and radii
    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, E), (E, A),
        (F, A), (F, B), (F, C), (F, D), (F, E),
    ]:
        model.set_segment(p1, p2)

    # Wedges (angles)
    model.set_wedge(F, A, A, B)
    model.set_wedge(A, F, F, B)
    model.set_wedge(B, A, A, F)
    model.set_wedge(B, F, F, C)
    model.set_wedge(B, A, A, C)

    return model


if __name__ == "__main__":
    construct_0512_g1()
