"""Programmatic construction for Serenus's Theorem on III.21 (0056.g3).

If ADB be any segment of a circle with midpoint C (AC = CB), and with C as
centre and radius CA or CB the circle AHB be described, then for any point D
on segment ACB with BD produced to meet the outer segment in E, AD + DB = BE.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0056_g3() -> Model:
    """Construct the figure for Serenus's theorem (0056.g3) using geometor.model."""
    model = Model("0056.g3")

    # 1. Base AB and midpoint C of segment ACB
    A = model.set_point(sp.Rational(-103, 200), sp.Rational(-18, 25), classes=["given"], label="A")
    B = model.set_point(sp.Rational(103, 200), sp.Rational(-18, 25), classes=["given"], label="B")
    C = model.set_point(0, 0, classes=["given"], label="C")
    F = model.set_point(sp.Rational(-103, 200), sp.Rational(18, 25), label="F")

    # 2. Outer circle AHB with centre C and radius CA = CB
    circle_AHB = model.construct_circle(C, A)

    # 3. Point D on inner segment ACB, BD produced to E, AD produced to H
    D = model.set_point(sp.Rational(-38, 100), sp.Rational(-15, 100), label="D")
    E = model.set_point(sp.Rational(-87, 100), sp.Rational(16, 100), label="E")
    H = model.set_point(sp.Rational(-11, 100), sp.Rational(88, 100), label="H")

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(C, F)
    model.set_segment(B, F)
    model.set_section([B, C, F])
    model.set_segment(F, A)

    model.set_segment(B, D)
    model.set_segment(D, E)
    model.set_segment(B, E)
    model.set_section([B, D, E])

    model.set_segment(A, D)
    model.set_segment(D, H)
    model.set_segment(A, H)
    model.set_section([A, D, H])

    model.set_segment(E, A)
    model.set_segment(H, B)

    model.set_polygon([A, C, F])
    model.set_polygon([A, D, E])
    model.set_polygon([A, C, B])
    model.set_polygon([A, D, B])

    return model


if __name__ == "__main__":
    construct_0056_g3()
