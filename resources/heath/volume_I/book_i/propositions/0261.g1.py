"""Programmatic construction for Book I, Proposition 4 (0261.g1).

If two triangles have the two sides equal to two sides respectively, and have
the angles contained by the equal straight lines equal, they will also have the
base equal to the base, the triangle will be equal to the triangle, and the
remaining angles will be equal to the remaining angles respectively, namely
those which the equal sides subtend.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0261_g1() -> Model:
    """Construct the figure for Book I, Proposition 4 using geometor.model."""
    model = Model("0261.g1")

    # 1. Let ABC, DEF be two triangles having AB = DE, AC = DF, and angle BAC = angle EDF.
    A = model.set_point(91, -23, classes=["given"], label="A")
    B = model.set_point(7, -111, classes=["given"], label="B")
    C = model.set_point(110, -111, classes=["given"], label="C")

    D = model.set_point(256, -23, classes=["given"], label="D")
    E = model.set_point(174, -111, classes=["given"], label="E")
    F = model.set_point(274, -111, classes=["given"], label="F")

    # Sides and bases of triangle ABC
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_polygon([A, B, C])

    # Sides and bases of triangle DEF
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(E, F)
    model.set_polygon([D, E, F])

    # Angles (wedges) of triangle ABC: < B A C ), < A B C ), < A C B )
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, A, A, B)

    # Angles (wedges) of triangle DEF: < E D F ), < D E F ), < D F E )
    model.set_wedge(D, E, E, F)
    model.set_wedge(E, D, D, F)
    model.set_wedge(F, D, D, E)

    return model


if __name__ == "__main__":
    construct_0261_g1()
