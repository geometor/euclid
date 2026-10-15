"""Programmatic construction for Book X, Lemma before Proposition 33 (0078.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0078_g1() -> Model:
    """Construct the figure 0078.g1 using geometor.model."""
    model = Model("0078.g1")

    # Right-angled triangle ABC (angle A right) with altitude AD perpendicular to BC
    A = model.set_point(55.5, -20.5, classes=["given"], label="A")
    B = model.set_point(20.0, -89.0, classes=["given"], label="B")
    D = model.set_point(55.5, -89.0, label="D")
    C = model.set_point(188.0, -89.0, classes=["given"], label="C")

    # Base lines
    model.construct_line(B, C)
    model.construct_line(A, B)
    model.construct_line(A, C)
    model.construct_line(A, D)

    # Segments
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_section([B, D, C])

    # Triangles ABC, ABD, ADC
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])

    # Right angles at A and D
    model.set_wedge(A, B, B, C)
    model.set_wedge(D, A, B, A)
    model.set_wedge(D, A, A, C)

    return model


if __name__ == "__main__":
    construct_0078_g1()
