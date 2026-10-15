"""Programmatic construction for Book XI, Proposition 23 Figure 2 (0319.g2).

Construct triangle LMN inscribed in circle (O, L), with auxiliary points P on OL
and Q on OM (PQ parallel to LM), and apex R above the plane of circle LMN such
that OR is perpendicular to the plane and RL = RM = RN = AB.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0319_g2() -> Model:
    """Construct Figure 2 for Book XI, Proposition 23 using geometor.model."""
    model = Model("0319.g2")

    # Circumcenter O and vertices L, M, N on circle
    O = model.set_point(sp.Rational(110, 82), sp.Rational(-108, 82), classes=["given"], label="O")
    L = model.set_point(sp.Rational(79, 82), sp.Rational(-184, 82), classes=["given"], label="L")
    M = model.set_point(sp.Rational(38, 82), sp.Rational(-67, 82), classes=["given"], label="M")
    N = model.set_point(sp.Rational(192, 82), sp.Rational(-113, 82), classes=["given"], label="N")

    # Points P on OL and Q on OM such that PQ is parallel to LM
    P = model.set_point(sp.Rational(87, 82), sp.Rational(-165, 82), label="P")
    Q = model.set_point(sp.Rational(56, 82), sp.Rational(-77, 82), label="Q")

    # Apex R of the solid angle above O
    R = model.set_point(sp.Rational(146, 82), sp.Rational(-49, 82), label="R")

    # Circumcircle
    model.construct_circle(O, L)

    # Segments in the base plane
    model.set_segment(L, M)
    model.set_segment(M, N)
    model.set_segment(N, L)
    model.set_segment(L, O)
    model.set_segment(M, O)
    model.set_segment(N, O)
    model.set_segment(O, P)
    model.set_segment(O, Q)
    model.set_segment(L, P)
    model.set_segment(Q, M)
    model.set_segment(P, Q)

    # Segments to apex R
    model.set_segment(O, R)
    model.set_segment(R, L)
    model.set_segment(R, M)
    model.set_segment(R, N)

    # Polygons (Triangles)
    model.set_polygon([L, M, N])
    model.set_polygon([L, O, M])
    model.set_polygon([M, O, N])
    model.set_polygon([N, O, L])
    model.set_polygon([P, Q, O])
    model.set_polygon([L, R, M])
    model.set_polygon([M, R, N])
    model.set_polygon([L, R, N])
    model.set_polygon([L, O, R])

    # Angles
    model.set_wedge(O, L, L, M)
    model.set_wedge(O, M, M, N)
    model.set_wedge(O, N, N, L)
    model.set_wedge(O, P, P, Q)
    model.set_wedge(O, L, L, R)
    model.set_wedge(R, L, L, M)
    model.set_wedge(R, M, M, N)
    model.set_wedge(R, L, L, N)

    return model


if __name__ == "__main__":
    construct_0319_g2()
