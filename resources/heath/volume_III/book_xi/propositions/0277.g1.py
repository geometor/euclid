"""Programmatic construction for Book XI, Proposition 1 Commentary (0277.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0277_g1() -> Model:
    """Construct the figure 0277.g1 using geometor.model."""
    model = Model("0277.g1")

    # Plane DE corners
    D = model.set_point(22.0, -23.0, classes=["given"], label="D")
    P2 = model.set_point(133.0, -23.0, classes=["plane_corner"])
    E = model.set_point(179.0, -105.0, classes=["given"], label="E")
    P4 = model.set_point(42.0, -97.0, classes=["plane_corner"])

    # Points inside plane DE and elevated point B
    A = model.set_point(53.0, -61.0, classes=["given"], label="A")
    C = model.set_point(93.0, -62.0, classes=["given"], label="C")
    F = model.set_point(135.0, -63.0, label="F")
    B = model.set_point(135.0, -48.0, classes=["given"], label="B")
    G = model.set_point(91.0, -93.0, label="G")

    # Construction line ACF
    model.construct_line(A, F)

    # Segments
    model.set_segment(A, C)
    model.set_segment(C, F)
    model.set_segment(A, F)
    model.set_segment(C, B)
    model.set_segment(C, G)

    # Plane boundary segments
    model.set_segment(D, P2)
    model.set_segment(P2, E)
    model.set_segment(E, P4)
    model.set_segment(P4, D)

    # Sections
    model.set_section([A, C, F])
    model.set_section([A, C, B])

    # Plane polygon
    model.set_polygon([D, P2, E, P4])

    # Angles
    model.set_wedge(C, A, A, G)
    model.set_wedge(C, G, G, F)

    return model


if __name__ == "__main__":
    construct_0277_g1()
