"""Programmatic construction for Book X, Proposition 41 (0094.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0094_g1() -> Model:
    """Construct the figure 0094.g1 using geometor.model."""
    model = Model("0094.g1")

    # Straight line AC divided into straight lines AB, BC
    A = model.set_point(23.0, -259.5, classes=["given"], label="A")
    B = model.set_point(94.0, -259.5, classes=["given"], label="B")
    C = model.set_point(146.0, -259.5, classes=["given"], label="C")

    # Parallelogram DH (K, H at top; G, F in middle; D, E at bottom)
    K = model.set_point(53.5, -18.5, label="K")
    H = model.set_point(118.5, -18.5, label="H")
    G = model.set_point(53.5, -103.5, label="G")
    F = model.set_point(118.5, -103.5, label="F")
    D = model.set_point(53.5, -236.0, classes=["given"], label="D")
    E = model.set_point(118.5, -236.0, classes=["given"], label="E")

    # Base lines
    model.construct_line(A, C)
    model.construct_line(D, K)
    model.construct_line(E, H)
    model.construct_line(D, E)
    model.construct_line(G, F)
    model.construct_line(K, H)

    # Segments
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(D, E)
    model.set_segment(G, F)
    model.set_segment(K, H)
    model.set_segment(D, G)
    model.set_segment(G, K)
    model.set_segment(D, K)
    model.set_segment(E, F)
    model.set_segment(F, H)
    model.set_segment(E, H)

    # Sections
    model.set_section([A, B, C])
    model.set_section([D, G, K])
    model.set_section([E, F, H])

    # Polygons: whole rectangle DH, lower rectangle DF, upper rectangle GH
    model.set_polygon([D, E, H, K])
    model.set_polygon([D, E, F, G])
    model.set_polygon([G, F, H, K])

    return model


if __name__ == "__main__":
    construct_0094_g1()
