"""Programmatic construction for Book II, Proposition 7 (0402.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0402_g1() -> Model:
    """Construct the figure for 0402.g1 (II.7) using geometor.model."""
    model = Model("0402.g1")

    # 1. Points
    A = model.set_point(27.0, -30.5, classes=["given"], label="A")
    C = model.set_point(130.0, -30.5, classes=["given"], label="C")
    B = model.set_point(170.5, -30.5, classes=["given"], label="B")

    H = model.set_point(27.0, -71.0, label="H")
    G = model.set_point(130.0, -71.0, label="G")
    F = model.set_point(170.5, -71.0, label="F")

    D = model.set_point(27.0, -174.0, label="D")
    N = model.set_point(130.0, -174.0, label="N")
    E = model.set_point(170.5, -174.0, label="E")

    # Gnomon markers
    K = model.set_point(105.0, -71.0, label="K")
    L = model.set_point(148.0, -53.0, label="L")
    M = model.set_point(130.0, -96.0, label="M")

    # 2. Segments
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(A, B)

    model.set_segment(H, G)
    model.set_segment(G, F)
    model.set_segment(H, F)

    model.set_segment(D, N)
    model.set_segment(N, E)
    model.set_segment(D, E)

    model.set_segment(A, H)
    model.set_segment(H, D)
    model.set_segment(A, D)

    model.set_segment(C, G)
    model.set_segment(G, N)
    model.set_segment(C, N)

    model.set_segment(B, F)
    model.set_segment(F, E)
    model.set_segment(B, E)

    model.set_segment(B, G)
    model.set_segment(G, D)
    model.set_segment(B, D)

    # 3. Collinear Sections
    model.set_section([A, C, B])
    model.set_section([H, G, F])
    model.set_section([D, N, E])
    model.set_section([A, H, D])
    model.set_section([C, G, N])
    model.set_section([B, F, E])
    model.set_section([B, G, D])

    # 4. Polygons (Squares, Rectangles, Gnomon)
    model.set_polygon([A, D, E, B])
    model.set_polygon([C, B, F, G])
    model.set_polygon([H, G, N, D])
    model.set_polygon([A, C, G, H])
    model.set_polygon([G, F, E, N])
    model.set_polygon([A, B, F, H])
    model.set_polygon([C, B, E, N])
    model.set_polygon([A, B, E, N, G, H])
    model.set_polygon([K, L, M])

    return model


if __name__ == "__main__":
    construct_0402_g1()
