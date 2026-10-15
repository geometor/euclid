"""Programmatic construction for Book VI, Proposition 3 (0202.g1).

If an angle of a triangle be bisected and the straight line cutting the angle cut the base also, the segments of the base will have the same ratio as the remaining sides of the triangle; and conversely.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0202_g1() -> Model:
    """Construct the figure for 0202.g1 (VI.3) using geometor.model."""
    model = Model("0202.g1")

    # 1. Points
    A = model.set_point(169, -71, classes=["given"], label="A")
    B = model.set_point(18, -160, classes=["given"], label="B")
    C = model.set_point(197, -160, classes=["given"], label="C")
    D = model.set_point(134.82, -160, classes=["given"], label="D")
    E = model.set_point(249.38, -23.62, label="E")

    # 2. Construction Lines
    model.construct_line(B, A)
    model.construct_line(C, E)

    # 3. Segments
    model.set_segment(B, A)
    model.set_segment(A, E)
    model.set_segment(B, E)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(B, C)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(C, E)

    # 4. Collinear Sections
    model.set_section([B, A, E])
    model.set_section([B, D, C])

    # 5. Polygons (Triangles)
    model.set_polygon([A, B, C])
    model.set_polygon([B, C, E])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([A, C, E])

    # 6. Angles (Wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, C, C, D)
    model.set_wedge(C, A, A, E)
    model.set_wedge(E, A, A, C)
    model.set_wedge(B, A, A, D)
    model.set_wedge(D, B, B, A)
    model.set_wedge(C, B, B, E)

    return model


if __name__ == "__main__":
    construct_0202_g1()
