"""Programmatic construction for Book VI, Proposition 20 Alternative Proof (0244.g1).

Alternative proof that the similar triangles into which similar polygons ABCDE,
FGHKL are divided have the same ratio to one another as the wholes.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0244_g1() -> Model:
    """Construct the figure for 0244.g1 (VI.20 alt.) using geometor.model."""
    model = Model("0244.g1")

    # 1. Points of similar pentagons ABCDE and FGHKL
    A = model.set_point(39.0, -60.0, classes=["given"], label="A")
    B = model.set_point(26.0, -115.0, classes=["given"], label="B")
    C = model.set_point(68.0, -163.0, classes=["given"], label="C")
    D = model.set_point(137.0, -163.0, classes=["given"], label="D")
    E = model.set_point(139.0, -108.0, classes=["given"], label="E")

    F = model.set_point(238.0, -22.0, classes=["given"], label="F")
    G = model.set_point(220.0, -97.0, classes=["given"], label="G")
    H = model.set_point(277.0, -162.0, classes=["given"], label="H")
    K = model.set_point(371.0, -162.0, classes=["given"], label="K")
    L = model.set_point(375.0, -87.0, classes=["given"], label="L")

    # 2. Segments of pentagon ABCDE and diagonals BE, EC
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, A)
    model.set_segment(B, E)
    model.set_segment(E, C)

    # 3. Segments of pentagon FGHKL and diagonals GL, LH
    model.set_segment(F, G)
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(K, L)
    model.set_segment(L, F)
    model.set_segment(G, L)
    model.set_segment(L, H)

    # 4. Polygons (Pentagons and Triangles)
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([F, G, H, K, L])

    model.set_polygon([A, B, E])
    model.set_polygon([E, B, C])
    model.set_polygon([E, C, D])

    model.set_polygon([F, G, L])
    model.set_polygon([L, G, H])
    model.set_polygon([L, H, K])

    return model


if __name__ == "__main__":
    construct_0244_g1()
