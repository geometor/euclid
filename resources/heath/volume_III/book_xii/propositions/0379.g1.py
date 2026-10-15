"""Programmatic construction for Book XII, Proposition 2 Commentary (0379.g1).

Similar polygons circumscribed about two circles with centers O and O',
corresponding tangent sides AB and A'B', and contact points C and C'.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0379_g1() -> Model:
    """Construct the figure 0379.g1 using geometor.model."""
    model = Model("0379.g1")

    # Left circle O (center (86, -94), radius 56)
    O = model.set_point(86.0, -94.0, classes=["given"], label="O")
    C = model.set_point(46.40, -54.40, label="C")
    A = model.set_point(71.86, -28.94, classes=["given"], label="A")
    B = model.set_point(20.94, -79.86, classes=["given"], label="B")
    D = model.set_point(132.0, -56.0, label="D")

    # Right circle O' (center (221, -102), radius 46)
    Op = model.set_point(221.0, -102.0, classes=["given"], label="O'")
    Cp = model.set_point(188.47, -69.47, label="C'")
    Ap = model.set_point(209.38, -48.56, classes=["given"], label="A'")
    Bp = model.set_point(167.56, -90.38, classes=["given"], label="B'")
    Dp = model.set_point(258.8, -70.8, label="D'")

    # Circles
    model.construct_circle(O, C)
    model.construct_circle(Op, Cp)

    # Segments
    for p1, p2 in [
        (A, B), (A, C), (C, B), (O, A), (O, B), (O, C), (A, D),
        (Ap, Bp), (Ap, Cp), (Cp, Bp), (Op, Ap), (Op, Bp), (Op, Cp), (Ap, Dp),
    ]:
        model.set_segment(p1, p2)

    # Triangles
    model.set_polygon([A, O, B])
    model.set_polygon([Ap, Op, Bp])

    # Angles
    model.set_wedge(A, O, O, B)
    model.set_wedge(Ap, Op, Op, Bp)
    model.set_wedge(B, A, A, O)
    model.set_wedge(Bp, Ap, Ap, Op)

    return model


if __name__ == "__main__":
    construct_0379_g1()
