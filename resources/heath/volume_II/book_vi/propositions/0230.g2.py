"""Programmatic construction for Book VI, Proposition C, External Altitude (0230.g2).

Perpendicular AD drawn from vertex A of triangle ABC to base BC produced, and
diameter AE of the circumscribed circle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0230_g2() -> Model:
    """Construct the figure for 0230.g2 using geometor.model."""
    model = Model("0230.g2")

    # 1. Points
    O = model.set_point(87.0, -108.0, label="O")
    A = model.set_point(146.85, -103.81, classes=["given"], label="A")
    B = model.set_point(42.41, -148.15, classes=["given"], label="B")
    C = model.set_point(131.59, -148.15, classes=["given"], label="C")
    D = model.set_point(146.85, -148.15, classes=["given"], label="D")
    E = model.set_point(27.15, -103.81, classes=["given"], label="E")

    # 2. Circumscribed Circle
    model.construct_circle(O, A)

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(B, D)
    model.set_segment(A, D)
    model.set_segment(A, E)
    model.set_segment(E, C)

    # 4. Collinear Sections
    model.set_section([B, C, D])

    # 5. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, C, D])
    model.set_polygon([A, E, C])

    # 6. Angles / Wedges
    model.set_wedge(D, B, B, A)
    model.set_wedge(C, E, E, A)
    model.set_wedge(B, A, A, D)
    model.set_wedge(E, A, A, C)

    return model


if __name__ == "__main__":
    construct_0230_g2()
