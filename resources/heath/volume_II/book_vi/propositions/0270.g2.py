"""Programmatic construction for Book VI, Proposition 28 Commentary (0270.g2).

Data Proposition 85: application of a parallelogram falling short by a rhombus with a given angle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0270_g2() -> Model:
    """Construct the figure for 0270.g2 (VI.28 commentary / Data Prop. 85) using geometor.model."""
    model = Model("0270.g2")

    # 1. Points
    E = model.set_point(50, -29, label="E")
    A = model.set_point(123, -29, classes=["given"], label="A")
    C1 = model.set_point(228, -29, label="C1")

    D = model.set_point(19, -95, label="D")
    B = model.set_point(92, -95, classes=["given"], label="B")
    C = model.set_point(197, -95, classes=["given"], label="C")

    # 2. Construction Lines
    model.construct_line(C, B)

    # 3. Segments
    model.set_segment(E, A)
    model.set_segment(A, C1)
    model.set_segment(E, C1)

    model.set_segment(D, B)
    model.set_segment(B, C)
    model.set_segment(D, C)

    model.set_segment(E, D)
    model.set_segment(A, B)
    model.set_segment(C1, C)

    # 4. Collinear Sections
    model.set_section([D, B, C])
    model.set_section([E, A, C1])

    # 5. Polygons (Parallelogram AC and Rhombus AD)
    model.set_polygon([A, B, C, C1])  # AC
    model.set_polygon([E, D, B, A])  # AD
    model.set_polygon([E, D, C, C1])  # EC

    # 6. Angles (Wedges)
    model.set_wedge(B, A, A, C)  # ABC
    model.set_wedge(D, E, E, B)  # EDB

    return model


if __name__ == "__main__":
    construct_0270_g2()
