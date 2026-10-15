"""Programmatic construction for Book I, Proposition 5 Note — Pappus' Proof (0268.g1).

Pappus' proof of I. 5 without auxiliary construction, conceiving the isosceles triangle
ABC as two triangles ABC and ACB.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0268_g1() -> Model:
    """Construct Pappus' isosceles triangle diagram (0268.g1) using geometor.model."""
    model = Model("0268.g1")

    # Let ABC be an isosceles triangle with AB equal to AC.
    A = model.set_point(0, sp.Rational(7, 3), classes=["given"], label="A")
    B = model.set_point(-1, 0, classes=["given"], label="B")
    C = model.set_point(1, 0, classes=["given"], label="C")

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_polygon([A, B, C])

    return model


if __name__ == "__main__":
    construct_0268_g1()
