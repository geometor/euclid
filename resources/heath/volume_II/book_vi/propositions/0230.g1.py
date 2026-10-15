"""Programmatic construction for Book VI, Proposition 16 / Converse of Prop. B (0230.g1).

Converse of Simson's Prop. B: line AD from vertex A meeting base BC in D and
circumcircle in E.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0230_g1() -> Model:
    """Construct the figure for 0230.g1 using geometor.model."""
    model = Model("0230.g1")

    # 1. Points
    O = model.set_point(90.0, -99.0, label="O")
    A = model.set_point(87.52, -28.04, classes=["given"], label="A")
    B = model.set_point(27.31, -65.67, classes=["given"], label="B")
    C = model.set_point(152.69, -65.67, classes=["given"], label="C")
    D = model.set_point(78.84, -65.67, classes=["given"], label="D")
    E = model.set_point(56.67, -161.69, classes=["given"], label="E")

    # 2. Circumscribed Circle
    model.construct_circle(O, A)

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(A, D)
    model.set_segment(D, E)
    model.set_segment(A, E)
    model.set_segment(C, E)
    model.set_segment(B, E)

    # 4. Collinear Sections
    model.set_section([B, D, C])
    model.set_section([A, D, E])

    # 5. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([A, E, C])
    model.set_polygon([A, B, E, C])

    # 6. Angles / Wedges
    model.set_wedge(A, C, C, B)
    model.set_wedge(A, D, D, B)
    model.set_wedge(A, C, C, E)
    model.set_wedge(B, A, A, D)
    model.set_wedge(E, A, A, C)
    model.set_wedge(D, B, B, A)
    model.set_wedge(D, A, A, C)
    model.set_wedge(C, E, E, A)
    model.set_wedge(C, B, B, A)
    model.set_wedge(C, E, E, B)

    return model


if __name__ == "__main__":
    construct_0230_g1()
