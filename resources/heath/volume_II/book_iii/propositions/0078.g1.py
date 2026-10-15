"""Programmatic construction for Book III, Proposition 35 Case 2 (0078.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0078_g1() -> Model:
    """Construct the figure 0078.g1 using geometor.model."""
    model = Model("0078.g1")

    # Center F(95, -92) and points on circle ABCD, radius 78 (y-inverted)
    F = model.set_point(95.0, -92.0, label="F")
    A = model.set_point(24.3, -59.0, classes=["given"], label="A")
    C = model.set_point(101.0, -169.77, classes=["given"], label="C")
    B = model.set_point(68.0, -165.18, classes=["given"], label="B")
    D = model.set_point(165.7, -59.0, classes=["given"], label="D")
    E = model.set_point(83.42, -144.39, label="E")
    G = model.set_point(62.65, -114.38, label="G")
    H = model.set_point(116.85, -112.09, label="H")

    # Circle ABCD
    model.construct_circle(F, A)

    # Chords AC and BD and their sub-segments
    model.set_segment(A, C)
    model.set_segment(A, G)
    model.set_segment(G, C)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(G, E)

    model.set_segment(B, D)
    model.set_segment(D, H)
    model.set_segment(H, B)
    model.set_segment(D, E)
    model.set_segment(E, B)
    model.set_segment(H, E)

    # Perpendiculars and radii from F
    model.set_segment(F, G)
    model.set_segment(F, H)
    model.set_segment(F, B)
    model.set_segment(F, C)
    model.set_segment(F, E)

    # Sections
    model.set_section([A, G, C])
    model.set_section([A, E, C])
    model.set_section([A, G, E])
    model.set_section([G, E, C])
    model.set_section([D, H, B])
    model.set_section([D, E, B])
    model.set_section([D, H, E])
    model.set_section([H, E, B])

    # Polygons
    model.set_polygon([F, G, E])
    model.set_polygon([F, G, C])
    model.set_polygon([F, H, E])
    model.set_polygon([F, H, B])

    return model


if __name__ == "__main__":
    construct_0078_g1()
