"""Programmatic construction for Book XIII, Proposition 2 (0447.g1).

If the square on a straight line be five times the square on a segment of it,
then, when the double of the said segment is cut in extreme and mean ratio,
the greater segment is the remaining part of the original straight line.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0447_g1() -> Model:
    """Construct the figure for Book XIII, Proposition 2 using geometor.model."""
    model = Model("0447.g1")

    # Straight line AB with segment AC, and CD = 2 AC
    A = model.set_point(15.0, -172.0, classes=["given"], label="A")
    C = model.set_point(79.0, -172.0, classes=["given"], label="C")
    B = model.set_point(163.0, -172.0, classes=["given"], label="B")
    D = model.set_point(214.0, -172.0, classes=["given"], label="D")

    model.construct_line(A, D)
    model.set_segment(A, D)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, D)
    model.set_segment(C, B)
    model.set_segment(B, D)

    # Square ALFB (AF) on AB, divided through C and H
    L = model.set_point(15.0, -24.0, label="L")
    R = model.set_point(79.0, -24.0, label="R")
    F = model.set_point(163.0, -24.0, label="F")
    P = model.set_point(15.0, -108.0, label="P")
    H = model.set_point(79.0, -108.0, label="H")
    Q = model.set_point(163.0, -108.0, label="Q")

    # Square CDGK (CG) on CD, divided by BE
    K = model.set_point(79.0, -307.0, label="K")
    E = model.set_point(163.0, -307.0, label="E")
    G = model.set_point(214.0, -307.0, label="G")

    # Horizontal segments in AF and CG
    model.set_segment(L, F)
    model.set_segment(L, R)
    model.set_segment(R, F)
    model.set_segment(P, Q)
    model.set_segment(P, H)
    model.set_segment(H, Q)
    model.set_segment(K, G)
    model.set_segment(K, E)
    model.set_segment(E, G)

    # Vertical segments in AF and CG
    model.set_segment(L, A)
    model.set_segment(L, P)
    model.set_segment(P, A)
    model.set_segment(R, K)
    model.set_segment(R, H)
    model.set_segment(H, C)
    model.set_segment(C, K)
    model.set_segment(F, E)
    model.set_segment(F, Q)
    model.set_segment(Q, B)
    model.set_segment(B, E)
    model.set_segment(D, G)

    # Diagonal AF
    model.set_segment(A, F)
    model.set_segment(A, H)
    model.set_segment(H, F)

    # Polygons (squares, rectangles, and gnomon MNO)
    model.set_polygon([A, L, F, B])
    model.set_polygon([C, D, G, K])
    model.set_polygon([A, P, H, C])
    model.set_polygon([H, R, F, Q])
    model.set_polygon([P, L, R, H])
    model.set_polygon([C, H, Q, B])
    model.set_polygon([C, B, E, K])
    model.set_polygon([B, D, G, E])
    model.set_polygon([P, L, F, B, C, H])

    return model


if __name__ == "__main__":
    construct_0447_g1()
