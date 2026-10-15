"""Programmatic construction for Book I, Proposition 17 Note — Proclus's Proof without Producing a Side (0296.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0296_g2() -> Model:
    """Construct the figure 0296.g2 using geometor.model."""
    model = Model("0296.g2")

    # Points
    A = model.set_point(53.5, -23.5, classes=["given"], label="A")
    B = model.set_point(7, -73, classes=["given"], label="B")
    D = model.set_point(87, -73, label="D")
    C = model.set_point(141, -73, classes=["given"], label="C")

    # Construction lines
    model.construct_line(B, C)

    # Segments
    model.set_segment(B, C)
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(D, C)

    # Collinear / broken sections
    model.set_section([B, D, C])

    # Polygons
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([A, B, C])

    # Angles (wedges)
    model.set_wedge(D, A, A, C)
    model.set_wedge(D, A, A, B)
    model.set_wedge(B, A, A, D)
    model.set_wedge(C, A, A, D)
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, D, D, C)
    model.set_wedge(A, B, B, C)

    return model


if __name__ == "__main__":
    construct_0296_g2()
