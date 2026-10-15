"""Programmatic construction for Book VI, Proposition E (0233.g1).

Triangle ABC inscribed in a circle, with angle BAC bisected by AD meeting
BC in E and the circumscribed circle in D.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0233_g1() -> Model:
    """Construct the figure for 0233.g1 using geometor.model."""
    model = Model("0233.g1")

    # 1. Points
    O = model.set_point(92.0, -99.0, classes=["given"], label="O")
    A = model.set_point(127.68, -31.90, classes=["given"], label="A")
    B = model.set_point(28.99, -141.50, classes=["given"], label="B")
    C = model.set_point(155.01, -141.50, classes=["given"], label="C")
    D = model.set_point(92.0, -175.0, classes=["given"], label="D")
    E = model.set_point(100.35, -141.50, classes=["given"], label="E")

    # 2. Circle and Lines
    model.construct_circle(O, A)
    model.construct_line(B, C)
    model.construct_line(A, D)

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(B, E)
    model.set_segment(E, C)
    model.set_segment(A, D)
    model.set_segment(A, E)
    model.set_segment(E, D)
    model.set_segment(B, D)
    model.set_segment(D, C)

    # 4. Sections
    model.set_section([B, E, C])
    model.set_section([A, E, D])

    # 5. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, E, C])
    model.set_polygon([A, B, D, C])

    # 6. Angles / Wedges
    model.set_wedge(A, B, B, C)
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, D, D, C)
    model.set_wedge(D, A, A, B)
    model.set_wedge(C, A, A, E)

    return model


if __name__ == "__main__":
    construct_0233_g1()
