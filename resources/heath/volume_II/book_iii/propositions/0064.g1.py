"""Programmatic construction for Book III, Proposition 27 (0064.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0064_g1() -> Model:
    """Construct the figure 0064.g1 using geometor.model."""
    model = Model("0064.g1")

    # Left circle ABC with center G and point K (y-inverted)
    G = model.set_point(83.00, -86.00, label="G")
    A = model.set_point(40.00, -37.26, classes=["given"], label="A")
    B = model.set_point(28.88, -122.00, classes=["given"], label="B")
    C = model.set_point(137.12, -122.00, classes=["given"], label="C")
    K = model.set_point(120.63, -139.00, label="K")

    # Right circle DEF with center H (y-inverted)
    H = model.set_point(244.00, -92.00, label="H")
    D = model.set_point(218.00, -32.43, classes=["given"], label="D")
    E = model.set_point(189.88, -128.00, classes=["given"], label="E")
    F = model.set_point(298.12, -128.00, classes=["given"], label="F")

    # Equal circles ABC and DEF
    model.construct_circle(G, A)
    model.construct_circle(H, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, G)
    model.set_segment(G, C)
    model.set_segment(G, K)

    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(E, H)
    model.set_segment(H, F)

    # Angles (wedges)
    model.set_wedge(G, B, B, C)
    model.set_wedge(G, B, B, K)
    model.set_wedge(H, E, E, F)
    model.set_wedge(A, B, B, C)
    model.set_wedge(D, E, E, F)

    return model


if __name__ == "__main__":
    construct_0064_g1()
