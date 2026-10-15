"""Programmatic construction for Book II, Proposition 12 (0418.g1).

In obtuse-angled triangles the square on the side subtending the obtuse angle
is greater than the squares on the sides containing the obtuse angle by twice
the rectangle contained by one of the sides about the obtuse angle, namely that
on which the perpendicular falls, and the straight line cut off outside by the
perpendicular towards the obtuse angle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0418_g1() -> Model:
    """Construct the figure for Book II, Proposition 12 using geometor.model."""
    model = Model("0418.g1")

    # Obtuse-angled triangle ABC with angle BAC obtuse, CA produced to D,
    # and BD perpendicular to CD.
    D = model.set_point(0, 0, label="D")
    A = model.set_point(3, 0, classes=["given"], label="A")
    C = model.set_point(7, 0, classes=["given"], label="C")
    B = model.set_point(0, 4, classes=["given"], label="B")

    # Line CA produced
    model.construct_line(C, A)

    # Segments
    model.set_segment(B, D)
    model.set_segment(D, A)
    model.set_segment(A, C)
    model.set_segment(D, C)
    model.set_segment(B, A)
    model.set_segment(B, C)

    # Collinear section D-A-C
    model.set_section([D, A, C])

    # Triangles
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([C, B, D])

    # Angles (obtuse angle BAC and right angle CDB)
    model.set_wedge(A, B, B, C)
    model.set_wedge(D, C, C, B)

    return model


if __name__ == "__main__":
    construct_0418_g1()
