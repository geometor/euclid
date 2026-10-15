"""Programmatic construction for Book III, Proposition 7 Heron Note (0022.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0022_g1() -> Model:
    """Construct the figure 0022.g1 using geometor.model."""
    model = Model("0022.g1")

    # Points (y-inverted for standard mathematical coordinates)
    D = model.set_point(108, -80, label="D")
    C = model.set_point(40.92, -68.82, classes=["given"], label="C")
    B = model.set_point(175.08, -91.18, classes=["given"], label="B")
    A = model.set_point(74.46, -74.41, classes=["given"], label="A")
    E = model.set_point(169.97, -52, classes=["given"], label="E")
    F = model.set_point(126, -145.57, classes=["given"], label="F")
    G = model.set_point(105.0, -67.24, label="G")
    H = model.set_point(88.65, -94.01, label="H")

    # Construction circle
    model.construct_circle(D, E)

    # Segments
    model.set_segment(C, B)
    model.set_segment(C, A)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(A, E)
    model.set_segment(A, G)
    model.set_segment(G, E)
    model.set_segment(A, F)
    model.set_segment(A, H)
    model.set_segment(H, F)
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(D, G)
    model.set_segment(D, H)

    # Sections
    model.set_section([C, A, B])
    model.set_section([C, D, B])
    model.set_section([A, G, E])
    model.set_section([A, H, F])

    # Polygons
    model.set_polygon([D, G, E])
    model.set_polygon([D, G, A])
    model.set_polygon([D, H, F])
    model.set_polygon([D, H, A])

    return model


if __name__ == "__main__":
    construct_0022_g1()
