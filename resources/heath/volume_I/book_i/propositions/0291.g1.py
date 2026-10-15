"""Programmatic construction for Book I, Proposition 14 Note — Porphyry's Construction (0291.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0291_g1() -> Model:
    """Construct the figure 0291.g1 using geometor.model."""
    model = Model("0291.g1")

    # Points
    A = model.set_point(20, -94, classes=["given"], label="A")
    C = model.set_point(108, -94, classes=["given"], label="C")
    B = model.set_point(180, -94, classes=["given"], label="B")
    D = model.set_point(108, -25, label="D")
    E = model.set_point(180, -25, label="E")
    F = model.set_point(180, -164, label="F")

    # Construction lines
    model.construct_line(A, B)
    model.construct_line(C, D)
    model.construct_line(E, F)

    # Segments
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(E, F)
    model.set_segment(C, E)
    model.set_segment(C, F)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(E, B)
    model.set_segment(B, F)

    # Collinear / broken sections
    model.set_section([A, C, B])
    model.set_section([E, B, F])

    # Polygons
    model.set_polygon([C, B, E])
    model.set_polygon([C, B, F])
    model.set_polygon([C, E, F])

    # Angles (wedges)
    model.set_wedge(C, D, D, E)
    model.set_wedge(C, D, D, F)
    model.set_wedge(C, E, E, B)
    model.set_wedge(C, B, B, F)
    model.set_wedge(C, D, D, B)
    model.set_wedge(C, D, D, A)

    return model


if __name__ == "__main__":
    construct_0291_g1()
