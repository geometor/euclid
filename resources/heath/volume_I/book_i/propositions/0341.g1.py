"""Programmatic construction for Book I, I.35 (0341.g1).

Parallelograms which are on the same base and in the same parallels are equal to one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0341_g1() -> Model:
    """Construct the figure for 0341.g1 (I.35) using geometor.model."""
    model = Model("0341.g1")

    # 1. Points
    A = model.set_point(30, -24.5, classes=["given"], label="A")
    D = model.set_point(123, -24.5, classes=["given"], label="D")
    E = model.set_point(145, -24.5, classes=["given"], label="E")
    F = model.set_point(238, -24.5, classes=["given"], label="F")
    G = model.set_point(127.2, -40.2, label="G")
    B = model.set_point(52, -106.5, classes=["given"], label="B")
    C = model.set_point(145, -106.5, classes=["given"], label="C")

    # 3. Segments
    model.set_segment(A, F)
    model.set_segment(A, D)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(A, E)
    model.set_segment(D, F)
    model.set_segment(B, C)
    model.set_segment(A, B)
    model.set_segment(D, C)
    model.set_segment(D, G)
    model.set_segment(G, C)
    model.set_segment(E, B)
    model.set_segment(E, G)
    model.set_segment(G, B)
    model.set_segment(F, C)

    # 4. Collinear Sections
    model.set_section([A, D, E])
    model.set_section([D, E, F])
    model.set_section([D, G, C])
    model.set_section([E, G, B])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C, D])
    model.set_polygon([E, B, C, F])
    model.set_polygon([E, A, B])
    model.set_polygon([F, D, C])
    model.set_polygon([D, G, E])
    model.set_polygon([G, B, C])
    model.set_polygon([A, B, G, D])
    model.set_polygon([E, G, C, F])
    model.set_polygon([A, B, C, F])
    model.set_polygon([E, B, C, D])

    # 6. Angles (Wedges)
    model.set_wedge(D, F, F, C)
    model.set_wedge(A, E, E, B)
    model.set_wedge(F, D, D, C)

    return model


if __name__ == "__main__":
    construct_0341_g1()
