"""Programmatic construction for Book VI, Proposition 7, Case 3 (0215.g1).

Simson's third case where one of the remaining angles is a right angle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0215_g1() -> Model:
    """Construct the figure for 0215.g1 (VI.7 Case 3) using geometor.model."""
    model = Model("0215.g1")

    # 1. Points (top configuration A, B, C, G; bottom configuration A2, B2, C2, G2; right D, E, F)
    A = model.set_point(115.0, -29.0, classes=["given"], label="A")
    B = model.set_point(19.0, -93.0, classes=["given"], label="B")
    C = model.set_point(115.0, -93.0, classes=["given"], label="C")
    G = model.set_point(115.0, -73.0, label="G")

    A2 = model.set_point(115.0, -125.0, classes=["given"], label="A'")
    B2 = model.set_point(19.0, -190.0, classes=["given"], label="B'")
    C2 = model.set_point(115.0, -190.0, classes=["given"], label="C'")
    G2 = model.set_point(115.0, -216.0, label="G'")

    D = model.set_point(272.0, -42.0, classes=["given"], label="D")
    E = model.set_point(153.0, -125.0, classes=["given"], label="E")
    F = model.set_point(272.0, -125.0, classes=["given"], label="F")

    # 2. Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, C)
    model.set_segment(A, G)
    model.set_segment(G, C)
    model.set_segment(B, G)

    model.set_segment(A2, B2)
    model.set_segment(B2, C2)
    model.set_segment(A2, C2)
    model.set_segment(C2, G2)
    model.set_segment(A2, G2)
    model.set_segment(B2, G2)

    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(D, F)

    # 3. Collinear Sections
    model.set_section([A, G, C])
    model.set_section([A2, C2, G2])

    # 4. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, G])
    model.set_polygon([B, G, C])
    model.set_polygon([A2, B2, C2])
    model.set_polygon([A2, B2, G2])
    model.set_polygon([B2, C2, G2])
    model.set_polygon([D, E, F])

    # 5. Angles / Wedges
    model.set_wedge(C, B, B, A)
    model.set_wedge(B, A, A, G)
    model.set_wedge(G, B, B, C)
    model.set_wedge(E, D, D, F)
    model.set_wedge(F, E, E, D)

    return model


if __name__ == "__main__":
    construct_0215_g1()
