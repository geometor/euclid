"""Programmatic construction for Book XI, Proposition 20 (0311.g3).

If a solid angle be contained by three plane angles, any two, taken together in
any manner, are greater than the remaining one.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0311_g3() -> Model:
    """Construct the figure for Book XI, Proposition 20 using geometor.model."""
    model = Model("0311.g3")

    # 1. Let the solid angle at A be contained by the three plane angles
    #    BAC, CAD, DAB.
    A = model.set_point(0, 0, classes=["given"], label="A")
    D = model.set_point(sp.Rational(15, 60), sp.Rational(59, 60), classes=["given"], label="D")
    B = model.set_point(sp.Rational(-141, 60), sp.Rational(-47, 60), classes=["given"], label="B")
    C = model.set_point(sp.Rational(77, 60), sp.Rational(-47, 60), classes=["given"], label="C")

    # 2. In the plane through BA, AC construct angle BAE equal to angle DAB,
    #    make AE equal to AD, and draw BEC across through E cutting AB, AC at B, C.
    E = model.set_point(sp.Rational(38, 60), sp.Rational(-47, 60), label="E")

    # 3. Join DB, DC.
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(A, E)
    model.set_segment(B, C)
    model.set_segment(B, E)
    model.set_segment(E, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_section([B, E, C])

    # Triangles and planes
    model.set_polygon([B, A, C])
    model.set_polygon([B, A, E])
    model.set_polygon([E, A, C])
    model.set_polygon([D, A, B])
    model.set_polygon([D, A, C])
    model.set_polygon([B, D, C])

    return model


if __name__ == "__main__":
    construct_0311_g3()
