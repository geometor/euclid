"""Programmatic construction for Book VI, Proposition 23 Commentary (0255.g1).

Data Propositions 56, 68, and 70: expressing the ratio of two equiangular
parallelograms AC, CF as the ratio of sides BC, CK by applying parallelogram DK
equal to CF.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0255_g1() -> Model:
    """Construct the figure for 0255.g1 (VI.23 Data commentary) using geometor.model."""
    model = Model("0255.g1")

    # 1. Points
    K2 = model.set_point(36.5, -31.0, label="K2")
    A = model.set_point(108.0, -31.0, classes=["given"], label="A")
    D = model.set_point(189.0, -31.0, classes=["given"], label="D")
    H = model.set_point(284.0, -31.0, label="H")

    K = model.set_point(30.5, -62.0, label="K")
    B = model.set_point(102.0, -62.0, classes=["given"], label="B")
    C = model.set_point(183.0, -62.0, classes=["given"], label="C")
    G = model.set_point(278.0, -62.0, classes=["given"], label="G")

    E = model.set_point(174.0, -112.0, classes=["given"], label="E")
    F = model.set_point(269.0, -112.0, classes=["given"], label="F")

    # 2. Construction lines
    model.construct_line(K, G)
    model.construct_line(D, E)

    # 3. Segments and sub-segments
    model.set_segment(K2, A)
    model.set_segment(A, D)
    model.set_segment(D, H)
    model.set_segment(K2, D)
    model.set_segment(A, H)

    model.set_segment(K, B)
    model.set_segment(B, C)
    model.set_segment(C, G)
    model.set_segment(K, C)
    model.set_segment(B, G)

    model.set_segment(E, F)

    model.set_segment(K2, K)
    model.set_segment(A, B)
    model.set_segment(D, C)
    model.set_segment(C, E)
    model.set_segment(D, E)
    model.set_segment(H, G)
    model.set_segment(G, F)
    model.set_segment(H, F)

    model.set_segment(D, G)
    model.set_segment(E, K)

    # 4. Parallelograms AC, CF, DK, AK, CH
    model.set_polygon([A, B, C, D])
    model.set_polygon([C, E, F, G])
    model.set_polygon([K2, K, C, D])
    model.set_polygon([K2, K, B, A])
    model.set_polygon([D, C, G, H])

    return model


if __name__ == "__main__":
    construct_0255_g1()
