"""Programmatic construction for Book XI, Proposition 23 Commentary Cases II & III (0324.g1).

Upper figure (Case II): Circumcenter O lies on side MN of triangle LMN.
Lower figure (Case III): Circumcenter O lies outside triangle LMN, with auxiliary
points P, Q, R on OL, OM, ON and S, T such that OS = OT = OP.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0324_g1() -> Model:
    """Construct Cases II and III figures for Book XI, Proposition 23 using geometor.model."""
    model = Model("0324.g1")

    # Case II (Upper figure: O on MN)
    O2 = model.set_point(sp.Rational(112, 82), sp.Rational(-68, 82), label="O2")
    M2 = model.set_point(sp.Rational(56, 82), sp.Rational(-68, 82), label="M2")
    N2 = model.set_point(sp.Rational(168, 82), sp.Rational(-68, 82), label="N2")
    L2 = model.set_point(sp.Rational(130, 82), sp.Rational(-15, 82), label="L2")

    model.construct_circle(O2, M2)
    model.set_segment(M2, N2)
    model.set_segment(M2, O2)
    model.set_segment(O2, N2)
    model.set_segment(L2, M2)
    model.set_segment(L2, N2)
    model.set_segment(L2, O2)
    model.set_polygon([L2, M2, N2])

    # Case III (Lower figure: O outside triangle LMN)
    O = model.set_point(sp.Rational(93, 82), sp.Rational(-412, 82), classes=["given"], label="O")
    L = model.set_point(sp.Rational(95, 82), sp.Rational(-330, 82), classes=["given"], label="L")
    M = model.set_point(sp.Rational(16, 82), sp.Rational(-384, 82), classes=["given"], label="M")
    N = model.set_point(sp.Rational(164, 82), sp.Rational(-371, 82), classes=["given"], label="N")

    P = model.set_point(sp.Rational(95, 82), sp.Rational(-349, 82), label="P")
    Q = model.set_point(sp.Rational(34, 82), sp.Rational(-390, 82), label="Q")
    R = model.set_point(sp.Rational(148, 82), sp.Rational(-380, 82), label="R")

    S = model.set_point(sp.Rational(30, 82), sp.Rational(-414, 82), label="S")
    T = model.set_point(sp.Rational(150, 82), sp.Rational(-386, 82), label="T")

    model.construct_circle(O, L)

    # Segments
    for u, v in [
        (L, M), (M, N), (N, L),
        (O, L), (O, M), (O, N),
        (O, P), (O, Q), (O, R),
        (P, Q), (Q, R), (P, R),
        (O, S), (O, T), (P, S), (P, T), (S, T),
    ]:
        model.set_segment(u, v)

    # Triangles
    for tri in [
        [L, M, N], [L, O, M], [N, O, L], [M, O, N],
        [P, O, Q], [P, O, S], [P, O, T], [S, P, T], [S, O, T],
    ]:
        model.set_polygon(tri)

    # Angles
    model.set_wedge(O, L, L, M)
    model.set_wedge(O, N, N, L)
    model.set_wedge(O, M, M, N)
    model.set_wedge(O, P, P, Q)
    model.set_wedge(O, P, P, S)
    model.set_wedge(O, P, P, T)
    model.set_wedge(O, S, S, T)
    model.set_wedge(L, M, M, N)
    model.set_wedge(P, S, S, T)

    return model


if __name__ == "__main__":
    construct_0324_g1()
