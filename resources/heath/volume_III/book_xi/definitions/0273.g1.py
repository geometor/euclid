"""Programmatic construction for Book XI, Definition 13 Commentary (0273.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0273_g1() -> Model:
    """Construct the figure 0273.g1 using geometor.model."""
    model = Model("0273.g1")

    # Points (y negated for standard Cartesian coordinates)
    A = model.set_point(85.0, -227.0, classes=["given"], label="A")
    B = model.set_point(176.0, -238.0, classes=["given"], label="B")
    C = model.set_point(251.0, -190.0, classes=["given"], label="C")
    D = model.set_point(24.0, -183.0, classes=["given"], label="D")
    E = model.set_point(85.0, -68.0, classes=["given"], label="E")
    F = model.set_point(150.0, -24.0, classes=["given"], label="F")
    G = model.set_point(55.0, -48.0, classes=["given"], label="G")

    # Segments of base ABCD
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)

    # Segments of opposite face EFG
    model.set_segment(E, F)
    model.set_segment(F, G)
    model.set_segment(G, E)

    # Lateral connecting segments
    model.set_segment(G, D)
    model.set_segment(E, D)
    model.set_segment(E, A)
    model.set_segment(E, B)
    model.set_segment(F, B)
    model.set_segment(F, C)
    model.set_segment(G, C)

    # Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([E, F, G])
    model.set_polygon([G, D, E])
    model.set_polygon([E, D, A])
    model.set_polygon([E, A, B])
    model.set_polygon([E, B, F])
    model.set_polygon([F, B, C])
    model.set_polygon([F, G, C])
    model.set_polygon([G, D, C])

    return model


if __name__ == "__main__":
    construct_0273_g1()
