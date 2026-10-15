"""Programmatic construction for Book I, I.34 (0340.g1).

An-Nairizi's construction for dividing a given straight line AB into three equal parts.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0340_g1() -> Model:
    """Construct the figure for 0340.g1 (I.34) using geometor.model."""
    model = Model("0340.g1")

    # 1. Points
    A = model.set_point(23, -134, classes=["given"], label="A")
    B = model.set_point(197, -134, classes=["given"], label="B")
    C = model.set_point(23, -226, label="C")
    D = model.set_point(197, -42, label="D")
    E = model.set_point(23, -180, label="E")
    F = model.set_point(197, -88, label="F")
    G = model.set_point(81, -134, label="G")
    H = model.set_point(139, -134, label="H")
    K = model.set_point(139, -88, label="K")

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(A, G)
    model.set_segment(G, H)
    model.set_segment(H, B)
    model.set_segment(A, C)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(B, D)
    model.set_segment(B, F)
    model.set_segment(F, D)
    model.set_segment(E, D)
    model.set_segment(E, G)
    model.set_segment(G, D)
    model.set_segment(C, F)
    model.set_segment(C, K)
    model.set_segment(K, F)
    model.set_segment(H, K)

    # 4. Collinear Sections
    model.set_section([A, G, H])
    model.set_section([G, H, B])
    model.set_section([A, E, C])
    model.set_section([B, F, D])
    model.set_section([E, G, D])
    model.set_section([C, K, F])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([E, C, H, K])
    model.set_polygon([E, A, G])
    model.set_polygon([K, H, G])
    model.set_polygon([F, B, H])

    # 6. Angles (Wedges)
    model.set_wedge(A, E, E, G)
    model.set_wedge(H, K, K, G)
    model.set_wedge(B, F, F, H)

    return model


if __name__ == "__main__":
    construct_0340_g1()
