"""Programmatic construction for Book III, Proposition 33 — Acute Angle Case (0073.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0073_g1() -> Model:
    """Construct the figure 0073.g1 using geometor.model."""
    model = Model("0073.g1")

    # Given acute angle at C (y-inverted)
    C = model.set_point(83.0, -103.0, classes=["given"], label="C")
    C1 = model.set_point(16.0, -103.0, label="C1")
    C2 = model.set_point(56.0, -63.0, label="C2")
    model.set_segment(C, C1)
    model.set_segment(C, C2)
    model.set_wedge(C, C1, C1, C2)

    # Circle ABE with center G(207, -104), radius 74
    G = model.set_point(207.0, -104.0, label="G")
    A = model.set_point(207.0, -30.0, classes=["given"], label="A")
    E = model.set_point(207.0, -178.0, label="E")
    B = model.set_point(134.15, -117.0, classes=["given"], label="B")
    F = model.set_point(170.58, -73.5, label="F")
    D = model.set_point(138.0, -30.0, label="D")
    D2 = model.set_point(284.0, -30.0, label="D2")

    # Construction circle ABE
    model.construct_circle(G, A)

    # Segments
    model.set_segment(D, D2)
    model.set_segment(A, D)
    model.set_segment(A, E)
    model.set_segment(A, G)
    model.set_segment(G, E)
    model.set_segment(A, B)
    model.set_segment(A, F)
    model.set_segment(F, B)
    model.set_segment(F, G)
    model.set_segment(G, B)
    model.set_segment(E, B)

    # Sections
    model.set_section([A, F, B])
    model.set_section([A, G, E])

    # Polygons
    model.set_polygon([A, F, G])
    model.set_polygon([B, F, G])
    model.set_polygon([A, B, G])
    model.set_polygon([A, B, E])

    # Angles
    model.set_wedge(A, D, D, B)
    model.set_wedge(A, D, D, E)
    model.set_wedge(F, A, A, G)
    model.set_wedge(F, B, B, G)
    model.set_wedge(E, A, A, B)

    return model


if __name__ == "__main__":
    construct_0073_g1()
