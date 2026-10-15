"""Programmatic construction for Book I, I.46 (0362.g1).

Proclus' proof that if two squares are equal, the straight lines are equal on which they are described.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0362_g1() -> Model:
    """Construct the figure for 0362.g1 (I.46) using geometor.model."""
    model = Model("0362.g1")

    # 1. Points
    D = model.set_point(24, -24, classes=["given"], label="D")
    F = model.set_point(114, -24, classes=["given"], label="F")
    A = model.set_point(24, -114, classes=["given"], label="A")
    B = model.set_point(114, -114, classes=["given"], label="B")
    C = model.set_point(204, -114, classes=["given"], label="C")
    G = model.set_point(114, -204, classes=["given"], label="G")
    E = model.set_point(204, -204, classes=["given"], label="E")

    # 3. Segments
    model.set_segment(D, F)
    model.set_segment(D, A)
    model.set_segment(A, B)
    model.set_segment(F, B)
    model.set_segment(B, C)
    model.set_segment(B, G)
    model.set_segment(C, E)
    model.set_segment(G, E)
    model.set_segment(A, C)
    model.set_segment(F, G)
    model.set_segment(A, F)
    model.set_segment(F, C)
    model.set_segment(C, G)
    model.set_segment(G, A)

    # 4. Collinear Sections
    model.set_section([A, B, C])
    model.set_section([F, B, G])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, D, F, B])
    model.set_polygon([B, C, E, G])
    model.set_polygon([A, F, C, G])
    model.set_polygon([A, B, F])
    model.set_polygon([C, B, G])
    model.set_polygon([F, B, C])
    model.set_polygon([A, F, C])
    model.set_polygon([G, F, C])

    return model


if __name__ == "__main__":
    construct_0362_g1()
