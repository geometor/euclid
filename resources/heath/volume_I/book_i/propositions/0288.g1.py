"""Programmatic construction for Book I, Proposition 12 Note — Heath's Reflection Proof via I. 7 (0288.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0288_g1() -> Model:
    """Construct the figure 0288.g1 using geometor.model."""
    model = Model("0288.g1")

    # Points
    A = model.set_point(12, -83.5, classes=["given"], label="A")
    G = model.set_point(50.5, -83.5, label="G")
    K = model.set_point(70.5, -83.5, label="K")
    H = model.set_point(117, -83.5, label="H")
    E = model.set_point(183.5, -83.5, label="E")
    B = model.set_point(231, -83.5, classes=["given"], label="B")
    C = model.set_point(117, -25, classes=["given"], label="C")
    L = model.set_point(117, -142, label="L")

    # Construction lines
    model.construct_line(A, B)
    model.construct_line(C, L)

    # Segments
    model.set_segment(A, B)
    model.set_segment(C, L)
    model.set_segment(C, G)
    model.set_segment(C, K)
    model.set_segment(C, E)
    model.set_segment(L, G)
    model.set_segment(L, K)
    model.set_segment(C, H)
    model.set_segment(H, L)
    model.set_segment(A, G)
    model.set_segment(G, K)
    model.set_segment(K, H)
    model.set_segment(H, G)
    model.set_segment(A, H)
    model.set_segment(H, E)
    model.set_segment(E, B)
    model.set_segment(H, B)
    model.set_segment(G, E)

    # Collinear / broken sections
    model.set_section([C, H, L])
    model.set_section([C, G, L])
    model.set_section([C, K, L])
    model.set_section([G, H, E])

    # Polygons
    model.set_polygon([C, G, L])
    model.set_polygon([C, K, L])
    model.set_polygon([C, H, E])
    model.set_polygon([C, H, G])
    model.set_polygon([L, H, G])
    model.set_polygon([C, H, K])
    model.set_polygon([L, H, K])

    # Angles (wedges)
    model.set_wedge(H, C, C, G)
    model.set_wedge(H, L, L, G)
    model.set_wedge(H, C, C, E)
    model.set_wedge(H, L, L, E)

    return model


if __name__ == "__main__":
    construct_0288_g1()
