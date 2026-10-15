"""Programmatic construction for Book II, Proposition 5 Note Figure (0397.g1).

Constructs the two parallel divided lines AB (bisected at C, cut unequally at D)
and A'D' (with C'B' = CD, C'D' = CB, and A'C' = C'B') comparing II. 5 and II. 6.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0397_g1() -> Model:
    """Construct the comparison lines for II. 5 and II. 6 on folio 0397."""
    model = Model("0397.g1")

    # Top line AB (bisected at C, cut at D)
    A = model.set_point(38.0, -35.5, classes=["given"], label="A")
    C = model.set_point(157.0, -35.5, classes=["given"], label="C")
    D = model.set_point(233.0, -35.5, classes=["given"], label="D")
    B = model.set_point(276.0, -35.5, classes=["given"], label="B")

    model.construct_line(A, B)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, D)
    model.set_segment(D, B)
    model.set_segment(A, D)
    model.set_segment(C, B)

    # Bottom line A'D' (A'B' bisected at C' and produced to D')
    Ap = model.set_point(81.0, -65.5, label="A'")
    Cp = model.set_point(157.0, -65.5, label="C'")
    Bp = model.set_point(233.0, -65.5, label="B'")
    Dp = model.set_point(276.0, -65.5, label="D'")

    model.construct_line(Ap, Dp)
    model.set_segment(Ap, Dp)
    model.set_segment(Ap, Cp)
    model.set_segment(Cp, Bp)
    model.set_segment(Bp, Dp)
    model.set_segment(Ap, Bp)
    model.set_segment(Cp, Dp)

    return model


if __name__ == "__main__":
    construct_0397_g1()
