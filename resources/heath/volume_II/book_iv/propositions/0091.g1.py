"""Programmatic construction for Book IV, Proposition 4 (0091.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0091_g1() -> Model:
    """Construct the figure 0091.g1 using geometor.model."""
    model = Model("0091.g1")

    # Points (y-inverted for standard mathematical coordinates)
    A = model.set_point(178.00, -28.00, classes=["given"], label="A")
    B = model.set_point(24.00, -159.00, classes=["given"], label="B")
    C = model.set_point(236.00, -159.00, classes=["given"], label="C")
    D = model.set_point(159.46, -109.18, label="D")
    E = model.set_point(127.18, -71.23, label="E")
    F = model.set_point(159.46, -159.00, label="F")
    G = model.set_point(205.01, -89.01, label="G")

    # Inscribed circle EFG
    model.construct_circle(D, E)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(B, F)
    model.set_segment(F, C)
    model.set_segment(C, G)
    model.set_segment(G, A)
    model.set_segment(B, D)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(D, G)

    # Collinear sections
    model.set_section([A, E, B])
    model.set_section([B, F, C])
    model.set_section([C, G, A])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([E, B, D])
    model.set_polygon([F, B, D])

    # Angles (wedges)
    model.set_wedge(B, A, A, C)
    model.set_wedge(B, A, A, D)
    model.set_wedge(B, C, C, D)
    model.set_wedge(C, A, A, B)
    model.set_wedge(C, D, D, B)
    model.set_wedge(A, B, B, C)
    model.set_wedge(E, B, B, D)
    model.set_wedge(F, B, B, D)

    return model


if __name__ == "__main__":
    construct_0091_g1()
