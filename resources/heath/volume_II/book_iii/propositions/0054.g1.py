"""Programmatic construction for Book III, Proposition 20 Heron Note (0054.g1).

Heron's extension of Book III, Proposition 20 to the case where the segment is
less than a semicircle.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0054_g1() -> Model:
    """Construct the figure for Heron's extension of III.20 (0054.g1)."""
    model = Model("0054.g1")

    # 1. Circle ABEC about centre D
    D = model.set_point(0, 0, classes=["given"], label="D")
    E = model.set_point(0, -1, classes=["given"], label="E")
    circle_ABEC = model.construct_circle(D, E)

    # Points B, C, F, G, A on circumference
    bx = sp.Rational(-17, 44)
    by = -sp.sqrt(1 - bx**2)
    B = model.set_point(bx, by, classes=["given"], label="B")
    C = model.set_point(-bx, by, classes=["given"], label="C")
    F = model.set_point(-bx, -by, label="F")
    G = model.set_point(bx, -by, label="G")

    ax = sp.Rational(5, 44)
    ay = sp.sqrt(1 - ax**2)
    A = model.set_point(ax, ay, classes=["given"], label="A")

    # 2. Chords AB, AC, BE, EC and diameters BDF, CDG, radius DE
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, E)
    model.set_segment(E, C)

    model.set_segment(B, D)
    model.set_segment(D, F)
    model.set_segment(B, F)
    model.set_section([B, D, F])

    model.set_segment(C, D)
    model.set_segment(D, G)
    model.set_segment(C, G)
    model.set_section([C, D, G])

    model.set_segment(D, E)

    model.set_polygon([D, B, E])
    model.set_polygon([D, C, E])

    return model


if __name__ == "__main__":
    construct_0054_g1()
