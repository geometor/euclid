"""Programmatic construction for Book XII, Proposition 10 (0404.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0404_g1() -> Model:
    """Construct the figure 0404.g1 using geometor.model."""
    model = Model("0404.g1")

    # Center O and points on circumference of circle ABCD
    O = model.set_point(131.0, -134.0)
    A = model.set_point(131.0, -29.0, classes=["given"], label="A")
    B = model.set_point(26.0, -134.0, classes=["given"], label="B")
    C = model.set_point(131.0, -239.0, classes=["given"], label="C")
    D = model.set_point(236.0, -134.0, classes=["given"], label="D")

    E = model.set_point(56.75, -59.75, label="E")
    F = model.set_point(56.75, -208.25, label="F")
    G = model.set_point(205.25, -208.25, label="G")
    H = model.set_point(205.25, -59.75, label="H")

    # Base circle ABCD
    model.construct_circle(O, A)

    # Square sides
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)

    # Octagon sides
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(B, F)
    model.set_segment(F, C)
    model.set_segment(C, G)
    model.set_segment(G, D)
    model.set_segment(D, H)
    model.set_segment(H, A)

    # Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, E, B, F, C, G, D, H])
    model.set_polygon([A, E, B])
    model.set_polygon([B, F, C])
    model.set_polygon([C, G, D])
    model.set_polygon([D, H, A])

    return model


if __name__ == "__main__":
    construct_0404_g1()
