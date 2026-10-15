"""Programmatic construction for Book I, Proposition 26 note - Fluminis Varatio (0319.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0319_g1() -> Model:
    """Construct the figure for Marcus Junius Nipsus' fluminis varatio (0319.g1)."""
    model = Model("0319.g1")

    A = model.set_point(22, -128.5, classes=["given"], label="A")
    B = model.set_point(22, -22, classes=["given"], label="B")
    C = model.set_point(111.5, -128.5, label="C")
    D = model.set_point(66.75, -128.5, label="D")
    E = model.set_point(111.5, -235, label="E")

    # Segments and collinear sub-segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_section([A, D, C])

    model.set_segment(C, E)
    model.set_segment(B, E)
    model.set_segment(B, D)
    model.set_segment(D, E)
    model.set_section([B, D, E])

    # Polygons
    model.set_polygon([B, A, D])
    model.set_polygon([E, C, D])

    # Angles
    model.set_wedge(A, B, B, D)
    model.set_wedge(C, E, E, D)
    model.set_wedge(D, A, A, B)
    model.set_wedge(D, C, C, E)
    model.set_wedge(B, A, A, D)
    model.set_wedge(E, C, C, D)

    return model


if __name__ == "__main__":
    construct_0319_g1()
