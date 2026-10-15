"""Programmatic construction for Book VI, Proposition 7 (0212.g1).

Case 1 of Proposition 7: two triangles with one angle equal, sides about other angles proportional, and remaining angles both less than a right angle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0212_g1() -> Model:
    """Construct the figure for 0212.g1 (VI.7) using geometor.model."""
    model = Model("0212.g1")

    # 1. Points
    A = model.set_point(62, -29, classes=["given"], label="A")
    B = model.set_point(28, -156, classes=["given"], label="B")
    C = model.set_point(147, -174, classes=["given"], label="C")
    G = model.set_point(137.65, -158.05, label="G")
    D = model.set_point(194, -26, classes=["given"], label="D")
    E = model.set_point(177, -94, classes=["given"], label="E")
    F = model.set_point(240, -105, classes=["given"], label="F")

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, G)
    model.set_segment(G, C)
    model.set_segment(A, C)
    model.set_segment(B, G)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, D)

    # 4. Collinear Sections
    model.set_section([A, G, C])

    # 5. Polygons (Triangles)
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, G])
    model.set_polygon([B, G, C])
    model.set_polygon([D, E, F])

    # 6. Angles (Wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, A, A, C)
    model.set_wedge(B, A, A, G)
    model.set_wedge(C, A, A, B)
    model.set_wedge(G, A, A, B)
    model.set_wedge(G, B, B, C)
    model.set_wedge(D, E, E, F)
    model.set_wedge(E, D, D, F)
    model.set_wedge(F, D, D, E)

    return model


if __name__ == "__main__":
    construct_0212_g1()
