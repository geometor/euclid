"""Programmatic construction for Book VI, Proposition 20 (0241.g1).

Similar polygons are divided into similar triangles, and into triangles equal in
multitude and in the same ratio as the wholes, and the polygon has to the polygon
a ratio duplicate of that which the corresponding side has to the corresponding side.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0241_g1() -> Model:
    """Construct the figure for 0241.g1 (VI.20) using geometor.model."""
    model = Model("0241.g1")

    # 1. Points of similar pentagons ABCDE and FGHKL
    A = model.set_point(66.0, -27.0, classes=["given"], label="A")
    B = model.set_point(28.0, -70.0, classes=["given"], label="B")
    C = model.set_point(66.0, -157.0, classes=["given"], label="C")
    D = model.set_point(177.0, -157.0, classes=["given"], label="D")
    E = model.set_point(193.0, -70.0, classes=["given"], label="E")
    M = model.set_point(66.0, -70.0, label="M")

    F = model.set_point(259.0, -61.0, classes=["given"], label="F")
    G = model.set_point(230.0, -94.0, classes=["given"], label="G")
    H = model.set_point(259.0, -157.0, classes=["given"], label="H")
    K = model.set_point(338.0, -157.0, classes=["given"], label="K")
    L = model.set_point(352.0, -94.0, classes=["given"], label="L")
    N = model.set_point(259.0, -94.0, label="N")

    # 2. Segments of pentagon ABCDE and diagonals
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, A)

    model.set_segment(B, E)
    model.set_segment(B, M)
    model.set_segment(M, E)
    model.set_segment(A, C)
    model.set_segment(A, M)
    model.set_segment(M, C)
    model.set_segment(E, C)
    model.set_segment(B, D)

    # 3. Segments of pentagon FGHKL and diagonals
    model.set_segment(F, G)
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(K, L)
    model.set_segment(L, F)

    model.set_segment(G, L)
    model.set_segment(G, N)
    model.set_segment(N, L)
    model.set_segment(F, H)
    model.set_segment(F, N)
    model.set_segment(N, H)
    model.set_segment(L, H)
    model.set_segment(G, K)

    # 4. Collinear Sections
    model.set_section([B, M, E])
    model.set_section([A, M, C])
    model.set_section([G, N, L])
    model.set_section([F, N, H])

    # 5. Polygons (Pentagons and Triangles)
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([F, G, H, K, L])

    model.set_polygon([A, B, E])
    model.set_polygon([E, B, C])
    model.set_polygon([E, C, D])
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, M])
    model.set_polygon([B, M, C])
    model.set_polygon([A, M, E])
    model.set_polygon([E, M, C])

    model.set_polygon([F, G, L])
    model.set_polygon([L, G, H])
    model.set_polygon([L, H, K])
    model.set_polygon([F, G, H])
    model.set_polygon([F, G, N])
    model.set_polygon([G, N, H])

    # 6. Angles
    model.set_wedge(A, B, B, E)  # < B A E )
    model.set_wedge(F, G, G, L)  # < G F L )
    model.set_wedge(B, A, A, E)  # < A B E ) / < A B M )
    model.set_wedge(G, F, F, L)  # < F G L ) / < F G N )
    model.set_wedge(B, A, A, C)  # < A B C )
    model.set_wedge(G, F, F, H)  # < F G H )
    model.set_wedge(B, E, E, C)  # < E B C )
    model.set_wedge(G, L, L, H)  # < L G H )
    model.set_wedge(A, B, B, C)  # < B A C ) / < B A M )
    model.set_wedge(F, G, G, H)  # < G F H ) / < G F N )
    model.set_wedge(C, B, B, A)  # < B C A )
    model.set_wedge(H, G, G, F)  # < G H F )
    model.set_wedge(M, A, A, B)  # < A M B )
    model.set_wedge(N, F, F, G)  # < F N G )

    return model


if __name__ == "__main__":
    construct_0241_g1()
