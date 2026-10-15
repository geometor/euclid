"""Programmatic construction for Book I, Definitions Commentary (0187.g2).

Frankland's illustration on the definition of a plane as the surface generated
by a straight line passing always through a fixed point O and intersecting a
fixed straight line X: rays OPP', OQQ' intersect X at P, Q, and for any third
point R on X, ray OR intersects P'Q' at R'.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0187_g2() -> Model:
    """Construct the plane projection diagram (0187.g2) using geometor.model."""
    model = Model("0187.g2")

    # 1. Fixed point O and points P, Q, R on the fixed straight line X
    O = model.set_point(18, 24, classes=["given"], label="O")
    P = model.set_point(58, 64, classes=["given"], label="P")
    Q = model.set_point(78, 54, classes=["given"], label="Q")
    R = model.set_point(68, 59, classes=["given"], label="R")
    X = model.set_point(128, 29, classes=["given"], label="X")

    line_X = model.construct_line(P, Q)
    model.set_section([P, R, Q])
    model.set_segment(P, R)
    model.set_segment(R, Q)
    model.set_segment(P, Q)
    model.set_segment(P, X)

    # 2. Rays OPP', OQQ' from O through P, Q and transversal P'Q'
    P_prime = model.set_point(86, 92, classes=["given"], label="P'")
    Q_prime = model.set_point(106, 68, classes=["given"], label="Q'")

    line_OP = model.construct_line(O, P)
    line_OQ = model.construct_line(O, Q)
    line_OR = model.construct_line(O, R)
    line_Pprime_Qprime = model.construct_line(P_prime, Q_prime)

    # 3. Intersection R' of OR with P'Q'
    R_prime = model.set_point(sp.Rational(1838, 19), sp.Rational(1504, 19), label="R'")

    # Collinear sections and sub-segments along rays and transversal P'Q'
    model.set_section([O, P, P_prime])
    model.set_segment(O, P)
    model.set_segment(P, P_prime)
    model.set_segment(O, P_prime)

    model.set_section([O, R, R_prime])
    model.set_segment(O, R)
    model.set_segment(R, R_prime)
    model.set_segment(O, R_prime)

    model.set_section([O, Q, Q_prime])
    model.set_segment(O, Q)
    model.set_segment(Q, Q_prime)
    model.set_segment(O, Q_prime)

    model.set_section([P_prime, R_prime, Q_prime])
    model.set_segment(P_prime, R_prime)
    model.set_segment(R_prime, Q_prime)
    model.set_segment(P_prime, Q_prime)

    return model


if __name__ == "__main__":
    construct_0187_g2()
