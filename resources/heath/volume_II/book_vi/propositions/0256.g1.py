"""Programmatic construction for Book VI, Proposition 23 Pappus Commentary (0256.g1).

Pappus's proof that equiangular parallelograms AC, DF have the same ratio as the
rectangles contained by their adjacent sides.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0256_g1() -> Model:
    """Construct the figure for 0256.g1 (VI.23 Pappus) using geometor.model."""
    model = Model("0256.g1")

    # 1. Parallelogram AC on base BC with altitude AG
    A = model.set_point(44.0, -29.0, classes=["given"], label="A")
    A2 = model.set_point(137.0, -29.0, label="A2")
    C = model.set_point(111.0, -122.0, classes=["given"], label="C")
    G = model.set_point(44.0, -122.0, label="G")
    B = model.set_point(18.0, -122.0, classes=["given"], label="B")

    model.set_segment(A, A2)
    model.set_segment(A2, C)
    model.set_segment(B, C)
    model.set_segment(B, G)
    model.set_segment(G, C)
    model.set_segment(A, B)
    model.set_segment(A, G)

    model.set_polygon([A, B, C, A2])
    model.set_polygon([A, B, G])

    # 2. Parallelogram DF on base EF with altitude DH
    D = model.set_point(197.0, -44.0, classes=["given"], label="D")
    D2 = model.set_point(324.0, -44.0, label="D2")
    F = model.set_point(303.0, -122.0, classes=["given"], label="F")
    H = model.set_point(197.0, -122.0, label="H")
    E = model.set_point(176.0, -122.0, classes=["given"], label="E")

    model.set_segment(D, D2)
    model.set_segment(D2, F)
    model.set_segment(E, F)
    model.set_segment(E, H)
    model.set_segment(H, F)
    model.set_segment(D, E)
    model.set_segment(D, H)

    model.set_polygon([D, E, F, D2])
    model.set_polygon([D, E, H])

    # 3. Angles at B, G, E, H
    model.set_wedge(B, A, A, G)  # < A B G )
    model.set_wedge(G, A, A, B)  # < A G B )
    model.set_wedge(E, D, D, H)  # < D E H )
    model.set_wedge(H, D, D, E)  # < D H E )

    return model


if __name__ == "__main__":
    construct_0256_g1()
