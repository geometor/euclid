"""Programmatic construction for Book XI, Proposition 21 Trihedral Equality (0315.g1).

Two trihedral angles V-ABC and V'-A'B'C' are equal if the three face angles of
the one are respectively equal to the three face angles of the other, arranged
in the same order.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0315_g1() -> Model:
    """Construct the trihedral equality figure for Book XI, Proposition 21 using geometor.model."""
    model = Model("0315.g1")

    # Left trihedral angle V-ABC
    V = model.set_point(0, 1, classes=["given"], label="V")
    D = model.set_point(sp.Rational(-53, 100), sp.Rational(70, 100), label="D")
    A = model.set_point(sp.Rational(-101, 100), sp.Rational(42, 100), classes=["given"], label="A")
    E = model.set_point(sp.Rational(-42, 100), sp.Rational(21, 100), label="E")
    F = model.set_point(sp.Rational(-4, 100), sp.Rational(41, 100), label="F")
    B = model.set_point(sp.Rational(44, 100), sp.Rational(-9, 100), classes=["given"], label="B")
    C = model.set_point(sp.Rational(102, 100), sp.Rational(40, 100), classes=["given"], label="C")

    # Right trihedral angle V'-A'B'C'
    Vp = model.set_point(sp.Rational(250, 100), sp.Rational(97, 100), classes=["given"], label="V'")
    Dp = model.set_point(sp.Rational(200, 100), sp.Rational(69, 100), label="D'")
    Ap = model.set_point(sp.Rational(150, 100), sp.Rational(40, 100), classes=["given"], label="A'")
    Ep = model.set_point(sp.Rational(210, 100), sp.Rational(19, 100), label="E'")
    Fp = model.set_point(sp.Rational(246, 100), sp.Rational(39, 100), label="F'")
    Bp = model.set_point(sp.Rational(290, 100), sp.Rational(-10, 100), classes=["given"], label="B'")
    Cp = model.set_point(sp.Rational(346, 100), sp.Rational(39, 100), classes=["given"], label="C'")

    # Left segments and polygons
    model.set_segment(V, A)
    model.set_segment(V, D)
    model.set_segment(D, A)
    model.set_segment(V, B)
    model.set_segment(V, C)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(E, F)

    model.set_polygon([V, A, B])
    model.set_polygon([V, B, C])
    model.set_polygon([V, C, A])
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, E])
    model.set_polygon([A, D, F])
    model.set_polygon([A, E, F])
    model.set_polygon([D, E, F])

    # Right segments and polygons
    model.set_segment(Vp, Ap)
    model.set_segment(Vp, Dp)
    model.set_segment(Dp, Ap)
    model.set_segment(Vp, Bp)
    model.set_segment(Vp, Cp)
    model.set_segment(Ap, Bp)
    model.set_segment(Bp, Cp)
    model.set_segment(Cp, Ap)
    model.set_segment(Dp, Ep)
    model.set_segment(Dp, Fp)
    model.set_segment(Ep, Fp)

    model.set_polygon([Vp, Ap, Bp])
    model.set_polygon([Vp, Bp, Cp])
    model.set_polygon([Vp, Cp, Ap])
    model.set_polygon([Ap, Bp, Cp])
    model.set_polygon([Ap, Dp, Ep])
    model.set_polygon([Ap, Dp, Fp])
    model.set_polygon([Ap, Ep, Fp])
    model.set_polygon([Dp, Ep, Fp])

    return model


if __name__ == "__main__":
    construct_0315_g1()
