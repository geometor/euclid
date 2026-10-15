"""Programmatic construction for Book I, I.43 (0354.g1).

In any parallelogram the complements of the parallelograms about the diameter are equal to one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0354_g1() -> Model:
    """Construct the figure for 0354.g1 (I.43) using geometor.model."""
    model = Model("0354.g1")

    # 1. Points
    A = model.set_point(64, -33, classes=["given"], label="A")
    B = model.set_point(30, -138, classes=["given"], label="B")
    C = model.set_point(202, -138, classes=["given"], label="C")
    D = model.set_point(236, -33, classes=["given"], label="D")
    E = model.set_point(55, -62, label="E")
    F = model.set_point(80, -138, label="F")
    G = model.set_point(227, -62, label="G")
    H = model.set_point(114, -33, label="H")
    K = model.set_point(105, -62, label="K")

    # 3. Segments
    model.set_segment(A, D)
    model.set_segment(A, H)
    model.set_segment(H, D)
    model.set_segment(B, C)
    model.set_segment(B, F)
    model.set_segment(F, C)
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(D, C)
    model.set_segment(D, G)
    model.set_segment(G, C)
    model.set_segment(A, C)
    model.set_segment(A, K)
    model.set_segment(K, C)
    model.set_segment(E, G)
    model.set_segment(E, K)
    model.set_segment(K, G)
    model.set_segment(H, F)
    model.set_segment(H, K)
    model.set_segment(K, F)

    # 4. Collinear Sections
    model.set_section([A, H, D])
    model.set_section([B, F, C])
    model.set_section([A, E, B])
    model.set_section([D, G, C])
    model.set_section([A, K, C])
    model.set_section([E, K, G])
    model.set_section([H, K, F])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, E, K, H])
    model.set_polygon([K, F, C, G])
    model.set_polygon([E, B, F, K])
    model.set_polygon([H, K, G, D])
    model.set_polygon([A, B, C])
    model.set_polygon([A, C, D])
    model.set_polygon([A, E, K])
    model.set_polygon([A, H, K])
    model.set_polygon([K, F, C])
    model.set_polygon([K, G, C])

    return model


if __name__ == "__main__":
    construct_0354_g1()
