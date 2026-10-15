"""Programmatic construction for Book III, Proposition 29 (0066.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0066_g1() -> Model:
    """Construct the figure 0066.g1 using geometor.model."""
    model = Model("0066.g1")

    # Left circle ABC with center K and arc points A, G (y-inverted)
    K = model.set_point(77.00, -78.00, label="K")
    B = model.set_point(28.63, -110.00, classes=["given"], label="B")
    C = model.set_point(125.37, -110.00, classes=["given"], label="C")
    A = model.set_point(77.00, -20.00, label="A")
    G = model.set_point(77.00, -136.00, label="G")

    # Right circle DEF with center L and arc points D, H (y-inverted)
    L = model.set_point(277.00, -78.00, label="L")
    E = model.set_point(228.63, -110.00, classes=["given"], label="E")
    F = model.set_point(325.37, -110.00, classes=["given"], label="F")
    D = model.set_point(277.00, -20.00, label="D")
    H = model.set_point(277.00, -136.00, label="H")

    # Equal circles ABC and DEF
    model.construct_circle(K, B)
    model.construct_circle(L, E)

    # Segments
    model.set_segment(B, C)
    model.set_segment(B, K)
    model.set_segment(K, C)

    model.set_segment(E, F)
    model.set_segment(E, L)
    model.set_segment(L, F)

    # Polygons
    model.set_polygon([B, K, C])
    model.set_polygon([E, L, F])

    # Angles (wedges)
    model.set_wedge(K, B, B, C)
    model.set_wedge(L, E, E, F)

    return model


if __name__ == "__main__":
    construct_0066_g1()
