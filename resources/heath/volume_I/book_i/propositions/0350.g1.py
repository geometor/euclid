"""Programmatic construction for Book I, I.38 (0350.g1).

Heron's comparison of areas of triangles when F falls inside triangle DEG.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0350_g1() -> Model:
    """Construct the figure for 0350.g1 (I.38) using geometor.model."""
    model = Model("0350.g1")

    # 1. Points
    A = model.set_point(148, -38, classes=["given"], label="A")
    B = model.set_point(70, -126, classes=["given"], label="B")
    C = model.set_point(187, -126, classes=["given"], label="C")
    D = model.set_point(316, -36, classes=["given"], label="D")
    E = model.set_point(231, -125, classes=["given"], label="E")
    F = model.set_point(267, -125, classes=["given"], label="F")
    H = model.set_point(324, -55, label="H")
    G = model.set_point(352, -125, label="G")

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(D, E)
    model.set_segment(E, G)
    model.set_segment(E, F)
    model.set_segment(F, G)
    model.set_segment(D, G)
    model.set_segment(D, H)
    model.set_segment(H, G)
    model.set_segment(D, F)
    model.set_segment(F, H)
    model.set_segment(E, H)

    # 4. Collinear Sections
    model.set_section([E, F, G])
    model.set_section([D, H, G])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([D, E, H])
    model.set_polygon([D, E, G])

    return model


if __name__ == "__main__":
    construct_0350_g1()
