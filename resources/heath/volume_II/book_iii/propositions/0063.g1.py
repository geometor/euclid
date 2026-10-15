"""Programmatic construction for Book III, Proposition 26 (0063.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0063_g1() -> Model:
    """Construct the figure 0063.g1 using geometor.model."""
    model = Model("0063.g1")

    # Left circle ABC with center G and arc point K (y-inverted)
    G = model.set_point(101.00, -86.00, label="G")
    A = model.set_point(68.00, -37.09, classes=["given"], label="A")
    B = model.set_point(52.09, -119.00, classes=["given"], label="B")
    C = model.set_point(149.91, -119.00, classes=["given"], label="C")
    K = model.set_point(101.00, -145.00, label="K")

    # Right circle DEF with center H and arc point L (y-inverted)
    H = model.set_point(281.00, -86.00, label="H")
    D = model.set_point(333.96, -60.00, classes=["given"], label="D")
    E = model.set_point(232.09, -119.00, classes=["given"], label="E")
    F = model.set_point(329.91, -119.00, classes=["given"], label="F")
    L = model.set_point(281.00, -145.00, label="L")

    # Equal circles ABC and DEF
    model.construct_circle(G, A)
    model.construct_circle(H, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, G)
    model.set_segment(G, C)
    model.set_segment(B, C)

    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(E, H)
    model.set_segment(H, F)
    model.set_segment(E, F)

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([B, G, C])
    model.set_polygon([D, E, F])
    model.set_polygon([E, H, F])

    # Angles (wedges)
    model.set_wedge(G, B, B, C)
    model.set_wedge(H, E, E, F)
    model.set_wedge(A, B, B, C)
    model.set_wedge(D, E, E, F)

    return model


if __name__ == "__main__":
    construct_0063_g1()
