"""Programmatic construction for Book VI, Proposition 14 Converse (0224.g1).

Equal parallelograms [triangles] which have the sides about one angle in each
reciprocally proportional are equiangular [have the angles included by those
sides either equal or supplementary].
"""

from __future__ import annotations

from geometor.model import Model


def construct_0224_g1() -> Model:
    """Construct the figure for 0224.g1 (VI.14-15 Converse) using geometor.model."""
    model = Model("0224.g1")

    # 1. Points (Left figure: A..K, Right figure: A2..K2)
    A = model.set_point(48.0, -212.0, classes=["given"], label="A")
    D = model.set_point(109.0, -212.0, classes=["given"], label="D")
    F = model.set_point(76.0, -130.0, classes=["given"], label="F")
    B = model.set_point(138.0, -130.0, classes=["given"], label="B")
    E = model.set_point(156.0, -74.0, classes=["given"], label="E")
    K = model.set_point(254.0, -74.0, label="K")
    H = model.set_point(236.0, -130.0, label="H")
    C = model.set_point(216.78, -185.15, classes=["given"], label="C")
    G = model.set_point(213.0, -196.0, classes=["given"], label="G")

    A2 = model.set_point(340.0, -211.0, classes=["given"], label="A'")
    D2 = model.set_point(402.0, -211.0, classes=["given"], label="D'")
    F2 = model.set_point(316.0, -126.0, classes=["given"], label="F'")
    B2 = model.set_point(378.0, -126.0, classes=["given"], label="B'")
    E2 = model.set_point(365.0, -71.0, classes=["given"], label="E'")
    C2 = model.set_point(452.0, -27.0, classes=["given"], label="C'")
    K2 = model.set_point(463.0, -71.0, label="K'")
    G2 = model.set_point(466.28, -81.36, classes=["given"], label="G'")
    H2 = model.set_point(478.0, -126.0, label="H'")

    # 2. Segments (Left figure)
    model.set_segment(A, D)
    model.set_segment(A, F)
    model.set_segment(F, D)
    model.set_segment(D, E)
    model.set_segment(D, B)
    model.set_segment(B, E)

    model.set_segment(F, H)
    model.set_segment(F, B)
    model.set_segment(B, H)

    model.set_segment(E, K)
    model.set_segment(E, H)
    model.set_segment(E, C)
    model.set_segment(E, G)
    model.set_segment(B, G)

    model.set_segment(K, G)
    model.set_segment(K, H)
    model.set_segment(H, C)
    model.set_segment(C, G)
    model.set_segment(H, G)

    # Segments (Right figure)
    model.set_segment(A2, D2)
    model.set_segment(A2, F2)
    model.set_segment(F2, D2)
    model.set_segment(D2, E2)
    model.set_segment(D2, B2)
    model.set_segment(B2, E2)
    model.set_segment(F2, H2)
    model.set_segment(F2, B2)
    model.set_segment(B2, H2)
    model.set_segment(E2, C2)
    model.set_segment(E2, K2)
    model.set_segment(E2, G2)
    model.set_segment(E2, H2)
    model.set_segment(B2, G2)
    model.set_segment(C2, H2)

    # 3. Collinear Sections
    model.set_section([D, B, E])
    model.set_section([F, B, H])
    model.set_section([G, C, H])
    model.set_section([C, H, K])

    # 4. Polygons
    model.set_polygon([F, A, D, B])
    model.set_polygon([E, B, G, C])
    model.set_polygon([E, B, H, K])
    model.set_polygon([F, B, D])
    model.set_polygon([E, B, G])
    model.set_polygon([E, B, H])
    model.set_polygon([B, G, H])

    # 5. Angles / Wedges
    model.set_wedge(B, F, F, D)
    model.set_wedge(B, E, E, G)
    model.set_wedge(B, D, D, H)
    model.set_wedge(G, B, B, H)
    model.set_wedge(H, B, B, G)

    return model


if __name__ == "__main__":
    construct_0224_g1()
