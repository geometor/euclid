"""Programmatic construction for Book I, Proposition 16 (0293.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0293_g1() -> Model:
    """Construct the figure 0293.g1 using geometor.model."""
    model = Model("0293.g1")

    # Points
    A = model.set_point(94, -20, classes=["given"], label="A")
    B = model.set_point(26, -121.5, classes=["given"], label="B")
    C = model.set_point(143.5, -121.5, classes=["given"], label="C")
    D = model.set_point(196, -121.5, label="D")
    E = model.set_point(118.75, -70.75, label="E")
    F = model.set_point(211.5, -20, label="F")
    G = model.set_point(175, -185, label="G")

    # Construction lines
    model.construct_line(B, D)
    model.construct_line(A, G)
    model.construct_line(B, F)

    # Segments
    model.set_segment(B, D)
    model.set_segment(A, B)
    model.set_segment(A, G)
    model.set_segment(B, F)
    model.set_segment(F, C)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(A, C)
    model.set_segment(C, G)
    model.set_segment(B, E)
    model.set_segment(E, F)

    # Collinear / broken sections
    model.set_section([B, C, D])
    model.set_section([A, E, C])
    model.set_section([A, C, G])
    model.set_section([B, E, F])

    # Polygons
    model.set_polygon([A, B, E])
    model.set_polygon([C, F, E])
    model.set_polygon([A, B, C])

    # Angles (wedges)
    model.set_wedge(C, A, A, D)
    model.set_wedge(B, C, C, A)
    model.set_wedge(A, B, B, C)
    model.set_wedge(E, A, A, B)
    model.set_wedge(E, F, F, C)
    model.set_wedge(C, E, E, F)
    model.set_wedge(C, F, F, D)
    model.set_wedge(C, B, B, G)
    model.set_wedge(C, A, A, B)

    return model


if __name__ == "__main__":
    construct_0293_g1()
