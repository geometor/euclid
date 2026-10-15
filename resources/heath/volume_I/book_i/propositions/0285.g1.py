"""Programmatic construction for Book I, Proposition 12 (0285.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0285_g1() -> Model:
    """Construct the figure 0285.g1 using geometor.model."""
    model = Model("0285.g1")

    # Points
    A = model.set_point(10, -150, classes=["given"], label="A")
    G = model.set_point(59, -150, label="G")
    H = model.set_point(130, -150, label="H")
    E = model.set_point(201, -150, label="E")
    B = model.set_point(260, -150, classes=["given"], label="B")
    C = model.set_point(130, -110, classes=["given"], label="C")
    F = model.set_point(130, -28.5, label="F")
    D = model.set_point(175, -177, classes=["given"], label="D")

    # Construction lines
    model.construct_line(A, B)

    # Construction circles
    model.construct_circle(C, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(C, H)
    model.set_segment(C, G)
    model.set_segment(C, E)
    model.set_segment(G, H)
    model.set_segment(H, E)
    model.set_segment(E, G)
    model.set_segment(A, G)
    model.set_segment(E, B)
    model.set_segment(C, D)
    model.set_segment(C, F)

    # Collinear / broken sections
    model.set_section([G, H, E])
    model.set_section([A, H, B])

    # Polygons
    model.set_polygon([C, G, H])
    model.set_polygon([C, E, H])
    model.set_polygon([C, G, E])

    # Angles (wedges)
    model.set_wedge(H, C, C, G)
    model.set_wedge(H, E, E, C)

    return model


if __name__ == "__main__":
    construct_0285_g1()
