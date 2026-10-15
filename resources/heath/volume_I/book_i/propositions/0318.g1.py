"""Programmatic construction for Book I, Proposition 26 note - Thales Ship Distance (0318.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0318_g1() -> Model:
    """Construct the figure for Thales' determination of a ship's distance (0318.g1)."""
    model = Model("0318.g1")

    A = model.set_point(23.5, -25.5, classes=["given"], label="A")
    B = model.set_point(23.5, -130.5, classes=["given"], label="B")
    C = model.set_point(176.5, -130.5, classes=["given"], label="C")
    D = model.set_point(23.5, -41.5, label="D")
    E = model.set_point(47, -41.5, label="E")

    # Segments and collinear sub-segments
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_section([A, D, B])

    model.set_segment(A, C)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_section([A, E, C])

    model.set_segment(B, C)
    model.set_segment(D, E)

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, E])
    model.set_polygon([D, B, C, E])

    # Angles
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, A, A, B)
    model.set_wedge(D, A, A, E)
    model.set_wedge(E, A, A, D)

    return model


if __name__ == "__main__":
    construct_0318_g1()
