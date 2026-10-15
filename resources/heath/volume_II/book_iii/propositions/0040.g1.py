"""Programmatic construction for Book III, Proposition 13 Simson Commentary (0040.g1).

Simson's proof that a circle EBF cannot touch a circle ABC internally at two points B, D:
chord BD is bisected at right angles by line GH passing through the centres.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0040_g1() -> Model:
    """Construct the figure 0040.g1 using geometor.model."""
    model = Model("0040.g1")

    # Outer circle ABC with centre O and horizontal diameter GH
    O = model.set_point(0, 0, classes=["auxiliary"])
    G = model.set_point(-71, 0, label="G")
    H = model.set_point(71, 0, label="H")
    model.construct_circle(O, H)
    model.construct_line(G, H)

    # Points B and D of supposed double internal contact
    y_BD = sp.sqrt(71**2 - 56**2)
    B = model.set_point(-56, y_BD, label="B")
    D = model.set_point(-56, -y_BD, label="D")
    M = model.set_point(-56, 0, classes=["auxiliary"], label="M")

    # Circumference points A, C on outer circle and E, F on inner circle
    A = model.set_point(55, 45, label="A")
    C = model.set_point(55, -45, label="C")
    O_inner = model.set_point(-18, 0, classes=["auxiliary"])
    E = model.set_point(32, 38, label="E")
    F = model.set_point(32, -38, label="F")
    model.construct_circle(O_inner, B)

    # Chord BD and perpendicular bisector GH
    model.set_segment(B, M)
    model.set_segment(M, D)
    model.set_segment(B, D)
    model.set_segment(G, M)
    model.set_segment(M, H)
    model.set_segment(G, H)

    return model


if __name__ == "__main__":
    construct_0040_g1()
