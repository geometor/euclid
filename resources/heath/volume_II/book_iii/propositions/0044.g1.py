"""Programmatic construction for Book III, Proposition 16 (0044.g1).

The straight line drawn at right angles to the diameter of a circle from its
extremity will fall outside the circle, and into the space between the straight
line and the circumference another straight line cannot be interposed; further
the angle of the semicircle is greater, and the remaining angle less, than any
acute rectilineal angle.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0044_g1() -> Model:
    """Construct the figure for Book III, Proposition 16 using geometor.model."""
    model = Model("0044.g1")

    # 1. Circle ABC about centre D and diameter AB
    D = model.set_point(0, 0, classes=["given"], label="D")
    B = model.set_point(0, 1, classes=["given"], label="B")
    A = model.set_point(0, -1, classes=["given"], label="A")
    circle_ABC = model.construct_circle(D, A)

    model.set_segment(B, D)
    model.set_segment(D, A)
    model.set_segment(B, A)
    model.set_section([B, D, A])

    # 2. First reductio: suppose perpendicular from A falls within as CA; join DC
    cx = sp.Rational(-27, 35)
    cy = -sp.sqrt(1 - cx**2)
    C = model.set_point(cx, cy, label="C")
    model.set_segment(C, A)
    model.set_segment(D, C)
    model.set_polygon([A, C, D])

    # 3. Tangent AE drawn from A at right angles to AB
    E = model.set_point(sp.Rational(-67, 35), -1, label="E")
    line_AE = model.construct_line(A, E)
    model.set_segment(A, E)

    # 4. Second reductio: suppose FA is interposed between AE and circumference CHA,
    #    and DG is drawn from D perpendicular to FA, cutting circumference CHA at H.
    F = model.set_point(sp.Rational(-65, 35), sp.Rational(-51, 70), label="F")
    line_AF = model.construct_line(A, F)

    # Point G on FA and point H where DG meets the circumference CHA
    t_G = sp.Rational(16, 65)
    G = model.set_point(F.x * t_G, -1 + (F.y + 1) * t_G, label="G")
    len_DG = sp.sqrt(G.x**2 + G.y**2)
    H = model.set_point(G.x / len_DG, G.y / len_DG, label="H")

    model.set_segment(A, G)
    model.set_segment(G, F)
    model.set_segment(F, A)
    model.set_section([A, G, F])

    model.set_segment(D, H)
    model.set_segment(H, G)
    model.set_segment(D, G)
    model.set_section([D, H, G])

    model.set_polygon([A, G, D])

    return model


if __name__ == "__main__":
    construct_0044_g1()
