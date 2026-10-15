"""Programmatic construction for Book I, Definitions Commentary (0178.g1).

The Cissoid of Diocles: constructed via perpendicular diameters AC, BD in a
circle with center O, symmetric chords EG, FH perpendicular to CA, and the
intersection P of AE with FH.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0178_g1() -> Model:
    """Construct the Cissoid of Diocles diagram (0178.g1) using geometor.model."""
    model = Model("0178.g1")

    # 1. Circle with center O and perpendicular diameters AC (horizontal), BD (vertical)
    O = model.set_point(0, 0, classes=["given"], label="O")
    A = model.set_point(1, 0, classes=["given"], label="A")
    C = model.set_point(-1, 0, classes=["given"], label="C")
    D = model.set_point(0, 1, classes=["given"], label="D")
    B = model.set_point(0, -1, classes=["given"], label="B")

    circle_O = model.construct_circle(O, A)
    line_CA = model.construct_line(C, A)
    line_BD = model.construct_line(B, D)

    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(O, A)
    model.set_segment(O, B)
    model.set_segment(O, C)
    model.set_segment(O, D)

    # 2. Asymptote CK perpendicular to CA at C
    K = model.set_point(-1, -sp.Rational(8, 5), label="K")
    model.construct_line(K, C)
    model.set_segment(C, K)

    # 3. Points E, F on quadrants BC, BA such that arcs BE, BF are equal
    x_H = sp.Rational(2, 5)
    y_E = -sp.sqrt(1 - x_H**2)
    G = model.set_point(-x_H, 0, label="G")
    H = model.set_point(x_H, 0, label="H")
    E = model.set_point(-x_H, y_E, label="E")
    F = model.set_point(x_H, y_E, label="F")

    # Collinear sections along diameter CA (C - G - O - H - A)
    model.set_section([C, G, O])
    model.set_section([G, O, H])
    model.set_section([O, H, A])
    model.set_segment(C, G)
    model.set_segment(G, O)
    model.set_segment(O, H)
    model.set_segment(H, A)

    # 4. Perpendiculars EG, FH to CA, chord AE, and cissoid point P = AE ∩ FH
    model.construct_line(G, E)
    model.construct_line(H, F)
    model.construct_line(A, E)

    y_P = y_E * (1 - x_H) / (1 + x_H)
    P = model.set_point(x_H, y_P, label="P")

    model.set_segment(E, G)
    model.set_segment(F, H)
    model.set_segment(H, P)
    model.set_segment(P, F)
    model.set_segment(A, E)
    model.set_segment(A, P)
    model.set_segment(P, E)
    model.set_segment(A, B)
    model.set_segment(A, D)

    # 5. Quadrants and arcs referenced in the commentary
    model.set_wedge(O, B, B, C)
    model.set_wedge(O, B, B, A)
    model.set_wedge(O, B, B, E)
    model.set_wedge(O, B, B, F)

    return model


if __name__ == "__main__":
    construct_0178_g1()
