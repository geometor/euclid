"""Programmatic construction for Book III, Proposition 2 Commentary (0015.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0015_g1() -> Model:
    """Construct the figure 0015.g1 using geometor.model."""
    model = Model("0015.g1")

    # Points (y-inverted for standard mathematical coordinates)
    D = model.set_point(80, -76, label="D")
    A = model.set_point(35.5, -122, classes=["given"], label="A")
    B = model.set_point(124.5, -122, classes=["given"], label="B")
    E = model.set_point(103, -122, label="E")

    # Construction circle
    model.construct_circle(D, A)

    # Construction line (AB produced)
    model.construct_line(A, B)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(D, A)
    model.set_segment(D, B)
    model.set_segment(D, E)

    # Sections
    model.set_section([A, E, B])

    # Polygons
    model.set_polygon([D, A, B])
    model.set_polygon([D, A, E])
    model.set_polygon([D, B, E])

    # Angles (wedges)
    model.set_wedge(A, D, D, B)
    model.set_wedge(B, D, D, A)
    model.set_wedge(E, D, D, A)

    return model


if __name__ == "__main__":
    construct_0015_g1()
