"""Programmatic construction for Book III, Proposition 9 Alternative Proof (0028.g1).

Alternative proof (Simson) of Book III, Proposition 9: from internal point D,
three equal straight lines DA, DB, DC fall on the circle ABC; if D is not the
centre, let the centre be E and draw diameter FG through D and E.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0028_g1() -> Model:
    """Construct the figure 0028.g1 using geometor.model."""
    model = Model("0028.g1")

    # Visual circle ABC centred at D(0, 0) with horizontal diameter FG
    D = model.set_point(0, 0, classes=["given"], label="D")
    G = model.set_point(1, 0, label="G")
    F = model.set_point(-1, 0, label="F")
    E = model.set_point(sp.Rational(25, 66), 0, label="E")

    model.construct_line(F, G)
    model.construct_circle(D, G)

    # Points A, B, C on the lower circumference
    A = model.set_point(sp.Rational(-3, 5), sp.Rational(-4, 5), classes=["given"], label="A")
    B = model.set_point(sp.Rational(7, 25), sp.Rational(-24, 25), classes=["given"], label="B")
    C = model.set_point(sp.Rational(12, 13), sp.Rational(-5, 13), classes=["given"], label="C")

    # Segments along diameter F-D-E-G
    model.set_segment(F, D)
    model.set_segment(D, E)
    model.set_segment(E, G)
    model.set_segment(F, E)
    model.set_segment(D, G)
    model.set_segment(F, G)
    model.set_section([F, D, G])
    model.set_section([D, E, G])

    # Equal straight lines DA, DB, DC
    model.set_segment(D, A)
    model.set_segment(D, B)
    model.set_segment(D, C)

    return model


if __name__ == "__main__":
    construct_0028_g1()
