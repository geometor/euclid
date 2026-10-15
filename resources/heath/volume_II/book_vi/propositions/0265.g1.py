"""Programmatic construction for Book VI, Proposition 27 Commentary (0265.g1).

Algebraic interpretation of the diorismos (maximum area condition) using rectangles.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0265_g1() -> Model:
    """Construct the figure for 0265.g1 (VI.27 commentary) using geometor.model."""
    model = Model("0265.g1")

    # 1. Points
    A = model.set_point(28, -115, classes=["given"], label="A")
    C = model.set_point(96, -115, label="C")
    K = model.set_point(116, -115, label="K")
    B = model.set_point(164, -115, classes=["given"], label="B")

    G = model.set_point(28, -55, label="G")
    C1 = model.set_point(96, -55, label="C1")
    F = model.set_point(116, -55, label="F")
    H = model.set_point(164, -55, label="H")

    A1 = model.set_point(28, -30, label="A1")
    D = model.set_point(96, -30, label="D")
    E = model.set_point(164, -30, label="E")

    # 2. Construction Lines
    model.construct_line(A, B)
    model.construct_line(B, D)

    # 3. Segments
    model.set_segment(A, C)
    model.set_segment(C, K)
    model.set_segment(K, B)
    model.set_segment(A, K)
    model.set_segment(C, B)
    model.set_segment(A, B)

    model.set_segment(G, C1)
    model.set_segment(C1, F)
    model.set_segment(F, H)
    model.set_segment(G, F)
    model.set_segment(C1, H)
    model.set_segment(G, H)

    model.set_segment(A1, D)
    model.set_segment(D, E)
    model.set_segment(A1, E)

    model.set_segment(A1, G)
    model.set_segment(G, A)
    model.set_segment(A1, A)

    model.set_segment(D, C1)
    model.set_segment(C1, C)
    model.set_segment(D, C)

    model.set_segment(F, K)

    model.set_segment(E, H)
    model.set_segment(H, B)
    model.set_segment(E, B)

    model.set_segment(D, F)
    model.set_segment(F, B)
    model.set_segment(D, B)

    # 4. Collinear Sections
    model.set_section([A, C, B])
    model.set_section([A, K, B])
    model.set_section([G, F, H])
    model.set_section([D, F, B])

    # 5. Polygons (Rectangles & Triangles)
    model.set_polygon([A, K, F, G])  # AKFG / AF
    model.set_polygon([C, B, E, D])  # CE / DB
    model.set_polygon([A, C, D, A1])  # AD
    model.set_polygon([K, B, H, F])  # KBHF / FB
    model.set_polygon([A, B, E, A1])  # AE
    model.set_polygon([A, B, H, G])  # AH
    model.set_polygon([C, B, D])
    model.set_polygon([K, B, F])

    return model


if __name__ == "__main__":
    construct_0265_g1()
