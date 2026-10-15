"""Programmatic construction for Book XI, Proposition 37 Interpolated Lemma (0364.g1).

Plane CAD perpendicular to plane AB with common section AD, and perpendicular
EF drawn from E in CAD to AB, with FG drawn in AB perpendicular to AD.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0364_g1() -> Model:
    """Construct the perpendicular planes lemma figure for 0364.g1 using geometor.model."""
    model = Model("0364.g1")

    C = model.set_point(sp.Rational(22, 100), sp.Rational(83, 100), classes=["given"], label="C")
    C_right = model.set_point(sp.Rational(148, 100), sp.Rational(83, 100), label="C_right")
    D = model.set_point(sp.Rational(148, 100), sp.Rational(35, 100), classes=["given"], label="D")
    A = model.set_point(sp.Rational(22, 100), sp.Rational(35, 100), classes=["given"], label="A")

    B_left = model.set_point(sp.Rational(74, 100), sp.Rational(15, 100), label="B_left")
    B = model.set_point(sp.Rational(204, 100), sp.Rational(15, 100), classes=["given"], label="B")

    E = model.set_point(sp.Rational(95, 100), sp.Rational(65, 100), classes=["given"], label="E")
    F = model.set_point(sp.Rational(95, 100), sp.Rational(21, 100), label="F")
    G = model.set_point(sp.Rational(78, 100), sp.Rational(35, 100), label="G")

    for p1, p2 in [
        (C, C_right), (C_right, D), (D, A), (A, C),
        (A, B_left), (B_left, B), (B, D),
        (A, G), (G, D),
        (E, F), (F, G), (E, G),
    ]:
        model.set_segment(p1, p2)

    model.set_polygon([C, C_right, D, A])
    model.set_polygon([A, D, B, B_left])
    model.set_polygon([E, G, F])

    return model


if __name__ == "__main__":
    construct_0364_g1()
