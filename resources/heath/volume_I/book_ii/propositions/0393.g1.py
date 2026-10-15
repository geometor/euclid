"""Programmatic construction for Book II, Proposition 4 (0393.g1).

If a straight line be cut at random, the square on the whole is equal to the
squares on the segments and twice the rectangle contained by the segments.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0393_g1() -> Model:
    """Construct the figure for Book II, Proposition 4 using geometor.model."""
    model = Model("0393.g1")

    # Straight line AB cut at random at C
    A = model.set_point(28.5, -29.5, classes=["given"], label="A")
    C = model.set_point(124.5, -29.5, classes=["given"], label="C")
    B = model.set_point(170.5, -29.5, classes=["given"], label="B")

    model.construct_line(A, B)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Square ADEB described on AB [I. 46], diagonal BD joined
    D = model.set_point(28.5, -171.5, label="D")
    E = model.set_point(170.5, -171.5, label="E")

    model.set_segment(A, D)
    model.set_segment(D, E)
    model.set_segment(B, E)
    model.set_polygon([A, D, E, B])

    model.construct_line(B, D)
    model.set_segment(B, D)

    # Parallel CF to AD/EB through C, meeting BD at G and DE at F [I. 31]
    G = model.set_point(124.5, -75.5, label="G")
    F = model.set_point(124.5, -171.5, label="F")
    model.construct_line(C, F)
    model.set_segment(C, F)
    model.set_segment(C, G)
    model.set_segment(G, F)
    model.set_segment(D, F)
    model.set_segment(F, E)
    model.set_segment(B, G)
    model.set_segment(G, D)

    # Parallel HK to AB/DE through G, meeting AD at H and BE at K [I. 31]
    H = model.set_point(28.5, -75.5, label="H")
    K = model.set_point(170.5, -75.5, label="K")
    model.construct_line(H, K)
    model.set_segment(H, K)
    model.set_segment(H, G)
    model.set_segment(G, K)
    model.set_segment(A, H)
    model.set_segment(H, D)
    model.set_segment(B, K)
    model.set_segment(K, E)

    # Squares about diameter: CGKB (CK) on CB and HDFG (HF) on AC
    model.set_polygon([C, G, K, B])
    model.set_polygon([H, D, F, G])

    # Complements AG (ACGH) and GE (GKEF), plus composite rectangles AF (ACFD) and FK (HKEF)
    model.set_polygon([A, C, G, H])
    model.set_polygon([G, K, E, F])
    model.set_polygon([A, C, F, D])
    model.set_polygon([H, K, E, D])

    # Gnomon around CK: A C G K E D
    model.set_polygon([A, C, G, K, E, D])

    # Referenced triangles ABD, CGB, GDF
    model.set_polygon([A, B, D])
    model.set_polygon([C, G, B])
    model.set_polygon([H, G, D])

    # Referenced angles CGB, ADB, ABD, GBC, KBC, GCB, CGK, GKB
    model.set_wedge(G, C, C, B)  # < C G B )
    model.set_wedge(D, A, A, B)  # < A D B )
    model.set_wedge(B, A, A, D)  # < A B D ) / < G B C )
    model.set_wedge(B, K, K, C)  # < K B C )
    model.set_wedge(C, G, G, B)  # < G C B )
    model.set_wedge(G, C, C, K)  # < C G K )
    model.set_wedge(K, G, G, B)  # < G K B )

    return model


if __name__ == "__main__":
    construct_0393_g1()
