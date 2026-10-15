"""Programmatic construction for Book I, Proposition 16 Note — Impossibility of Three Equal Lines from One Point (0295.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0295_g1() -> Model:
    """Construct the figure 0295.g1 using geometor.model."""
    model = Model("0295.g1")

    # Points
    A = model.set_point(94, -32, classes=["given"], label="A")
    B = model.set_point(20, -96, classes=["given"], label="B")
    C = model.set_point(118, -96, label="C")
    D = model.set_point(169, -96, classes=["given"], label="D")

    # Construction lines
    model.construct_line(B, D)

    # Segments
    model.set_segment(B, D)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(B, C)
    model.set_segment(C, D)

    # Collinear / broken sections
    model.set_section([B, C, D])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, C, D])
    model.set_polygon([A, B, D])

    # Angles (wedges)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, A, A, B)
    model.set_wedge(C, A, A, D)
    model.set_wedge(D, A, A, C)
    model.set_wedge(A, B, B, C)
    model.set_wedge(A, C, C, D)
    model.set_wedge(A, B, B, D)

    return model


if __name__ == "__main__":
    construct_0295_g1()
