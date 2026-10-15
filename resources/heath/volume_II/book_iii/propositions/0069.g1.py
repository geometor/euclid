"""Programmatic construction for Book III, Proposition 31 Commentary (0069.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0069_g1() -> Model:
    """Construct the figure 0069.g1 using geometor.model."""
    model = Model("0069.g1")

    # Semicircle endpoints D, E, center B, and midpoint of arc C (y-inverted)
    D = model.set_point(16.00, -84.00, classes=["given"], label="D")
    E = model.set_point(154.00, -84.00, classes=["given"], label="E")
    B = model.set_point(85.00, -84.00, label="B")
    C = model.set_point(85.00, -15.00, label="C")

    # Circle for semicircle
    model.construct_circle(B, D)

    # Segments and section
    model.set_segment(D, E)
    model.set_segment(D, B)
    model.set_segment(B, E)
    model.set_segment(B, C)
    model.set_segment(D, C)
    model.set_segment(C, E)
    model.set_section([D, B, E])

    # Polygons
    model.set_polygon([D, C, E])
    model.set_polygon([D, B, C])
    model.set_polygon([E, B, C])

    # Angles (wedges)
    model.set_wedge(C, D, D, E)
    model.set_wedge(B, D, D, C)
    model.set_wedge(B, E, E, C)

    return model


if __name__ == "__main__":
    construct_0069_g1()
