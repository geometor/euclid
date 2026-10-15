"""Programmatic construction for Book XIII, Proposition 5 (0452.g1).

If a straight line be cut in extreme and mean ratio, and there be added to it
a straight line equal to the greater segment, the whole straight line has been
cut in extreme and mean ratio, and the original straight line is the greater
segment.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0452_g1() -> Model:
    """Construct the figure for Book XIII, Proposition 5 using geometor.model."""
    model = Model("0452.g1")

    # Straight line AB cut in extreme and mean ratio at C, with AD = AC
    D = model.set_point(12.0, -26.0, classes=["given"], label="D")
    A = model.set_point(93.0, -26.0, classes=["given"], label="A")
    C = model.set_point(174.0, -26.0, classes=["given"], label="C")
    B = model.set_point(228.0, -26.0, classes=["given"], label="B")

    model.construct_line(D, B)
    model.set_segment(D, B)
    model.set_segment(D, C)
    model.set_segment(D, A)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Grid points of square AE on AB and square DH on AD
    L = model.set_point(12.0, -107.0, label="L")
    H = model.set_point(93.0, -107.0, label="H")
    F = model.set_point(174.0, -107.0, label="F")
    K = model.set_point(228.0, -107.0, label="K")

    M = model.set_point(93.0, -161.0, label="M")
    G = model.set_point(174.0, -161.0, label="G")
    E = model.set_point(228.0, -161.0, label="E")

    # Horizontal segments
    model.set_segment(L, K)
    model.set_segment(L, H)
    model.set_segment(H, F)
    model.set_segment(F, K)
    model.set_segment(M, E)
    model.set_segment(M, G)
    model.set_segment(G, E)

    # Vertical segments
    model.set_segment(D, L)
    model.set_segment(A, M)
    model.set_segment(A, H)
    model.set_segment(H, M)
    model.set_segment(C, G)
    model.set_segment(C, F)
    model.set_segment(F, G)
    model.set_segment(B, E)
    model.set_segment(B, K)
    model.set_segment(K, E)

    # Diagonal AE
    model.set_segment(A, E)
    model.set_segment(A, F)
    model.set_segment(F, E)

    # Polygons (squares and rectangles)
    model.set_polygon([A, B, E, M])
    model.set_polygon([D, B, K, L])
    model.set_polygon([D, A, H, L])
    model.set_polygon([A, C, F, H])
    model.set_polygon([C, B, E, G])
    model.set_polygon([H, K, E, M])
    model.set_polygon([A, B, K, H])
    model.set_polygon([C, B, K, F])
    model.set_polygon([H, F, G, M])
    model.set_polygon([F, K, E, G])

    return model


if __name__ == "__main__":
    construct_0452_g1()
