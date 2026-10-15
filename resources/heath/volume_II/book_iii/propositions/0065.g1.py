"""Programmatic construction for Book III, Proposition 28 (0065.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0065_g1() -> Model:
    """Construct the figure 0065.g1 using geometor.model."""
    model = Model("0065.g1")

    # Left circle ABC with center K and arc points C, G (y-inverted)
    K = model.set_point(73.00, -75.00, label="K")
    A = model.set_point(25.30, -108.00, classes=["given"], label="A")
    B = model.set_point(120.70, -108.00, classes=["given"], label="B")
    C = model.set_point(73.00, -17.00, label="C")
    G = model.set_point(73.00, -133.00, label="G")

    # Right circle DEF with center L and arc points F, H (y-inverted)
    L = model.set_point(313.00, -75.00, label="L")
    D = model.set_point(265.30, -108.00, classes=["given"], label="D")
    E = model.set_point(360.70, -108.00, classes=["given"], label="E")
    F = model.set_point(313.00, -17.00, label="F")
    H = model.set_point(313.00, -133.00, label="H")

    # Equal circles ABC and DEF
    model.construct_circle(K, A)
    model.construct_circle(L, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, K)
    model.set_segment(K, B)

    model.set_segment(D, E)
    model.set_segment(D, L)
    model.set_segment(L, E)

    # Polygons
    model.set_polygon([A, K, B])
    model.set_polygon([D, L, E])

    # Angles (wedges)
    model.set_wedge(K, A, A, B)
    model.set_wedge(L, D, D, E)

    return model


if __name__ == "__main__":
    construct_0065_g1()
