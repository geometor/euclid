"""Programmatic construction for Book IV, Proposition 2 (0088.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0088_g1() -> Model:
    """Construct the figure 0088.g1 using geometor.model."""
    model = Model("0088.g1")

    # Points (y-inverted for standard mathematical coordinates)
    O = model.set_point(106.0, -86.0, label="O")
    A = model.set_point(90.70, -152.26, classes=["given"], label="A")
    B = model.set_point(74.00, -25.97, label="B")
    C = model.set_point(172.51, -100.14, label="C")
    G = model.set_point(18.59, -135.61, label="G")
    H = model.set_point(208.60, -179.49, label="H")

    # Given triangle DEF
    D = model.set_point(224.80, -126.64, classes=["given"], label="D")
    E = model.set_point(211.00, -29.00, classes=["given"], label="E")
    F = model.set_point(288.50, -88.07, classes=["given"], label="F")

    # Circle ABC
    model.construct_circle(O, A)

    # Tangent line GH
    model.construct_line(G, H)

    # Segments
    model.set_segment(G, H)
    model.set_segment(A, G)
    model.set_segment(A, H)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, C)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(D, F)

    # Collinear section
    model.set_section([G, A, H])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])

    # Angles (wedges)
    model.set_wedge(A, H, H, C)
    model.set_wedge(A, G, G, B)
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, A, A, B)
    model.set_wedge(E, D, D, F)
    model.set_wedge(F, D, D, E)
    model.set_wedge(D, E, E, F)

    return model


if __name__ == "__main__":
    construct_0088_g1()
