"""Programmatic construction for Book I, I.43 (0355.g1).

Proclus' commentary on I.43: non-overlapping parallelograms about the diameter producing five-sided complements.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0355_g1() -> Model:
    """Construct the figure for 0355.g1 (I.43) using geometor.model."""
    model = Model("0355.g1")

    # 1. Points
    A = model.set_point(50, -20, classes=["given"], label="A")
    B = model.set_point(17, -107, classes=["given"], label="B")
    C = model.set_point(160, -107, classes=["given"], label="C")
    D = model.set_point(193, -20, classes=["given"], label="D")
    E = model.set_point(25.4, -85, label="E")
    F = model.set_point(53, -107, label="F")
    G = model.set_point(61.5, -85, label="G")
    H = model.set_point(122.2, -55, label="H")
    K = model.set_point(135.5, -20, label="K")
    L = model.set_point(180, -55, label="L")

    # 3. Segments
    model.set_segment(A, D)
    model.set_segment(B, C)
    model.set_segment(A, B)
    model.set_segment(D, C)
    model.set_segment(B, D)
    model.set_segment(E, G)
    model.set_segment(G, F)
    model.set_segment(K, H)
    model.set_segment(H, L)

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C, D])
    model.set_polygon([E, B, F, G])
    model.set_polygon([K, H, L, D])
    model.set_polygon([A, K, H, G, E])
    model.set_polygon([L, H, G, F, C])

    return model


if __name__ == "__main__":
    construct_0355_g1()
