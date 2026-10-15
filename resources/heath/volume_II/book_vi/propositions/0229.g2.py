"""Programmatic construction for Book VI, Proposition 16 / Simson Prop. B (0229.g2).

General theorem (external lines AD, AE without angle BAC).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0229_g2() -> Model:
    """Construct the figure for 0229.g2 using geometor.model."""
    model = Model("0229.g2")

    # 1. Points
    O = model.set_point(114.0, -99.0, label="O")
    A = model.set_point(95.62, -30.42, classes=["given"], label="A")
    B = model.set_point(49.14, -127.88, classes=["given"], label="B")
    C = model.set_point(178.86, -127.88, classes=["given"], label="C")
    D = model.set_point(19.00, -127.88, classes=["given"], label="D")
    E = model.set_point(184.61, -91.58, classes=["given"], label="E")

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
    model.set_section([D, B, C])

    # 5. Polygons (Triangles)
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([A, E, C])

    # 6. Angles / Wedges
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, E, E, C)
    model.set_wedge(A, C, C, B)
    model.set_wedge(B, D, D, A)
    model.set_wedge(E, C, C, A)

    return model


if __name__ == "__main__":
    construct_0229_g2()
