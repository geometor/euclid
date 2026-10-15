"""Programmatic construction for Book VI, Proposition 7, Todhunter Alternative (0214.g1).

Todhunter's presentation of the ambiguous case for similar triangles.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0214_g1() -> Model:
    """Construct the figure for 0214.g1 (VI.7 Todhunter note) using geometor.model."""
    model = Model("0214.g1")

    # 1. Points
    A = model.set_point(110.0, -21.0, classes=["given"], label="A")
    B = model.set_point(19.0, -133.0, classes=["given"], label="B")
    C = model.set_point(142.0, -133.0, classes=["given"], label="C")
    G = model.set_point(121.52, -61.32, label="G")
    D = model.set_point(284.0, -38.0, classes=["given"], label="D")
    E = model.set_point(210.0, -132.0, classes=["given"], label="E")
    F = model.set_point(294.0, -73.0, classes=["given"], label="F")

    # 2. Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, C)
    model.set_segment(A, G)
    model.set_segment(G, C)
    model.set_segment(B, G)

    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(D, F)

    # 3. Collinear Sections
    model.set_section([A, G, C])

    # 4. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, G])
    model.set_polygon([B, G, C])
    model.set_polygon([D, E, F])

    # 5. Angles / Wedges
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, A, A, C)
    model.set_wedge(B, A, A, G)
    model.set_wedge(C, B, B, A)
    model.set_wedge(G, B, B, A)
    model.set_wedge(G, B, B, C)
    model.set_wedge(D, E, E, F)
    model.set_wedge(E, D, D, F)
    model.set_wedge(F, E, E, D)

    return model


if __name__ == "__main__":
    construct_0214_g1()
