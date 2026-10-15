"""Programmatic construction for Book I, Proposition 12 Note — Point M on CL (0288.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0288_g2() -> Model:
    """Construct the figure 0288.g2 using geometor.model."""
    model = Model("0288.g2")

    # Points
    N = model.set_point(103, -16, label="N")
    C = model.set_point(83, -35, classes=["given"], label="C")
    G = model.set_point(18, -96, classes=["given"], label="G")
    M = model.set_point(62, -96, label="M")
    L = model.set_point(125, -96, classes=["given"], label="L")

    # Construction lines
    model.construct_line(C, G)
    model.construct_line(G, L)

    # Segments
    model.set_segment(G, L)
    model.set_segment(G, N)
    model.set_segment(C, M)
    model.set_segment(C, L)
    model.set_segment(C, G)
    model.set_segment(C, N)
    model.set_segment(G, M)
    model.set_segment(M, L)

    # Collinear / broken sections
    model.set_section([G, C, N])
    model.set_section([G, M, L])

    # Polygons
    model.set_polygon([C, G, M])
    model.set_polygon([C, M, L])
    model.set_polygon([C, G, L])

    # Angles (wedges)
    model.set_wedge(G, N, N, M)
    model.set_wedge(M, G, G, L)
    model.set_wedge(M, C, C, L)
    model.set_wedge(M, C, C, G)
    model.set_wedge(L, G, G, C)

    return model


if __name__ == "__main__":
    construct_0288_g2()
