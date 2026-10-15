"""Programmatic construction for Book III, Proposition 12 Note (0035.g1).

Impossible hypothesis where A lies on FG produced in external contact:
collinear points F, C, D, G, A with circle on diameter DA (centre G)
and the impossible curve with centre F passing through C and touching at A.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0035_g1() -> Model:
    """Construct the figure 0035.g1 using geometor.model."""
    model = Model("0035.g1")

    # Collinear points F, C, D, G, A along the line of centres produced
    F = model.set_point(0, 0, classes=["given"], label="F")
    C = model.set_point(sp.Rational(1, 5), 0, label="C")
    D = model.set_point(sp.Rational(2, 5), 0, label="D")
    G = model.set_point(1, 0, classes=["given"], label="G")
    A = model.set_point(sp.Rational(8, 5), 0, classes=["given"], label="A")
    B = model.set_point(sp.Rational(11, 5), 0, classes=["auxiliary"], label="B")

    # Line through centres [ F A ]
    model.construct_line(F, A)

    # Circle with centre G and radius GA (diameter DA)
    model.construct_circle(G, A)

    # Hypothetical circle with centre F and radius FC
    model.construct_circle(F, C)

    # Collinear segments along F-C-D-G-A
    model.set_segment(F, C)
    model.set_segment(C, D)
    model.set_segment(D, G)
    model.set_segment(G, A)
    model.set_segment(F, D)
    model.set_segment(F, G)
    model.set_segment(F, A)
    model.set_segment(C, A)
    model.set_segment(D, A)
    model.set_segment(A, B)
    model.set_section([F, G, A])
    model.set_section([B, A, C])

    return model


if __name__ == "__main__":
    construct_0035_g1()
