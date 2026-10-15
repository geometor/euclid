"""Programmatic construction for Book III, Proposition 17 (0049.g1).

From a given point to draw a straight line touching a given circle.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0049_g1() -> Model:
    """Construct the figure for Book III, Proposition 17 using geometor.model."""
    model = Model("0049.g1")

    # 1. Let A be the given point, and BCD the given circle about centre E.
    E = model.set_point(0, 0, classes=["given"], label="E")
    D = model.set_point(0, 1, classes=["given"], label="D")
    C = model.set_point(1, 0, label="C")
    r_outer = sp.Rational(45, 29)
    A = model.set_point(0, r_outer, classes=["given"], label="A")

    circle_BCD = model.construct_circle(E, D)

    # 2. Let AE be joined, and with centre E and distance EA describe circle AFG.
    model.set_segment(E, D)
    model.set_segment(D, A)
    model.set_segment(A, E)
    model.set_section([E, D, A])

    circle_AFG = model.construct_circle(E, A)

    # 3. From D draw DF at right angles to EA meeting circle AFG at F.
    fx = -sp.sqrt(r_outer**2 - 1)
    F = model.set_point(fx, 1, label="F")
    G = model.set_point(sp.Rational(34, 29), -sp.sqrt(r_outer**2 - sp.Rational(34, 29) ** 2), label="G")
    model.set_segment(D, F)

    # 4. Join EF (cutting circle BCD at B) and join AB.
    B = model.set_point(fx / r_outer, 1 / r_outer, label="B")
    model.set_segment(E, B)
    model.set_segment(B, F)
    model.set_segment(E, F)
    model.set_section([E, B, F])

    model.set_segment(A, B)

    # 5. Triangles DEF and BEA
    model.set_polygon([D, E, F])
    model.set_polygon([B, E, A])

    return model


if __name__ == "__main__":
    construct_0049_g1()
