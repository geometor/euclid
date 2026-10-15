"""Programmatic construction for Book III, Proposition 1 (0012.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0012_g1() -> Model:
    """Construct the figure 0012.g1 using geometor.model."""
    model = Model("0012.g1")

    # Points (y-inverted for standard mathematical coordinates)
    F = model.set_point(89, -104, label="F")
    C = model.set_point(89, -34, classes=["given"], label="C")
    E = model.set_point(89, -174, label="E")
    D = model.set_point(89, -148, label="D")
    A = model.set_point(34.56, -148, classes=["given"], label="A")
    B = model.set_point(143.44, -148, classes=["given"], label="B")
    G = model.set_point(109, -110, label="G")

    # Construction circle
    model.construct_circle(F, C)

    # Construction lines
    model.construct_line(C, E)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(C, E)
    model.set_segment(D, C)
    model.set_segment(D, E)
    model.set_segment(C, F)
    model.set_segment(F, E)
    model.set_segment(F, D)
    model.set_segment(G, A)
    model.set_segment(G, D)
    model.set_segment(G, B)

    # Collinear sections
    model.set_section([A, D, B])
    model.set_section([C, F, E])
    model.set_section([C, D, E])

    # Polygons
    model.set_polygon([A, D, G])
    model.set_polygon([B, D, G])
    model.set_polygon([A, G, B])

    # Angles (wedges)
    model.set_wedge(D, A, A, G)
    model.set_wedge(D, G, G, B)
    model.set_wedge(D, F, F, B)

    return model


if __name__ == "__main__":
    construct_0012_g1()
