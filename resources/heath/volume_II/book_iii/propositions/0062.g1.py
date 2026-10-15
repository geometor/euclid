"""Programmatic construction for Book III, Proposition 25 Case 3 (0062.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0062_g1() -> Model:
    """Construct the figure 0062.g1 using geometor.model."""
    model = Model("0062.g1")

    # Points (y-inverted)
    E = model.set_point(83.00, -72.00, label="E")
    D = model.set_point(110.00, -72.00, label="D")
    A = model.set_point(110.00, -24.00, classes=["given"], label="A")
    C = model.set_point(110.00, -120.00, classes=["given"], label="C")
    B = model.set_point(27.93, -72.00, classes=["given"], label="B")

    # Circle for segment ABC
    model.construct_circle(E, A)

    # Segments and sections
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(B, D)
    model.set_segment(B, E)
    model.set_segment(E, D)
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_section([A, D, C])
    model.set_section([B, E, D])

    # Polygons
    model.set_polygon([A, B, D])
    model.set_polygon([A, B, E])
    model.set_polygon([A, E, D])

    # Angles (wedges)
    model.set_wedge(B, A, A, D)
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, B, B, E)

    return model


if __name__ == "__main__":
    construct_0062_g1()
