"""Programmatic construction for Book II, Proposition 13 (0420.g1).

In acute-angled triangles the square on the side subtending the acute angle is
less than the squares on the sides containing the acute angle by twice the
rectangle contained by one of the sides about the acute angle, namely that on
which the perpendicular falls, and the straight line cut off within by the
perpendicular towards the acute angle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0420_g1() -> Model:
    """Construct the figure for Book II, Proposition 13 using geometor.model."""
    model = Model("0420.g1")

    # Acute-angled triangle ABC with AD perpendicular to BC
    B = model.set_point(0, 0, classes=["given"], label="B")
    D = model.set_point(5, 0, label="D")
    C = model.set_point(8, 0, classes=["given"], label="C")
    A = model.set_point(5, 6, classes=["given"], label="A")

    # Segments
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(A, D)
    model.set_segment(A, B)
    model.set_segment(A, C)

    # Collinear section B-D-C
    model.set_section([B, D, C])

    # Triangles
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])

    # Angles (acute angle at B and right angle at D)
    model.set_wedge(B, C, C, A)
    model.set_wedge(D, C, C, A)

    return model


if __name__ == "__main__":
    construct_0420_g1()
