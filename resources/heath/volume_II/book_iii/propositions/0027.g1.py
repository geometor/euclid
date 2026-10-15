"""Programmatic construction for Book III, Proposition 9 (0027.g1).

If a point D be taken within a circle ABC, and more than two equal straight
lines DA, DB, DC fall from D on the circle, the point D is the centre of the
circle ABC (proved via perpendicular bisectors GK of AB and HL of BC).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0027_g1() -> Model:
    """Construct the figure 0027.g1 for Book III, Proposition 9."""
    model = Model("0027.g1")

    # Circle ABC with centre D at origin and horizontal diameter KG
    D = model.set_point(0, 0, classes=["given"], label="D")
    G = model.set_point(1, 0, label="G")
    K = model.set_point(-1, 0, label="K")

    model.construct_line(K, G)
    model.construct_circle(D, G)

    # Vertical chord AB bisected perpendicularly at E(-3/4, 0) by KG
    E = model.set_point(sp.Rational(-3, 4), 0, label="E")
    B = model.set_point(sp.Rational(-3, 4), sp.sqrt(7) / 4, classes=["given"], label="B")
    A = model.set_point(sp.Rational(-3, 4), -sp.sqrt(7) / 4, classes=["given"], label="A")
    model.construct_line(A, B)

    # Point C on circumference just above G
    C = model.set_point(sp.Rational(199, 200), sp.sqrt(399) / 200, classes=["given"], label="C")
    model.construct_line(B, C)

    # Midpoint F of BC and perpendicular bisector diameter HL through D and F
    F = model.set_point((B.x + C.x) / 2, (B.y + C.y) / 2, label="F")
    model.construct_line(D, F)
    len_DF = sp.sqrt(F.x**2 + F.y**2)
    L = model.set_point(F.x / len_DF, F.y / len_DF, label="L")
    H = model.set_point(-F.x / len_DF, -F.y / len_DF, label="H")

    # Equal straight lines DA, DB, DC
    model.set_segment(D, A)
    model.set_segment(D, B)
    model.set_segment(D, C)

    # Chord AB and sub-segments AE, EB
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(A, B)
    model.set_section([A, E, B])

    # Chord BC and sub-segments BF, FC
    model.set_segment(B, F)
    model.set_segment(F, C)
    model.set_segment(B, C)
    model.set_section([B, F, C])

    # Diameter KG and sub-segments KE, ED, DG
    model.set_segment(K, E)
    model.set_segment(E, D)
    model.set_segment(D, G)
    model.set_segment(K, D)
    model.set_segment(E, G)
    model.set_segment(K, G)

    # Diameter HL and sub-segments HD, DF, FL
    model.set_segment(H, D)
    model.set_segment(D, F)
    model.set_segment(F, L)
    model.set_segment(H, F)
    model.set_segment(D, L)
    model.set_segment(H, L)

    # Triangles AED and BED
    model.set_polygon([A, E, D])
    model.set_polygon([B, E, D])

    return model


if __name__ == "__main__":
    construct_0027_g1()
