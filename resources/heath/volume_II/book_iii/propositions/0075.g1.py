"""Programmatic construction for Book III, Proposition 33 — Obtuse Angle Case (0075.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0075_g1() -> Model:
    """Construct the figure 0075.g1 using geometor.model."""
    model = Model("0075.g1")

    # Given obtuse angle at C (y-inverted)
    C = model.set_point(55.0, -89.0, classes=["given"], label="C")
    C1 = model.set_point(155.0, -89.0, label="C1")
    C2 = model.set_point(12.0, -37.8, label="C2")
    model.set_segment(C, C1)
    model.set_segment(C, C2)
    model.set_wedge(C, C1, C1, C2)

    # Circle AEBH with center G(263, -91), radius 73
    G = model.set_point(263.0, -91.0, label="G")
    A = model.set_point(263.0, -18.0, classes=["given"], label="A")
    E = model.set_point(263.0, -164.0, label="E")
    B = model.set_point(191.13, -103.8, classes=["given"], label="B")
    F = model.set_point(227.07, -60.9, label="F")
    H = model.set_point(211.38, -39.38, label="H")
    D = model.set_point(340.0, -18.0, label="D")

    # Construction circle AEB
    model.construct_circle(G, A)

    # Segments
    model.set_segment(A, D)
    model.set_segment(A, E)
    model.set_segment(A, G)
    model.set_segment(G, E)
    model.set_segment(A, B)
    model.set_segment(A, F)
    model.set_segment(F, B)
    model.set_segment(F, G)
    model.set_segment(G, B)
    model.set_segment(A, H)
    model.set_segment(H, B)

    # Sections
    model.set_section([A, F, B])
    model.set_section([A, G, E])

    # Polygons
    model.set_polygon([A, F, G])
    model.set_polygon([B, F, G])
    model.set_polygon([A, B, G])
    model.set_polygon([A, H, B])

    # Angles
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, D, D, E)
    model.set_wedge(F, A, A, G)
    model.set_wedge(F, B, B, G)
    model.set_wedge(H, A, A, B)

    return model


if __name__ == "__main__":
    construct_0075_g1()
