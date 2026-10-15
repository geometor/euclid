"""Programmatic construction for Book VI, Proposition 32 Commentary (0279.g1).

Simson's similar and similarly situated parallelograms ABCF, CDEG placed with
vertically opposite angles at C so that diagonals AC, CE are in a straight line.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0279_g1() -> Model:
    """Construct the figure for 0279.g1 (VI.32 commentary) using geometor.model."""
    model = Model("0279.g1")

    # 1. Points
    A = model.set_point(24.0, -51.0, classes=["given"], label="A")
    F = model.set_point(85.0, -51.0, classes=["given"], label="F")
    B = model.set_point(41.0, -102.0, classes=["given"], label="B")
    C = model.set_point(102.0, -102.0, classes=["given"], label="C")
    G = model.set_point(189.0, -102.0, classes=["given"], label="G")
    D = model.set_point(126.0, -173.0, classes=["given"], label="D")
    E = model.set_point(213.0, -173.0, classes=["given"], label="E")

    # 2. Construction Lines
    model.construct_line(B, G)
    model.construct_line(F, D)
    model.construct_line(A, E)

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, F)
    model.set_segment(F, A)
    model.set_segment(A, C)

    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, G)
    model.set_segment(G, C)
    model.set_segment(C, E)

    model.set_segment(B, G)
    model.set_segment(D, F)
    model.set_segment(A, E)

    # 4. Collinear Sections
    model.set_section([B, C, G])
    model.set_section([D, C, F])
    model.set_section([A, C, E])

    # 5. Polygons (Parallelograms and Triangles)
    model.set_polygon([A, B, C, F])
    model.set_polygon([C, D, E, G])
    model.set_polygon([A, B, C])
    model.set_polygon([C, D, E])

    return model


if __name__ == "__main__":
    construct_0279_g1()
