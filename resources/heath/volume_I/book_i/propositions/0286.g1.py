"""Programmatic construction for Book I, Proposition 12 Note — Proclus's Refutation Case 1 (0286.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0286_g1() -> Model:
    """Construct the figure 0286.g1 using geometor.model."""
    model = Model("0286.g1")

    # Points
    A = model.set_point(2, -119, classes=["given"], label="A")
    G = model.set_point(52, -119, label="G")
    H = model.set_point(104, -119, label="H")
    K = model.set_point(125, -119, label="K")
    E = model.set_point(156, -119, label="E")
    B = model.set_point(215, -119, classes=["given"], label="B")
    C = model.set_point(104, -70, classes=["given"], label="C")
    L = model.set_point(104, -135, label="L")
    F = model.set_point(58, -27, label="F")

    # Construction lines
    model.construct_line(A, B)
    model.construct_line(C, L)

    # Construction circles
    model.construct_circle(C, G)

    # Segments
    model.set_segment(A, B)
    model.set_segment(C, L)
    model.set_segment(C, G)
    model.set_segment(C, K)
    model.set_segment(C, E)
    model.set_segment(C, H)
    model.set_segment(H, L)
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(K, E)
    model.set_segment(H, E)
    model.set_segment(G, K)
    model.set_segment(G, E)

    # Collinear / broken sections
    model.set_section([G, H, E])
    model.set_section([C, H, L])

    # Polygons
    model.set_polygon([C, G, H])
    model.set_polygon([C, K, H])
    model.set_polygon([C, E, H])
    model.set_polygon([C, K, E])
    model.set_polygon([C, G, K])
    model.set_polygon([C, G, E])

    # Angles (wedges)
    model.set_wedge(H, C, C, G)
    model.set_wedge(H, C, C, E)
    model.set_wedge(G, C, C, K)
    model.set_wedge(K, C, C, G)
    model.set_wedge(K, C, C, E)
    model.set_wedge(E, C, C, K)

    return model


if __name__ == "__main__":
    construct_0286_g1()
