"""Programmatic construction for Book I, Proposition 14 (0290.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0290_g1() -> Model:
    """Construct the figure 0290.g1 using geometor.model."""
    model = Model("0290.g1")

    # Points
    C = model.set_point(5, -79.5, classes=["given"], label="C")
    B = model.set_point(87, -79.5, classes=["given"], label="B")
    D = model.set_point(168, -79.5, classes=["given"], label="D")
    A = model.set_point(58, -22, classes=["given"], label="A")
    E = model.set_point(150, -18, label="E")

    # Construction lines
    model.construct_line(C, D)
    model.construct_line(A, B)
    model.construct_line(B, E)

    # Segments
    model.set_segment(C, D)
    model.set_segment(A, B)
    model.set_segment(B, E)
    model.set_segment(B, C)
    model.set_segment(B, D)

    # Collinear / broken sections
    model.set_section([C, B, D])
    model.set_section([C, B, E])

    # Polygons
    model.set_polygon([C, B, A])
    model.set_polygon([A, B, E])
    model.set_polygon([E, B, D])

    # Angles (wedges)
    model.set_wedge(B, A, A, C)
    model.set_wedge(B, A, A, D)
    model.set_wedge(B, A, A, E)
    model.set_wedge(B, E, E, D)

    return model


if __name__ == "__main__":
    construct_0290_g1()
