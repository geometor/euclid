"""Programmatic construction for Book VI, Proposition 1 (0197.g1).

Triangles and parallelograms which are under the same height are to one another as their bases.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0197_g1() -> Model:
    """Construct the figure for 0197.g1 (VI.1) using geometor.model."""
    model = Model("0197.g1")

    # 1. Points
    E = model.set_point(115, -30, classes=["given"], label="E")
    A = model.set_point(148, -30, classes=["given"], label="A")
    F = model.set_point(204, -30, classes=["given"], label="F")
    H = model.set_point(19, -149, label="H")
    G = model.set_point(52, -149, label="G")
    B = model.set_point(84, -149, classes=["given"], label="B")
    C = model.set_point(117, -149, classes=["given"], label="C")
    D = model.set_point(173, -149, classes=["given"], label="D")
    K = model.set_point(229, -149, label="K")
    L = model.set_point(286, -149, label="L")

    # 2. Construction Lines
    model.construct_line(B, D)

    # 3. Segments
    # Top parallel segments
    model.set_segment(E, A)
    model.set_segment(A, F)
    model.set_segment(E, F)

    # Parallelogram sides and rays from A
    model.set_segment(E, B)
    model.set_segment(F, D)
    model.set_segment(A, H)
    model.set_segment(A, G)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(A, K)
    model.set_segment(A, L)

    # Base segments and collinear sub-segments
    model.set_segment(H, G)
    model.set_segment(G, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, K)
    model.set_segment(K, L)
    model.set_segment(B, D)
    model.set_segment(H, C)
    model.set_segment(C, L)
    model.set_segment(H, L)

    # 4. Collinear Sections
    model.set_section([E, A, F])
    model.set_section([H, G, B])
    model.set_section([G, B, C])
    model.set_section([B, C, D])
    model.set_section([C, D, K])
    model.set_section([D, K, L])
    model.set_section([H, C, L])

    # 5. Polygons (Triangles and Parallelograms)
    model.set_polygon([A, B, C])
    model.set_polygon([A, C, D])
    model.set_polygon([A, G, B])
    model.set_polygon([A, H, G])
    model.set_polygon([A, H, C])
    model.set_polygon([A, L, C])
    model.set_polygon([A, D, K])
    model.set_polygon([A, K, L])
    model.set_polygon([E, B, C, A])
    model.set_polygon([A, C, D, F])

    return model


if __name__ == "__main__":
    construct_0197_g1()
