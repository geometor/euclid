"""Programmatic construction for Book VI, Proposition 15 (0226.g1).

In equal triangles which have one angle equal to one angle the sides about the
equal angles are reciprocally proportional; and conversely.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0226_g1() -> Model:
    """Construct the figure for 0226.g1 (VI.15) using geometor.model."""
    model = Model("0226.g1")

    # 1. Points
    B = model.set_point(51.0, -30.0, classes=["given"], label="B")
    C = model.set_point(20.0, -152.0, classes=["given"], label="C")
    D = model.set_point(112.0, -48.0, classes=["given"], label="D")
    E = model.set_point(139.0, -185.0, classes=["given"], label="E")
    A = model.set_point(81.07, -82.96, classes=["given"], label="A")

    # 2. Construction Lines
    model.construct_line(C, D)
    model.construct_line(B, E)

    # 3. Segments
    model.set_segment(C, A)
    model.set_segment(A, D)
    model.set_segment(C, D)

    model.set_segment(B, A)
    model.set_segment(A, E)
    model.set_segment(B, E)

    model.set_segment(B, C)
    model.set_segment(D, E)
    model.set_segment(B, D)

    # 4. Collinear Sections
    model.set_section([C, A, D])
    model.set_section([B, A, E])

    # 5. Polygons (Triangles)
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, E])
    model.set_polygon([B, A, D])
    model.set_polygon([B, C, D])
    model.set_polygon([B, D, E])

    # 6. Angles / Wedges
    model.set_wedge(A, C, C, B)
    model.set_wedge(A, D, D, E)

    return model


if __name__ == "__main__":
    construct_0226_g1()
