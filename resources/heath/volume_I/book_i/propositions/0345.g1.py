"""Programmatic construction for Book I, I.36 (0345.g1).

Parallelograms which are on equal bases and in the same parallels are equal to one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0345_g1() -> Model:
    """Construct the figure for 0345.g1 (I.36) using geometor.model."""
    model = Model("0345.g1")

    # 1. Points
    A = model.set_point(60, -29, classes=["given"], label="A")
    D = model.set_point(141, -29, classes=["given"], label="D")
    E = model.set_point(212, -29, classes=["given"], label="E")
    H = model.set_point(293, -29, classes=["given"], label="H")
    B = model.set_point(54, -121, classes=["given"], label="B")
    C = model.set_point(135, -121, classes=["given"], label="C")
    F = model.set_point(246, -121, classes=["given"], label="F")
    G = model.set_point(327, -121, classes=["given"], label="G")

    # 3. Segments
    model.set_segment(A, H)
    model.set_segment(A, D)
    model.set_segment(D, E)
    model.set_segment(E, H)
    model.set_segment(B, G)
    model.set_segment(B, C)
    model.set_segment(C, F)
    model.set_segment(F, G)
    model.set_segment(A, B)
    model.set_segment(D, C)
    model.set_segment(E, F)
    model.set_segment(H, G)
    model.set_segment(B, E)
    model.set_segment(C, H)

    # 4. Collinear Sections
    model.set_section([A, D, E])
    model.set_section([D, E, H])
    model.set_section([B, C, F])
    model.set_section([C, F, G])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C, D])
    model.set_polygon([E, F, G, H])
    model.set_polygon([E, B, C, H])

    return model


if __name__ == "__main__":
    construct_0345_g1()
