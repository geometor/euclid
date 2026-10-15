"""Programmatic construction for Book I, Proposition 12 Note — Proclus's Refutation Case 3 (0287.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0287_g2() -> Model:
    """Construct the figure 0287.g2 using geometor.model."""
    model = Model("0287.g2")

    # Points
    A = model.set_point(7, -120.5, classes=["given"], label="A")
    G = model.set_point(56.5, -120.5, label="G")
    K = model.set_point(89, -120.5, label="K")
    M = model.set_point(114.5, -110, label="M")
    H = model.set_point(114.5, -120.5, label="H")
    L = model.set_point(140, -120.5, label="L")
    E = model.set_point(172.5, -120.5, label="E")
    B = model.set_point(239, -120.5, classes=["given"], label="B")
    C = model.set_point(114.5, -80, classes=["given"], label="C")
    F = model.set_point(65, -31, label="F")

    # Construction lines
    model.construct_line(A, B)
    model.construct_line(C, H)

    # Construction circles
    model.construct_circle(C, G)

    # Segments
    model.set_segment(A, B)
    model.set_segment(C, G)
    model.set_segment(C, K)
    model.set_segment(C, H)
    model.set_segment(C, L)
    model.set_segment(C, E)
    model.set_segment(C, M)
    model.set_segment(M, H)
    model.set_segment(G, K)
    model.set_segment(K, H)
    model.set_segment(H, L)
    model.set_segment(L, E)
    model.set_segment(G, H)
    model.set_segment(H, E)
    model.set_segment(G, E)

    # Collinear / broken sections
    model.set_section([C, M, H])
    model.set_section([G, H, E])

    # Polygons
    model.set_polygon([C, G, K])
    model.set_polygon([C, K, H])
    model.set_polygon([C, L, H])
    model.set_polygon([C, L, E])
    model.set_polygon([C, G, H])
    model.set_polygon([C, E, H])

    # Angles (wedges)
    model.set_wedge(H, C, C, K)
    model.set_wedge(K, C, C, H)
    model.set_wedge(H, C, C, L)
    model.set_wedge(L, C, C, H)

    return model


if __name__ == "__main__":
    construct_0287_g2()
