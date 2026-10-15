"""Programmatic construction for Book III, Proposition 36 Case 1 (0080.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0080_g1() -> Model:
    """Construct the figure 0080.g1 using geometor.model."""
    model = Model("0080.g1")

    # Circle ABC with center F(84, -74), radius 58 (y-inverted)
    F = model.set_point(84.0, -74.0, label="F")
    B = model.set_point(26.0, -74.0, classes=["given"], label="B")
    D = model.set_point(26.0, -152.0, classes=["given"], label="D")
    C = model.set_point(49.39, -120.54, label="C")
    A = model.set_point(118.61, -27.46, label="A")

    # Circle ABC
    model.construct_circle(F, B)

    # Segments
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(A, F)
    model.set_segment(F, C)
    model.set_segment(C, D)
    model.set_segment(F, D)
    model.set_segment(D, B)
    model.set_segment(F, B)

    # Sections
    model.set_section([D, C, A])
    model.set_section([D, C, F])
    model.set_section([C, F, A])
    model.set_section([D, F, A])

    # Polygon and angle
    model.set_polygon([F, B, D])
    model.set_wedge(B, F, F, D)

    return model


if __name__ == "__main__":
    construct_0080_g1()
