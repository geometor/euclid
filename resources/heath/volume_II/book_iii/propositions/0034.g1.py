"""Programmatic construction for Book III, Proposition 12 (0034.g1).

If two circles touch one another externally, the straight line joining their
centres will pass through the point of contact (reductio ad absurdum figure).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0034_g1() -> Model:
    """Construct the figure 0034.g1 using geometor.model."""
    model = Model("0034.g1")

    # Point of external contact A and true circle centres for the two tangent circles
    A = model.set_point(0, 0, classes=["given"], label="A")
    O1 = model.set_point(-49, 23, classes=["auxiliary"])
    O2 = model.set_point(60, -28, classes=["auxiliary"])

    # Circle ABC and circle ADE touching externally at A
    model.construct_circle(O1, A)
    model.construct_circle(O2, A)

    B = model.set_point(-49, 23 + sp.sqrt(2930), label="B")
    E = model.set_point(60 + sp.sqrt(4384), -28, label="E")

    # Assumed centres F and G in the reductio proof
    F = model.set_point(-53, 12, classes=["given"], label="F")
    G = model.set_point(47, -52, classes=["given"], label="G")

    # Straight line FCDG joining the assumed centres F and G
    model.construct_line(F, G)

    # Intersections C (on circle ABC) and D (on circle ADE) along FG
    C = model.set_point(sp.Rational(-53, 5), sp.Rational(-76, 5), label="C")
    D = model.set_point(sp.Rational(-28, 5), sp.Rational(-92, 5), label="D")

    # Radii joined to the point of contact A
    model.set_segment(F, A)
    model.set_segment(G, A)

    # Collinear segments along FCDG
    model.set_segment(F, C)
    model.set_segment(C, D)
    model.set_segment(D, G)
    model.set_segment(F, D)
    model.set_segment(C, G)
    model.set_segment(F, G)
    model.set_section([F, C, G])
    model.set_section([F, D, G])

    # Triangle FAG formed in the reductio hypothesis
    model.set_polygon([F, A, G])

    return model


if __name__ == "__main__":
    construct_0034_g1()
