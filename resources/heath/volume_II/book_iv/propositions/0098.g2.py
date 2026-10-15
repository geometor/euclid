"""Programmatic construction for Book IV, Proposition 7 (0098.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0098_g2() -> Model:
    """Construct the figure 0098.g2 using geometor.model."""
    model = Model("0098.g2")

    # Points (y-inverted for standard mathematical coordinates)
    E = model.set_point(90.00, -95.00, label="E")
    A = model.set_point(90.00, -31.00, classes=["given"], label="A")
    B = model.set_point(26.00, -95.00, label="B")
    C = model.set_point(90.00, -159.00, label="C")
    D = model.set_point(154.00, -95.00, label="D")
    G = model.set_point(26.00, -31.00, label="G")
    F = model.set_point(154.00, -31.00, label="F")
    H = model.set_point(26.00, -159.00, label="H")
    K = model.set_point(154.00, -159.00, label="K")

    # Circle ABCD
    model.construct_circle(E, A)

    # Construction lines
    model.construct_line(A, C)
    model.construct_line(B, D)
    model.construct_line(F, G)
    model.construct_line(G, H)
    model.construct_line(H, K)
    model.construct_line(K, F)

    # Segments
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(E, A)
    model.set_segment(E, B)
    model.set_segment(E, C)
    model.set_segment(E, D)
    model.set_segment(F, G)
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(K, F)
    model.set_segment(G, A)
    model.set_segment(A, F)
    model.set_segment(G, B)
    model.set_segment(B, H)
    model.set_segment(H, C)
    model.set_segment(C, K)
    model.set_segment(K, D)
    model.set_segment(D, F)

    # Collinear sections
    model.set_section([A, E, C])
    model.set_section([B, E, D])
    model.set_section([G, A, F])
    model.set_section([G, B, H])
    model.set_section([H, C, K])
    model.set_section([F, D, K])

    # Polygons (squares and rectangles)
    model.set_polygon([F, G, H, K])
    model.set_polygon([G, H, C, A])
    model.set_polygon([A, C, K, F])
    model.set_polygon([F, G, B, D])
    model.set_polygon([B, H, K, D])
    model.set_polygon([G, B, E, A])

    # Angles (wedges)
    model.set_wedge(E, A, A, B)
    model.set_wedge(B, E, E, G)
    model.set_wedge(G, A, A, B)
    model.set_wedge(H, G, G, K)
    model.set_wedge(K, H, H, F)
    model.set_wedge(F, K, K, G)

    return model


if __name__ == "__main__":
    construct_0098_g2()
