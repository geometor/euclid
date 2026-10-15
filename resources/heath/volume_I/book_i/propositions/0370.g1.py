"""Programmatic construction for Proposition 47 Commentary (0370.g1).

Zeuthen's similar-rectangle grid verification for the (3, 4, 5) right-angled triangle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0370_g1() -> Model:
    """Construct Zeuthen's similar-rectangle grid figure (0370.g1) using geometor.model."""
    model = Model("0370.g1")

    A = model.set_point(108, -34, classes=["given"], label="A")
    B = model.set_point(26, -100, classes=["given"], label="B")
    C = model.set_point(154, -100, classes=["given"], label="C")
    D = model.set_point(108, -100, label="D")
    E = model.set_point(26, -34, label="E")
    F = model.set_point(154, -34, label="F")
    G = model.set_point(72, -166, label="G")

    # Polygons: triangles ABC, ABD, ADC, BGC and rectangles BCFE, BDAE, DCFA, BGCA
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([B, G, C])
    model.set_polygon([B, C, F, E])
    model.set_polygon([B, D, A, E])
    model.set_polygon([D, C, F, A])
    model.set_polygon([B, G, C, A])

    # Segments
    for p1, p2 in [
        (B, C), (B, D), (D, C),
        (A, B), (A, C), (A, D),
        (E, F), (E, A), (A, F), (E, B), (F, C),
        (B, G), (C, G),
    ]:
        model.set_segment(p1, p2)

    # Angles
    model.set_wedge(A, B, B, C)  # < B A C )
    model.set_wedge(D, A, A, B)  # < A D B )
    model.set_wedge(D, A, A, C)  # < A D C )

    return model


if __name__ == "__main__":
    construct_0370_g1()
