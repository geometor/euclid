"""Programmatic construction for Book VI, Proposition 8 (0216.g1).

If in a right-angled triangle a perpendicular be drawn from the right angle
to the base, the triangles adjoining the perpendicular are similar both to
the whole and to one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0216_g1() -> Model:
    """Construct the figure for 0216.g1 (VI.8) using geometor.model."""
    model = Model("0216.g1")

    # 1. Points
    A = model.set_point(131.0, -28.0, classes=["given"], label="A")
    B = model.set_point(19.0, -118.0, classes=["given"], label="B")
    C = model.set_point(203.0, -118.0, classes=["given"], label="C")
    D = model.set_point(131.0, -118.0, label="D")

    # 2. Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(A, D)

    # 3. Collinear Sections
    model.set_section([B, D, C])

    # 4. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])

    # 5. Angles / Wedges
    model.set_wedge(A, B, B, C)
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, D, D, C)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, A, A, B)
    model.set_wedge(D, A, A, B)
    model.set_wedge(D, A, A, C)

    return model


if __name__ == "__main__":
    construct_0216_g1()
