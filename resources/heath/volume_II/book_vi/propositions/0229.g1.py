"""Programmatic construction for Book VI, Proposition 16 / Simson Prop. B (0229.g1).

General theorem (internal lines AD, AE within angle BAC).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0229_g1() -> Model:
    """Construct the figure for 0229.g1 using geometor.model."""
    model = Model("0229.g1")

    # 1. Points
    O = model.set_point(110.0, -119.0, label="O")
    A = model.set_point(66.29, -63.05, classes=["given"], label="A")
    B = model.set_point(42.10, -98.24, classes=["given"], label="B")
    C = model.set_point(177.90, -98.24, classes=["given"], label="C")
    D = model.set_point(64.44, -98.24, classes=["given"], label="D")
    E = model.set_point(159.32, -170.07, classes=["given"], label="E")

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
    model.set_segment(C, E)

    # 4. Collinear Sections
    model.set_section([B, D, C])

    # 5. Polygons (Triangles)
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([A, E, C])

    # 6. Angles / Wedges
    model.set_wedge(A, D, D, B)
    model.set_wedge(A, C, C, E)
    model.set_wedge(A, C, C, B)
    model.set_wedge(B, A, A, D)
    model.set_wedge(E, A, A, C)

    return model


if __name__ == "__main__":
    construct_0229_g1()
