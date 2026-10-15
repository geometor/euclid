"""Programmatic construction for Book VI, Proposition 5 (0209.g1).

Given triangle ABC in Proposition 5.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0209_g1() -> Model:
    """Construct the figure for 0209.g1 (VI.5) using geometor.model."""
    model = Model("0209.g1")

    # 1. Points
    A = model.set_point(131, -49, classes=["given"], label="A")
    B = model.set_point(26, -151, classes=["given"], label="B")
    C = model.set_point(103, -136, classes=["given"], label="C")

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)

    # 5. Polygons (Triangle)
    model.set_polygon([A, B, C])

    # 6. Angles (Wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, A, A, B)

    return model


if __name__ == "__main__":
    construct_0209_g1()
