"""Programmatic construction for Book III, Proposition 7 Commentary (0021.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0021_g1() -> Model:
    """Construct the figure 0021.g1 using geometor.model."""
    model = Model("0021.g1")

    # Points (y-inverted for standard mathematical coordinates)
    E = model.set_point(86, -75, label="E")
    A = model.set_point(26, -75, classes=["given"], label="A")
    D = model.set_point(146, -75, classes=["given"], label="D")
    F = model.set_point(111, -75, classes=["given"], label="F")
    B = model.set_point(31.01, -51, classes=["given"], label="B")
    C = model.set_point(43.15, -33, classes=["given"], label="C")
    M = model.set_point(74.97, -64.19, label="M")

    # Construction circle
    model.construct_circle(E, A)

    # Segments
    model.set_segment(A, D)
    model.set_segment(A, E)
    model.set_segment(E, F)
    model.set_segment(F, D)
    model.set_segment(F, B)
    model.set_segment(F, C)
    model.set_segment(E, C)
    model.set_segment(E, B)
    model.set_segment(E, M)
    model.set_segment(M, C)
    model.set_segment(F, M)
    model.set_segment(M, B)

    # Sections
    model.set_section([A, E, D])
    model.set_section([A, F, D])
    model.set_section([E, M, C])
    model.set_section([F, M, B])

    # Polygons
    model.set_polygon([E, B, F])
    model.set_polygon([E, C, F])
    model.set_polygon([E, M, F])

    # Angles (wedges)
    model.set_wedge(F, B, B, D)
    model.set_wedge(F, C, C, D)
    model.set_wedge(E, B, B, D)
    model.set_wedge(E, C, C, D)
    model.set_wedge(F, E, E, B)
    model.set_wedge(F, E, E, C)

    return model


if __name__ == "__main__":
    construct_0021_g1()
