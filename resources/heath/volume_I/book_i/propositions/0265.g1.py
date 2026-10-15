"""Programmatic construction for Book I, Proposition 5 (0265.g1).

In isosceles triangles the angles at the base are equal to one another,
and, if the equal straight lines be produced further, the angles under the
base will be equal to one another (Pons Asinorum).
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0265_g1() -> Model:
    """Construct the figure for Book I, Proposition 5 using geometor.model."""
    model = Model("0265.g1")

    # 1. Let ABC be an isosceles triangle having the side AB equal to the side AC.
    A = model.set_point(0, sp.Rational(43, 19), classes=["given"], label="A")
    B = model.set_point(-1, 0, classes=["given"], label="B")
    C = model.set_point(1, 0, classes=["given"], label="C")

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_polygon([A, B, C])

    # 2. Let the straight lines BD, CE be produced further in a straight line with AB, AC [Post. 2].
    line_AB = model.construct_line(A, B)
    line_AC = model.construct_line(A, C)

    # Outer endpoints D and E on the produced rays
    t_D = sp.Rational(153, 86)
    D = model.set_point(-t_D, sp.Rational(43, 19) * (1 - t_D), label="D")
    E = model.set_point(t_D, sp.Rational(43, 19) * (1 - t_D), label="E")

    # 3. Let a point F be taken at random on BD;
    #    from AE the greater let AG be cut off equal to AF the less [I. 3].
    t_F = sp.Rational(125, 86)
    F = model.set_point(-t_F, sp.Rational(43, 19) * (1 - t_F), label="F")
    G = model.set_point(t_F, sp.Rational(43, 19) * (1 - t_F), label="G")

    # Collinear sections and sub-segments along left ray ABD
    model.set_section([A, B, F])
    model.set_section([B, F, D])
    model.set_segment(B, F)
    model.set_segment(F, D)
    model.set_segment(A, F)
    model.set_segment(B, D)
    model.set_segment(A, D)

    # Collinear sections and sub-segments along right ray ACE
    model.set_section([A, C, G])
    model.set_section([C, G, E])
    model.set_segment(C, G)
    model.set_segment(G, E)
    model.set_segment(A, G)
    model.set_segment(C, E)
    model.set_segment(A, E)

    # 4. And let the straight lines FC, GB be joined [Post. 1].
    model.set_segment(F, C)
    model.set_segment(G, B)

    # 5. Triangles compared in the proof: AFC, AGB and BFC, CGB
    model.set_polygon([A, F, C])
    model.set_polygon([A, G, B])
    model.set_polygon([B, F, C])
    model.set_polygon([C, G, B])

    return model


if __name__ == "__main__":
    construct_0265_g1()
