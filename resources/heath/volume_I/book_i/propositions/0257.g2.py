"""Programmatic construction for Book I, Proposition 1 Note — Scalene Triangle (0257.g2).

Proclus' construction of a scalene triangle using the two circles of Proposition 1.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0257_g2() -> Model:
    """Construct Proclus' scalene triangle figure (0257.g2) using geometor.model."""
    model = Model("0257.g2")

    # 1. Given finite straight line AB and circles ( A B ) and ( B A )
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(1, 0, classes=["given"], label="B")
    model.set_segment(A, B)

    model.construct_circle(A, B)
    model.construct_circle(B, A)

    # 2. Radius AC of circle ( A B ) lying outside circle ( B A )
    C = model.set_point(
        -sp.Rational(31, 78),
        sp.sqrt(1 - sp.Rational(31, 78) ** 2),
        label="C",
    )
    model.set_segment(A, C)

    # 3. Point D on AC in the portion of circle ( A B ) outside circle ( B A )
    t = sp.Rational(39, 62)
    D = model.set_point(t * C.x, t * C.y, label="D")
    model.set_section([A, D, C])
    model.set_segment(A, D)
    model.set_segment(D, C)

    # 4. Join BD, intersecting circle ( B A ) at E, forming scalene triangle ABD
    model.set_segment(B, D)
    dist_BD = sp.sqrt((D.x - B.x) ** 2 + (D.y - B.y) ** 2)
    E = model.set_point(
        B.x + (D.x - B.x) / dist_BD,
        B.y + (D.y - B.y) / dist_BD,
        label="E",
    )
    model.set_section([B, E, D])
    model.set_polygon([A, B, D])

    return model


if __name__ == "__main__":
    construct_0257_g2()
