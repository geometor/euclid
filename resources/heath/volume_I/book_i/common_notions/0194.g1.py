"""Programmatic construction for Book I, Definitions Commentary (0194.g1).

Veronese's definition of a cluster of straight lines, a cluster of rays, or a
plane: the figure given by all the straight lines joining the points of a
straight line r to a point P outside it and by the parallel r' to r through P.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0194_g1() -> Model:
    """Construct Veronese's cluster/plane diagram (0194.g1) using geometor.model."""
    model = Model("0194.g1")

    # 1. Straight line r (upper horizontal line [ R1 R2 ])
    R1 = model.set_point(11, 89, classes=["given"], label="R1")
    R2 = model.set_point(245, 89, classes=["given"], label="r")
    model.construct_line(R1, R2)
    model.set_segment(R1, R2)

    # 2. Point P outside r and the parallel r' to r through P (lower horizontal line [ P Q ])
    P1 = model.set_point(15, 25, classes=["given"], label="P1")
    P = model.set_point(72, 25, classes=["given"], label="P")
    Q = model.set_point(258, 25, classes=["given"], label="r'")
    model.construct_line(P, Q)
    model.set_section([P1, P, Q])
    model.set_segment(P1, P)
    model.set_segment(P, Q)
    model.set_segment(P1, Q)

    # 3. Ray PS from P toward a point on r
    S = model.set_point(190, 81, classes=["given"], label="S")
    model.construct_line(P, S)
    model.set_segment(P, S)

    # Plane strip polygon bounded by r and r'
    model.set_polygon([R1, R2, Q, P1])

    return model


if __name__ == "__main__":
    construct_0194_g1()
