"""Programmatic construction for Book III, Proposition 7 Note (0023.g1).

Heron's second case: A is a point on the diameter CB (not the centre D), and
AE, AF are drawn to the circumference on opposite sides of CB such that the
perpendicular DG from D to AE falls on AE itself, while the perpendicular DH
from D to AF falls on FA produced beyond A.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0023_g1() -> Model:
    """Construct the figure 0023.g1 using geometor.model."""
    model = Model("0023.g1")

    # Circle centre D and diameter endpoints C, B
    D = model.set_point(0, 0, classes=["given"], label="D")
    B = model.set_point(1, 0, classes=["given"], label="B")
    C = model.set_point(-1, 0, label="C")

    model.construct_line(C, B)
    model.construct_circle(D, B)

    # Internal point A on segment CD
    A = model.set_point(sp.Rational(-23, 35), 0, classes=["given"], label="A")

    # Point E on upper circumference and point F on lower circumference
    E = model.set_point(sp.Rational(1, 2), sp.sqrt(3) / 2, label="E")
    F = model.set_point(sp.Rational(-4, 5), sp.Rational(-3, 5), label="F")

    model.construct_line(A, E)
    model.construct_line(F, A)

    # Foot of perpendicular G from D on AE
    # Line AE through A(-23/35, 0) and E(1/2, sqrt(3)/2)
    dx_AE = sp.Rational(1, 2) - sp.Rational(-23, 35)
    dy_AE = sp.sqrt(3) / 2
    t_G = (sp.Rational(23, 35) * dx_AE) / (dx_AE**2 + dy_AE**2)
    G = model.set_point(
        sp.Rational(-23, 35) + t_G * dx_AE,
        t_G * dy_AE,
        label="G",
    )

    # Foot of perpendicular H from D on FA produced
    dx_FA = sp.Rational(-23, 35) - sp.Rational(-4, 5)
    dy_FA = sp.Rational(3, 5)
    t_H = (sp.Rational(23, 35) * dx_FA) / (dx_FA**2 + dy_FA**2)
    H = model.set_point(
        sp.Rational(-23, 35) + t_H * dx_FA,
        t_H * dy_FA,
        label="H",
    )

    # Diameter segments
    model.set_segment(C, A)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(C, D)
    model.set_segment(A, B)
    model.set_segment(C, B)
    model.set_section([C, A, D])
    model.set_section([A, D, B])

    # Segments along AE
    model.set_segment(A, G)
    model.set_segment(G, E)
    model.set_segment(A, E)
    model.set_section([A, G, E])

    # Segments along FAH
    model.set_segment(F, A)
    model.set_segment(A, H)
    model.set_segment(F, H)
    model.set_section([F, A, H])

    # Radii and perpendiculars from D
    model.set_segment(D, G)
    model.set_segment(D, H)
    model.set_segment(D, E)
    model.set_segment(D, F)

    # Right-angled triangles used in Heron's argument
    model.set_polygon([D, G, E])
    model.set_polygon([D, G, A])
    model.set_polygon([D, H, F])
    model.set_polygon([D, H, A])

    return model


if __name__ == "__main__":
    construct_0023_g1()
