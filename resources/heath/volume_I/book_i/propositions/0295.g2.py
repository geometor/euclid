"""Programmatic construction for Book I, Proposition 16 Note — Proclus's Non-Meeting Lines (0295.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0295_g2() -> Model:
    """Construct the figure 0295.g2 using geometor.model."""
    model = Model("0295.g2")

    # Points
    A = model.set_point(24, -30, classes=["given"], label="A")
    B = model.set_point(24, -122.5, classes=["given"], label="B")
    C = model.set_point(65, -30, classes=["given"], label="C")
    D = model.set_point(65, -122.5, label="D")
    E = model.set_point(161, -122.5, classes=["given"], label="E")

    # Construction lines
    model.construct_line(B, E)
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Segments
    model.set_segment(B, E)
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(B, D)
    model.set_segment(D, E)

    # Collinear / broken sections
    model.set_section([B, D, E])

    # Polygons
    model.set_polygon([A, B, D, C])

    # Angles (wedges)
    model.set_wedge(B, A, A, D)
    model.set_wedge(D, C, C, E)
    model.set_wedge(D, C, C, B)

    return model


if __name__ == "__main__":
    construct_0295_g2()
