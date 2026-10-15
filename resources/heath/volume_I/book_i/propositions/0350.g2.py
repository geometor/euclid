"""Programmatic construction for Book I, I.39 (0350.g2).

Equal triangles which are on the same base and on the same side are also in the same parallels.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0350_g2() -> Model:
    """Construct the figure for 0350.g2 (I.39) using geometor.model."""
    model = Model("0350.g2")

    # 1. Points
    A = model.set_point(54, -35, classes=["given"], label="A")
    B = model.set_point(34, -110, classes=["given"], label="B")
    C = model.set_point(178, -110, classes=["given"], label="C")
    D = model.set_point(144, -35, classes=["given"], label="D")
    E = model.set_point(125, -45, label="E")

    # 3. Segments
    model.set_segment(B, C)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(B, D)
    model.set_segment(B, E)
    model.set_segment(E, D)
    model.set_segment(C, D)
    model.set_segment(A, E)
    model.set_segment(E, C)

    # 4. Collinear Sections
    model.set_section([B, E, D])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C])
    model.set_polygon([D, B, C])
    model.set_polygon([E, B, C])

    return model


if __name__ == "__main__":
    construct_0350_g2()
