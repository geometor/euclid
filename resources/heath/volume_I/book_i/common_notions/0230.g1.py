"""Programmatic construction for Postulate 5 Commentary, Legendre (0230.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0230_g1() -> Model:
    """Construct the figure 0230.g1 (Legendre's first proof of Theorem I) using geometor.model."""
    model = Model("0230.g1")

    # Points (y negated for Cartesian coordinates)
    A = model.set_point(68, -112, classes=["given"], label="A")
    B = model.set_point(115, -23, classes=["given"], label="B")
    C = model.set_point(135, -112, classes=["given"], label="C")
    D = model.set_point(182, -23, label="D")
    E = model.set_point(202, -112, label="E")
    F = model.set_point(249, -23, label="F")
    G = model.set_point(269, -112, label="G")
    H = model.set_point(316, -23, label="H")
    J = model.set_point(336, -112, label="J")
    K = model.set_point(383, -23, label="K")

    # Construction lines
    model.construct_line(A, J)
    model.construct_line(B, K)
    model.construct_line(A, B)
    model.construct_line(B, C)
    model.construct_line(C, D)
    model.construct_line(D, E)
    model.construct_line(E, F)
    model.construct_line(F, G)
    model.construct_line(G, H)
    model.construct_line(H, J)
    model.construct_line(J, K)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(A, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(C, E)
    model.set_segment(B, D)
    model.set_segment(E, F)
    model.set_segment(F, G)
    model.set_segment(E, G)
    model.set_segment(D, F)
    model.set_segment(G, H)
    model.set_segment(H, J)
    model.set_segment(G, J)
    model.set_segment(F, H)
    model.set_segment(J, K)
    model.set_segment(H, K)
    model.set_segment(A, J)
    model.set_segment(B, K)

    # Sections / composite lines
    model.set_section([A, C, J])
    model.set_section([B, D, K])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([B, C, D])
    model.set_polygon([D, C, E])
    model.set_polygon([D, E, F])
    model.set_polygon([F, E, G])
    model.set_polygon([F, G, H])
    model.set_polygon([H, G, J])
    model.set_polygon([H, J, K])

    # Angles (wedges)
    model.set_wedge(A, C, C, B)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, B, B, A)
    model.set_wedge(C, D, D, B)
    model.set_wedge(C, E, E, D)
    model.set_wedge(E, F, F, D)

    return model


if __name__ == "__main__":
    construct_0230_g1()
