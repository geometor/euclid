"""Programmatic construction for Book I, I.38 (0349.g2).

Heron's comparison of areas of triangles when the included angles are together greater than two right angles (Case 3).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0349_g2() -> Model:
    """Construct the figure for 0349.g2 (I.38) using geometor.model."""
    model = Model("0349.g2")

    # 1. Points
    A = model.set_point(151, -36, classes=["given"], label="A")
    B = model.set_point(43, -78.5, classes=["given"], label="B")
    C = model.set_point(209, -78.5, classes=["given"], label="C")
    D = model.set_point(357, -36, classes=["given"], label="D")
    E = model.set_point(246, -78.5, classes=["given"], label="E")
    F = model.set_point(366, -105, classes=["given"], label="F")
    G = model.set_point(400, -65, label="G")
    H = model.set_point(421, -78.5, label="H")

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(E, F)
    model.set_segment(D, H)
    model.set_segment(D, G)
    model.set_segment(G, H)
    model.set_segment(F, H)
    model.set_segment(E, H)
    model.set_segment(E, G)

    # 4. Collinear Sections
    model.set_section([D, G, H])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([D, E, H])
    model.set_polygon([D, E, G])

    # 6. Angles (Wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(D, E, E, F)
    model.set_wedge(H, D, D, F)
    model.set_wedge(F, D, D, H)

    return model


if __name__ == "__main__":
    construct_0349_g2()
