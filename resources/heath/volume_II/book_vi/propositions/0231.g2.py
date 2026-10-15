"""Programmatic construction for Book VI, Proposition D, First Figure (0231.g2).

Ptolemy's theorem (Ptolemy's original figure where angle EBD is added).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0231_g2() -> Model:
    """Construct the figure for 0231.g2 using geometor.model."""
    model = Model("0231.g2")

    # 1. Points
    O = model.set_point(104.0, -114.0, label="O")
    A = model.set_point(57.16, -166.02, classes=["given"], label="A")
    B = model.set_point(60.90, -58.84, classes=["given"], label="B")
    C = model.set_point(163.36, -76.91, classes=["given"], label="C")
    D = model.set_point(166.92, -144.69, classes=["given"], label="D")
    E = model.set_point(97.52, -132.16, classes=["given"], label="E")

    # 2. Circumscribed Circle
    model.construct_circle(O, A)

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)

    model.set_segment(A, C)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(B, D)
    model.set_segment(B, E)

    # 4. Collinear Sections
    model.set_section([A, E, C])

    # 5. Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B, D])
    model.set_polygon([E, B, C])
    model.set_polygon([A, B, E])
    model.set_polygon([D, B, C])
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, C])

    # 6. Angles / Wedges
    model.set_wedge(B, E, E, A)
    model.set_wedge(B, D, D, E)
    model.set_wedge(B, C, C, D)
    model.set_wedge(B, D, D, A)
    model.set_wedge(B, C, C, E)
    model.set_wedge(D, A, A, B)
    model.set_wedge(D, B, B, C)
    model.set_wedge(C, E, E, B)
    model.set_wedge(A, B, B, E)

    return model


if __name__ == "__main__":
    construct_0231_g2()
