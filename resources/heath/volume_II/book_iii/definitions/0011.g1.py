"""Programmatic construction for Book III, Definition 10 Note (0011.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0011_g1() -> Model:
    """Construct the figure 0011.g1 using geometor.model."""
    model = Model("0011.g1")

    # Points (y-inverted for standard mathematical coordinates)
    A = model.set_point(49, -28, classes=["given"], label="A")
    D = model.set_point(28, -94, classes=["given"], label="D")
    B = model.set_point(152, -94, classes=["given"], label="B")
    E = model.set_point(90, -94, label="E")
    C = model.set_point(90, -121, classes=["given"], label="C")
    F = model.set_point(65.6, -38.64, label="F")
    O = model.set_point(90, -36.32, classes=["auxiliary"], label="O")

    # Construction circle for arc DCB
    model.construct_circle(O, D)

    # Segments
    model.set_segment(A, D)
    model.set_segment(A, B)
    model.set_segment(B, D)
    model.set_segment(D, E)
    model.set_segment(E, B)
    model.set_segment(E, C)
    model.set_segment(A, E)
    model.set_segment(A, C)
    model.set_segment(E, F)
    model.set_segment(C, F)
    model.set_segment(A, F)
    model.set_segment(F, B)

    # Sections (broken line AEC and collinear divisions)
    model.set_section([A, E, C])
    model.set_section([B, E, D])
    model.set_section([A, F, B])

    # Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, C, E])
    model.set_polygon([A, C, F])

    return model


if __name__ == "__main__":
    construct_0011_g1()
