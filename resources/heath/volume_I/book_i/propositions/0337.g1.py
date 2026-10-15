"""Programmatic construction for Book I, I.33 (0337.g1).

The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0337_g1() -> Model:
    """Construct the figure for 0337.g1 (I.33) using geometor.model."""
    model = Model("0337.g1")

    # 1. Points
    A = model.set_point(34, -15.5, classes=["given"], label="A")
    B = model.set_point(199, -15.5, classes=["given"], label="B")
    C = model.set_point(13, -113.5, classes=["given"], label="C")
    D = model.set_point(178, -113.5, classes=["given"], label="D")

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(B, C)

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C])
    model.set_polygon([D, C, B])
    model.set_polygon([A, C, D, B])

    # 6. Angles (Wedges)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, B, B, D)
    model.set_wedge(C, A, A, B)
    model.set_wedge(B, C, C, D)

    return model


if __name__ == "__main__":
    construct_0337_g1()
