"""Programmatic construction for Book I, Definitions Commentary (0174.g1).

Conchoid of Nicomedes (both the first conchoid and the looped variety where
the constant distance a is greater than the distance b of the pole O from
the fixed straight line / asymptote).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0174_g1() -> Model:
    """Construct the Conchoid of Nicomedes diagram (0174.g1) using geometor.model."""
    model = Model("0174.g1")

    # Pole O and foot A of perpendicular on the fixed straight line (asymptote)
    # Distance b = |OA| = 17/10, constant distance a = |AV| = 3 (so a > b).
    b = sp.Rational(17, 10)
    a = sp.Integer(3)

    O = model.set_point(0, -b, classes=["given"], label="O")
    A = model.set_point(0, 0, classes=["given"], label="A")

    # Fixed straight line (asymptote) through A perpendicular to OA
    L = model.set_point(-7, 0, classes=["given"], label="L")
    R = model.set_point(7, 0, classes=["given"], label="R")
    model.construct_line(L, R)
    model.set_segment(L, R)

    # Vertical axis through O and A
    model.construct_line(O, A)

    # Circle of radius a centered at A determines the vertices V (upper) and B (loop bottom)
    c_A = model.construct_circle(A, model.set_point(0, a, label="V"))
    V = model.get_element_by_ID("V")
    B = model.set_point(0, -a, label="B")

    # Collinear segments along the principal axis: b = OA, a = AV, and loop depth OB = a - b
    model.set_section([B, O, A])
    model.set_section([O, A, V])
    model.set_segment(O, A)
    model.set_segment(A, V)
    model.set_segment(O, B)
    model.set_segment(A, B)
    model.set_segment(B, V)

    # Sample rays from pole O intersecting the fixed line at M1..M4
    for idx, x_m in enumerate(
        [sp.Rational(2, 5), sp.Rational(4, 5), sp.Rational(7, 5), sp.Rational(13, 5)],
        start=1,
    ):
        M = model.set_point(x_m, 0, label=f"M{idx}")
        model.construct_line(O, M)
        dist_OM = sp.sqrt(x_m**2 + b**2)
        ux = x_m / dist_OM
        uy = b / dist_OM
        P = model.set_point(x_m + a * ux, a * uy, label=f"P{idx}")
        Q = model.set_point(x_m - a * ux, -a * uy, label=f"Q{idx}")
        model.set_segment(O, M)
        model.set_segment(M, P)
        model.set_segment(M, Q)

    return model


if __name__ == "__main__":
    construct_0174_g1()
