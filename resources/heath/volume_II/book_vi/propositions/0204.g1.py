"""Programmatic construction for Book VI, Proposition 3 Commentary (0204.g1).

Harmonic division and the Circle of Apollonius on diameter DE.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0204_g1() -> Model:
    """Construct the figure for 0204.g1 (VI.3 commentary) using geometor.model."""
    model = Model("0204.g1")

    # 1. Points
    A = model.set_point(132, -69, classes=["given"], label="A")
    B = model.set_point(19, -145, classes=["given"], label="B")
    C = model.set_point(160, -145, classes=["given"], label="C")
    D = model.set_point(107.41, -145, classes=["given"], label="D")
    E = model.set_point(366.94, -145, classes=["given"], label="E")
    F = model.set_point(188.43, -31.05, label="F")
    O = model.set_point(237.18, -145, label="O")

    # 2. Construction Lines & Circles
    model.construct_line(B, E)
    model.construct_line(B, F)
    model.construct_circle(O, D)

    # 3. Segments
    model.set_segment(B, A)
    model.set_segment(A, F)
    model.set_segment(B, F)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(C, E)
    model.set_segment(B, C)
    model.set_segment(D, E)
    model.set_segment(B, E)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(A, E)

    # 4. Collinear Sections
    model.set_section([B, A, F])
    model.set_section([B, D, C])
    model.set_section([D, C, E])
    model.set_section([B, C, E])

    # 5. Polygons (Triangles)
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([A, C, E])
    model.set_polygon([A, D, E])
    model.set_polygon([A, B, E])

    # 6. Angles (Wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, D, D, C)
    model.set_wedge(A, C, C, F)
    model.set_wedge(A, C, C, E)
    model.set_wedge(A, E, E, F)
    model.set_wedge(A, D, D, E)

    return model


if __name__ == "__main__":
    construct_0204_g1()
