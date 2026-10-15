"""Programmatic construction for Book I, Proposition 11 Note — Apollonius's Construction (0284.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0284_g1() -> Model:
    """Construct the figure 0284.g1 using geometor.model."""
    model = Model("0284.g1")

    # Points
    A = model.set_point(10, -65, classes=["given"], label="A")
    D = model.set_point(111, -65, label="D")
    C = model.set_point(141, -65, classes=["given"], label="C")
    E = model.set_point(171, -65, label="E")
    B = model.set_point(296, -65, classes=["given"], label="B")
    F = model.set_point(141, -13, label="F")

    # Construction lines
    model.construct_line(A, B)

    # Construction circles
    model.construct_circle(D, E)
    model.construct_circle(E, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(D, F)
    model.set_segment(F, E)
    model.set_segment(F, C)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(C, E)
    model.set_segment(E, B)
    model.set_segment(D, E)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Collinear / broken sections
    model.set_section([D, C, E])
    model.set_section([A, C, B])

    # Polygons
    model.set_polygon([F, D, E])
    model.set_polygon([D, C, F])
    model.set_polygon([E, C, F])

    # Angles (wedges)
    model.set_wedge(C, D, D, F)
    model.set_wedge(C, E, E, F)

    return model


if __name__ == "__main__":
    construct_0284_g1()
