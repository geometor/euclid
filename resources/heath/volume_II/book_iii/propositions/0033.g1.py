"""Programmatic construction for Book III, Proposition 11 Note (0033.g1).

Two circles touching internally at A with centres F (outer) and G (inner),
common diameter CBA, and secant radius FPQ from F meeting the inner circle
at P and the outer circle at Q.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0033_g1() -> Model:
    """Construct the figure 0033.g1 using geometor.model."""
    model = Model("0033.g1")

    # Centre F of outer circle and point of internal contact A
    F = model.set_point(0, 0, classes=["given"], label="F")
    A = model.set_point(1, 0, classes=["given"], label="A")

    # Centre G of inner circle on segment FA
    G = model.set_point(sp.Rational(3, 8), 0, classes=["given"], label="G")

    # Common diameter line [ C A ]
    model.construct_line(F, A)

    # Outer circle ( F A ) with diameter CA, and inner circle ( G A ) with diameter BA
    model.construct_circle(F, A)
    model.construct_circle(G, A)

    C = model.set_point(-1, 0, label="C")
    B = model.set_point(sp.Rational(-1, 4), 0, label="B")

    # Radius FQ of the outer circle meeting inner circle at P and outer circle at Q
    Q = model.set_point(sp.Rational(12, 13), sp.Rational(-5, 13), label="Q")
    t_P = (sp.Rational(9, 13) + sp.sqrt(sp.Rational(81, 169) + 1)) / 2
    P = model.set_point(t_P * sp.Rational(12, 13), t_P * sp.Rational(-5, 13), label="P")

    # Collinear segments along diameter CBA
    model.set_segment(C, B)
    model.set_segment(B, F)
    model.set_segment(F, G)
    model.set_segment(G, A)
    model.set_segment(C, F)
    model.set_segment(F, A)
    model.set_segment(B, A)
    model.set_segment(C, A)
    model.set_section([C, B, A])

    # Secant radius FPQ segments
    model.set_segment(F, P)
    model.set_segment(P, Q)
    model.set_segment(F, Q)
    model.set_section([F, P, Q])

    return model


if __name__ == "__main__":
    construct_0033_g1()
