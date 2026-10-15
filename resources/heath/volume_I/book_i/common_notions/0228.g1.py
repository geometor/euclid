"""Programmatic construction for Postulate 5 Commentary, Legendre (0228.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0228_g1() -> Model:
    """Construct the figure 0228.g1 (Legendre's angle-deficit doubling) using geometor.model."""
    model = Model("0228.g1")

    # Points (y negated for Cartesian coordinates)
    A = model.set_point(201, -116, classes=["given"], label="A")
    B = model.set_point(141, -69, classes=["given"], label="B")
    C = model.set_point(113, -116, classes=["given"], label="C")
    D = model.set_point(53, -69, label="D")
    E = model.set_point(85, -25, label="E")
    F = model.set_point(19, -116, label="F")

    # Construction lines
    model.construct_line(A, E)
    model.construct_line(A, F)
    model.construct_line(E, F)
    model.construct_line(B, C)
    model.construct_line(B, D)
    model.construct_line(C, D)

    # Segments (including collinear sub-segments)
    model.set_segment(A, B)
    model.set_segment(B, E)
    model.set_segment(A, E)
    model.set_segment(A, C)
    model.set_segment(C, F)
    model.set_segment(A, F)
    model.set_segment(E, D)
    model.set_segment(D, F)
    model.set_segment(E, F)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(C, D)

    # Collinear sections
    model.set_section([A, B, E])
    model.set_section([A, C, F])
    model.set_section([E, D, F])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([D, B, C])
    model.set_polygon([D, E, B])
    model.set_polygon([F, D, C])
    model.set_polygon([A, E, F])

    # Angles (wedges)
    model.set_wedge(A, C, C, B)
    model.set_wedge(B, C, C, A)
    model.set_wedge(C, A, A, B)
    model.set_wedge(B, D, D, C)
    model.set_wedge(C, B, B, D)

    return model


if __name__ == "__main__":
    construct_0228_g1()
