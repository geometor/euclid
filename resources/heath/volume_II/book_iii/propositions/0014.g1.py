"""Programmatic construction for Book III, Proposition 2 (0014.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0014_g1() -> Model:
    """Construct the figure 0014.g1 using geometor.model."""
    model = Model("0014.g1")

    # Points (y-inverted for standard mathematical coordinates)
    D = model.set_point(102, -90, label="D")
    A = model.set_point(27.3, -104, classes=["given"], label="A")
    B = model.set_point(97, -165.84, classes=["given"], label="B")
    C = model.set_point(155, -35.53, classes=["given"], label="C")
    F = model.set_point(66.37, -157.13, label="F")
    E = model.set_point(62.38, -164.64, label="E")

    # Construction circle ABC
    model.construct_circle(D, A)

    # Segments
    model.set_segment(D, A)
    model.set_segment(D, B)
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(F, E)
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)

    # Sections
    model.set_section([D, F, E])
    model.set_section([A, E, B])

    # Polygons
    model.set_polygon([D, A, E])
    model.set_polygon([D, B, E])
    model.set_polygon([D, A, B])

    # Angles (wedges)
    model.set_wedge(A, D, D, E)
    model.set_wedge(B, D, D, E)
    model.set_wedge(E, D, D, B)

    return model


if __name__ == "__main__":
    construct_0014_g1()
