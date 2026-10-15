"""Programmatic construction for Book I, Definitions Commentary (0200.g1).

Saccheri's proof that a diameter MAN bisects a circle MDHNKM with center A:
turning the lower semicircle MNKM about M, N onto the upper semicircle MNHDM
shows that radii AK, AH, AD must be equal and MAN is the unique straight line
extending MA.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0200_g1() -> Model:
    """Construct Saccheri's circle bisection diagram (0200.g1)."""
    model = Model("0200.g1")

    # 1. Circle MDHNKM with center A and diameter MAN
    A = model.set_point(0, 0, classes=["given"], label="A")
    M = model.set_point(-1, 0, classes=["given"], label="M")
    N = model.set_point(1, 0, classes=["given"], label="N")

    circle_A = model.construct_circle(A, M)
    line_MN = model.construct_line(M, N)

    model.set_section([M, A, N])
    model.set_segment(M, A)
    model.set_segment(A, N)
    model.set_segment(M, N)

    # 2. Points D, H on upper semicircle NHDM and K on lower semicircle NKM
    x_D = -sp.Rational(4, 9)
    D = model.set_point(x_D, sp.sqrt(1 - x_D**2), label="D")

    x_H = sp.Rational(3, 4)
    H = model.set_point(x_H, sp.sqrt(1 - x_H**2), label="H")
    K = model.set_point(x_H, -sp.sqrt(1 - x_H**2), label="K")

    # 3. Radii AD, AH, AK
    model.set_segment(A, D)
    model.set_segment(A, H)
    model.set_segment(A, K)

    # Semicircular arcs NHDM (upper) and NKM (lower)
    model.set_wedge(A, M, N, M)
    model.set_wedge(A, M, M, N)

    return model


if __name__ == "__main__":
    construct_0200_g1()
