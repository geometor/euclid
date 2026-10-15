"""Programmatic construction for Book III, Proposition 1 Commentary (0013.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0013_g1() -> Model:
    """Construct De Morgan's figure 0013.g1 using geometor.model."""
    model = Model("0013.g1")

    # Points (y-inverted for standard mathematical coordinates)
    O = model.set_point(96, -90, label="O")
    B = model.set_point(30.55, -60, classes=["given"], label="B")
    A = model.set_point(96, -162, classes=["given"], label="A")
    C = model.set_point(153.6, -133.2, classes=["given"], label="C")
    D = model.set_point(63.28, -111, label="D")
    E = model.set_point(124.8, -147.6, label="E")

    # Construction circle
    model.construct_circle(O, A)

    # Construction lines (perpendicular bisectors)
    model.construct_line(D, O)
    model.construct_line(E, O)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(A, C)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(D, O)
    model.set_segment(E, O)
    model.set_segment(B, C)

    # Sections
    model.set_section([A, D, B])
    model.set_section([A, E, C])
    model.set_section([B, A, C])

    # Polygons
    model.set_polygon([A, D, O, E])

    # Angles (wedges)
    model.set_wedge(D, A, A, O)
    model.set_wedge(E, A, A, O)

    return model


if __name__ == "__main__":
    construct_0013_g1()
