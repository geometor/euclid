"""Programmatic construction for Book X Introductory Note (0006.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0006_g1() -> Model:
    """Construct the square ABCD with diagonal AC for 0006.g1."""
    model = Model("0006.g1")

    # Vertices of square ABCD (in Euclidean y-up coordinates)
    A = model.set_point(21.5, -22.5, classes=["given"], label="A")
    B = model.set_point(119.0, -22.5, classes=["given"], label="B")
    C = model.set_point(119.0, -120.0, label="C")
    D = model.set_point(21.5, -120.0, label="D")

    # Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, C])

    # Segments: sides and diagonal AC
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)
    model.set_segment(A, C)

    # Angle wedges
    model.set_wedge(B, A, A, C)
    model.set_wedge(D, A, A, C)
    model.set_wedge(A, B, B, C)
    model.set_wedge(A, D, D, C)

    return model


if __name__ == "__main__":
    construct_0006_g1()
