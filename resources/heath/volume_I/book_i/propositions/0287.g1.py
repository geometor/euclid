"""Programmatic construction for Book I, Proposition 12 Note — Proclus's Refutation Case 2 (0287.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0287_g1() -> Model:
    """Construct the figure 0287.g1 using geometor.model."""
    model = Model("0287.g1")

    # Points
    A = model.set_point(7, -138, classes=["given"], label="A")
    G = model.set_point(69, -138, label="G")
    H = model.set_point(123, -138, label="H")
    K = model.set_point(150, -138, label="K")
    E = model.set_point(177, -138, label="E")
    B = model.set_point(238, -138, classes=["given"], label="B")
    C = model.set_point(123, -95, classes=["given"], label="C")
    L = model.set_point(156.5, -148.5, label="L")

    # Construction lines
    model.construct_line(A, B)
    model.construct_line(C, L)

    # Construction circles
    model.construct_circle(C, G)

    # Segments
    model.set_segment(A, B)
    model.set_segment(C, G)
    model.set_segment(C, H)
    model.set_segment(C, L)
    model.set_segment(C, E)
    model.set_segment(C, K)
    model.set_segment(K, L)
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(K, E)
    model.set_segment(H, E)
    model.set_segment(G, E)

    # Collinear / broken sections
    model.set_section([G, H, E])
    model.set_section([H, K, E])
    model.set_section([C, K, L])

    # Polygons
    model.set_polygon([C, G, H])
    model.set_polygon([C, H, K])
    model.set_polygon([C, K, E])
    model.set_polygon([C, H, E])
    model.set_polygon([C, G, E])

    # Angles (wedges)
    model.set_wedge(H, C, C, K)
    model.set_wedge(K, C, C, H)
    model.set_wedge(K, C, C, E)
    model.set_wedge(H, C, C, G)

    return model


if __name__ == "__main__":
    construct_0287_g1()
