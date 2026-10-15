"""Programmatic construction for Book VI, Proposition C, Internal Altitude (0230.g3).

Perpendicular AD drawn from vertex A of triangle ABC to base BC, and diameter
AE of the circumscribed circle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0230_g3() -> Model:
    """Construct the figure for 0230.g3 using geometor.model."""
    model = Model("0230.g3")

    # 1. Points
    O = model.set_point(102.0, -84.0, label="O")
    A = model.set_point(122.18, -28.56, classes=["given"], label="A")
    B = model.set_point(45.29, -67.74, classes=["given"], label="B")
    C = model.set_point(158.71, -67.74, classes=["given"], label="C")
    D = model.set_point(122.18, -67.74, classes=["given"], label="D")
    E = model.set_point(81.82, -139.44, classes=["given"], label="E")

    # 2. Circumscribed Circle
    model.construct_circle(O, A)

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(A, D)
    model.set_segment(A, E)
    model.set_segment(E, C)

    # 4. Collinear Sections
    model.set_section([B, D, C])

    # 5. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([A, E, C])

    # 6. Angles / Wedges
    model.set_wedge(D, B, B, A)
    model.set_wedge(C, E, E, A)
    model.set_wedge(B, A, A, D)
    model.set_wedge(E, A, A, C)

    return model


if __name__ == "__main__":
    construct_0230_g3()
