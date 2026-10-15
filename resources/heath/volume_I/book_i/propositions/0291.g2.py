"""Programmatic construction for Book I, Proposition 15 (0291.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0291_g2() -> Model:
    """Construct the figure 0291.g2 using geometor.model."""
    model = Model("0291.g2")

    # Points
    A = model.set_point(21, -36, classes=["given"], label="A")
    C = model.set_point(25, -72.5, classes=["given"], label="C")
    E = model.set_point(95, -72.5, label="E")
    D = model.set_point(170, -72.5, classes=["given"], label="D")
    B = model.set_point(169, -109, classes=["given"], label="B")

    # Construction lines
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Segments
    model.set_segment(C, D)
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(C, E)
    model.set_segment(E, D)

    # Collinear / broken sections
    model.set_section([A, E, B])
    model.set_section([C, E, D])

    # Polygons
    model.set_polygon([A, E, C])
    model.set_polygon([D, E, B])
    model.set_polygon([C, E, B])
    model.set_polygon([A, E, D])

    # Angles (wedges)
    model.set_wedge(E, A, A, C)
    model.set_wedge(E, D, D, B)
    model.set_wedge(E, C, C, B)
    model.set_wedge(E, A, A, D)

    return model


if __name__ == "__main__":
    construct_0291_g2()
