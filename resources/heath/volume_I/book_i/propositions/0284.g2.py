"""Programmatic construction for Book I, Proposition 11 Note — Heron's Perpendicular at an Extremity (0284.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0284_g2() -> Model:
    """Construct the figure 0284.g2 using geometor.model."""
    model = Model("0284.g2")

    # Points
    A = model.set_point(8, -140, classes=["given"], label="A")
    C = model.set_point(89, -140, classes=["given"], label="C")
    B = model.set_point(185, -140, classes=["given"], label="B")
    F = model.set_point(8, -57, label="F")
    D = model.set_point(89, -57, label="D")
    E = model.set_point(89, -20, label="E")

    # Construction lines
    model.construct_line(A, B)
    model.construct_line(C, E)

    # Segments
    model.set_segment(A, B)
    model.set_segment(C, E)
    model.set_segment(A, F)
    model.set_segment(D, F)
    model.set_segment(C, F)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(C, D)
    model.set_segment(D, E)

    # Collinear / broken sections
    model.set_section([A, C, B])
    model.set_section([C, D, E])

    # Polygons
    model.set_polygon([A, C, F])
    model.set_polygon([D, C, F])
    model.set_polygon([A, C, D, F])

    # Angles (wedges)
    model.set_wedge(C, A, A, E)
    model.set_wedge(C, A, A, F)
    model.set_wedge(C, D, D, F)
    model.set_wedge(A, F, F, C)
    model.set_wedge(D, C, C, F)
    model.set_wedge(D, E, E, F)
    model.set_wedge(C, E, E, B)

    return model


if __name__ == "__main__":
    construct_0284_g2()
