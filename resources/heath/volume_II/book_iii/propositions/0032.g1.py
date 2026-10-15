"""Programmatic construction for Book III, Proposition 11 Note (0032.g1).

Hypothesis (a) in Camerer/Heath's commentary on Book III, Proposition 11:
point of contact A lies on GF produced beyond F, and FG produced beyond G
meets the outer circle at H and the inner circle at D (with GD > GH), so the
circles intersect at X and Y.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0032_g1() -> Model:
    """Construct the figure 0032.g1 using geometor.model."""
    model = Model("0032.g1")

    # Outer circle with centre F(0, 0) and horizontal diameter HA
    F = model.set_point(0, 0, classes=["given"], label="F")
    A = model.set_point(1, 0, classes=["given"], label="A")
    H = model.set_point(-1, 0, label="H")
    model.construct_line(H, A)
    model.construct_circle(F, A)

    # Inner centre G to the left of F, and point D beyond H on FG produced
    G = model.set_point(sp.Rational(-18, 53), 0, classes=["given"], label="G")
    D = model.set_point(sp.Rational(-79, 53), 0, label="D")

    # Symmetric intersection points X (above) and Y (below) of the two circles
    X = model.set_point(sp.Rational(-40, 53), sp.sqrt(1209) / 53, label="X")
    Y = model.set_point(sp.Rational(-40, 53), -sp.sqrt(1209) / 53, label="Y")

    # Collinear segments along D-H-G-F-A
    model.set_segment(D, H)
    model.set_segment(H, G)
    model.set_segment(G, F)
    model.set_segment(F, A)
    model.set_segment(G, D)
    model.set_segment(G, H)
    model.set_segment(F, D)
    model.set_segment(F, H)
    model.set_segment(G, A)
    model.set_segment(D, A)

    # Segments to X and Y
    model.set_segment(F, X)
    model.set_segment(G, X)
    model.set_segment(F, Y)
    model.set_segment(G, Y)

    return model


if __name__ == "__main__":
    construct_0032_g1()
