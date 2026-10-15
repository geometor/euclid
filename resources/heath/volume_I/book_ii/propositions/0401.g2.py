"""Programmatic construction for Book II, Proposition 6 commentary (0401.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0401_g2() -> Model:
    """Construct the figure for 0401.g2 (II.6 Simson commentary) using geometor.model."""
    model = Model("0401.g2")

    # 1. Points
    A = model.set_point(18.0, -107.0, classes=["given"], label="A")
    C = model.set_point(104.0, -107.0, classes=["given"], label="C")
    B = model.set_point(190.0, -107.0, classes=["given"], label="B")
    D = model.set_point(218.0, -107.0, label="D")
    Q = model.set_point(190.0, -32.0, label="Q")

    K = model.set_point(18.0, -135.0, label="K")
    L = model.set_point(104.0, -135.0, label="L")
    M = model.set_point(190.0, -135.0, label="M")
    H = model.set_point(218.0, -135.0, label="H")

    E = model.set_point(104.0, -221.0, label="E")
    G = model.set_point(190.0, -221.0, label="G")
    F = model.set_point(218.0, -221.0, label="F")

    N = model.set_point(162.0, -124.0, label="N")
    O = model.set_point(204.0, -118.0, label="O")
    P = model.set_point(200.0, -158.0, label="P")

    # 2. Circle arc (C, Q) cutting AB produced in D
    model.construct_circle(C, Q)

    # 3. Segments
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(B, D)
    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(A, D)

    model.set_segment(B, Q)
    model.set_segment(C, Q)

    model.set_segment(K, L)
    model.set_segment(L, M)
    model.set_segment(M, H)
    model.set_segment(K, H)

    model.set_segment(E, G)
    model.set_segment(G, F)
    model.set_segment(E, F)

    model.set_segment(A, K)
    model.set_segment(C, L)
    model.set_segment(L, E)
    model.set_segment(C, E)
    model.set_segment(B, M)
    model.set_segment(M, G)
    model.set_segment(B, G)
    model.set_segment(D, H)
    model.set_segment(H, F)
    model.set_segment(D, F)
    model.set_segment(D, E)

    # 4. Collinear Sections
    model.set_section([A, C, B])
    model.set_section([C, B, D])
    model.set_section([A, B, D])

    # 5. Polygons (Rectangles, Squares, Gnomon, Right Triangle)
    model.set_polygon([C, B, Q])
    model.set_polygon([A, D, H, K])
    model.set_polygon([C, E, F, D])
    model.set_polygon([L, E, G, M])
    model.set_polygon([C, D, F, G, M, L])
    model.set_polygon([N, O, P])

    return model


if __name__ == "__main__":
    construct_0401_g2()
