"""Programmatic construction for Book IV, Proposition 15 (0113.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0113_g1() -> Model:
    """Construct the figure 0113.g1 (Inscribed regular hexagon) using geometor.model."""
    model = Model("0113.g1")

    # Points (y-inverted for standard mathematical coordinates)
    G = model.set_point(86.00, -145.00, label="G")
    A = model.set_point(86.00, -209.00, classes=["given"], label="A")
    B = model.set_point(30.57, -177.00, label="B")
    C = model.set_point(30.57, -113.00, label="C")
    D = model.set_point(86.00, -81.00, label="D")
    E = model.set_point(141.43, -113.00, label="E")
    F = model.set_point(141.43, -177.00, label="F")
    H = model.set_point(86.00, -17.00, label="H")

    # Given circle ABCDEF and auxiliary circle EGCH
    model.construct_circle(G, A)
    model.construct_circle(D, G)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, A)
    model.set_segment(A, D)
    model.set_segment(B, E)
    model.set_segment(C, F)
    model.set_segment(G, A)
    model.set_segment(G, B)
    model.set_segment(G, C)
    model.set_segment(G, D)
    model.set_segment(G, E)
    model.set_segment(G, F)

    # Collinear sections
    model.set_section([A, G, D])
    model.set_section([B, G, E])
    model.set_section([C, G, F])

    # Polygons
    model.set_polygon([A, B, C, D, E, F])
    model.set_polygon([E, G, D])
    model.set_polygon([D, G, C])

    # Angles (wedges)
    model.set_wedge(E, G, G, D)
    model.set_wedge(G, D, D, E)
    model.set_wedge(D, E, E, G)
    model.set_wedge(D, G, G, C)
    model.set_wedge(C, G, G, B)
    model.set_wedge(E, G, G, C)
    model.set_wedge(B, G, G, A)
    model.set_wedge(A, G, G, F)
    model.set_wedge(F, G, G, E)
    model.set_wedge(F, E, E, D)
    model.set_wedge(A, F, F, E)

    return model


if __name__ == "__main__":
    construct_0113_g1()
