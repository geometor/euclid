"""Programmatic construction for Book III, Proposition 25 Case 2 (0061.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0061_g2() -> Model:
    """Construct the figure 0061.g2 using geometor.model."""
    model = Model("0061.g2")

    # Points (y-inverted)
    D = model.set_point(85.00, -80.00, label="D")
    A = model.set_point(85.00, -22.00, classes=["given"], label="A")
    C = model.set_point(85.00, -138.00, classes=["given"], label="C")
    B = model.set_point(27.00, -80.00, classes=["given"], label="B")

    # Circle for semicircle ABC
    model.construct_circle(D, A)

    # Segments and sections
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(B, D)
    model.set_segment(A, B)
    model.set_section([A, D, C])

    # Polygon
    model.set_polygon([A, B, D])

    # Angles (wedges)
    model.set_wedge(B, A, A, D)
    model.set_wedge(A, B, B, D)

    return model


if __name__ == "__main__":
    construct_0061_g2()
