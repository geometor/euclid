"""Programmatic construction for Book III, Proposition 30 (0067.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0067_g1() -> Model:
    """Construct the figure 0067.g1 using geometor.model."""
    model = Model("0067.g1")

    # Points (y-inverted)
    O = model.set_point(107.00, -115.38, label="O")
    A = model.set_point(28.00, -83.00, classes=["given"], label="A")
    B = model.set_point(186.00, -83.00, classes=["given"], label="B")
    C = model.set_point(107.00, -83.00, label="C")
    D = model.set_point(107.00, -30.00, label="D")

    # Circle for circumference ADB
    model.construct_circle(O, A)

    # Segments and section
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(C, D)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_section([A, C, B])

    # Polygons
    model.set_polygon([A, C, D])
    model.set_polygon([B, C, D])
    model.set_polygon([A, D, B])

    # Angles (wedges)
    model.set_wedge(C, A, A, D)
    model.set_wedge(C, B, B, D)

    return model


if __name__ == "__main__":
    construct_0067_g1()
