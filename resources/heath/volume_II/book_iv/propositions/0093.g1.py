"""Programmatic construction for Book IV, Proposition 4 Commentary — Heron's Formula (0093.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0093_g1() -> Model:
    """Construct the figure 0093.g1 using geometor.model."""
    model = Model("0093.g1")

    # Points (y-inverted for standard mathematical coordinates)
    A = model.set_point(185.00, -28.00, classes=["given"], label="A")
    C = model.set_point(28.00, -172.00, classes=["given"], label="C")
    B = model.set_point(245.00, -172.00, classes=["given"], label="B")
    G = model.set_point(165.02, -118.68, label="G")
    D = model.set_point(214.24, -98.17, label="D")
    E = model.set_point(165.02, -172.00, label="E")
    F = model.set_point(128.98, -79.38, label="F")
    H = model.set_point(321.02, -172.00, label="H")
    K = model.set_point(185.77, -172.00, label="K")
    L = model.set_point(245.00, -324.21, label="L")

    # Inscribed circle DEF
    model.construct_circle(G, D)

    # Construction line CH
    model.construct_line(C, H)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(B, E)
    model.set_segment(E, C)
    model.set_segment(C, F)
    model.set_segment(F, A)
    model.set_segment(B, H)
    model.set_segment(C, H)
    model.set_segment(E, K)
    model.set_segment(K, B)
    model.set_segment(A, G)
    model.set_segment(B, G)
    model.set_segment(C, G)
    model.set_segment(D, G)
    model.set_segment(E, G)
    model.set_segment(F, G)
    model.set_segment(G, L)
    model.set_segment(G, K)
    model.set_segment(K, L)
    model.set_segment(B, L)
    model.set_segment(C, L)

    # Collinear sections
    model.set_section([A, D, B])
    model.set_section([A, F, C])
    model.set_section([C, E, B])
    model.set_section([C, B, H])
    model.set_section([E, K, B])
    model.set_section([G, K, L])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([B, G, C])
    model.set_polygon([A, C, G])
    model.set_polygon([A, B, G])
    model.set_polygon([A, G, D])
    model.set_polygon([C, L, B])
    model.set_polygon([C, G, B, L])

    # Angles (wedges)
    model.set_wedge(G, C, C, L)
    model.set_wedge(B, C, C, L)
    model.set_wedge(G, C, C, B)
    model.set_wedge(L, C, C, B)
    model.set_wedge(G, A, A, D)
    model.set_wedge(G, A, A, C)
    model.set_wedge(G, D, D, B)
    model.set_wedge(D, A, A, G)

    return model


if __name__ == "__main__":
    construct_0093_g1()
