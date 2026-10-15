"""Programmatic construction for Book VI, Proposition 24 (0257.g1).

In any parallelogram the parallelograms about the diameter are similar both to
the whole and to one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0257_g1() -> Model:
    """Construct the figure for 0257.g1 (VI.24) using geometor.model."""
    model = Model("0257.g1")

    # 1. Points of parallelogram ABCD, diameter AC, and parallels EK, GH through F
    A = model.set_point(27.0, -29.0, classes=["given"], label="A")
    E = model.set_point(73.0, -29.0, label="E")
    B = model.set_point(179.0, -29.0, classes=["given"], label="B")

    G = model.set_point(30.0, -60.0, label="G")
    F = model.set_point(76.0, -60.0, label="F")
    H = model.set_point(182.0, -60.0, label="H")

    D = model.set_point(35.0, -128.0, classes=["given"], label="D")
    K = model.set_point(81.0, -128.0, label="K")
    C = model.set_point(187.0, -128.0, classes=["given"], label="C")

    # 2. Construction lines
    model.construct_line(A, C)
    model.construct_line(G, H)
    model.construct_line(E, K)

    # 3. Segments and sub-segments
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)

    model.set_segment(G, H)
    model.set_segment(G, F)
    model.set_segment(F, H)

    model.set_segment(D, C)
    model.set_segment(D, K)
    model.set_segment(K, C)

    model.set_segment(A, D)
    model.set_segment(A, G)
    model.set_segment(G, D)

    model.set_segment(E, K)
    model.set_segment(E, F)
    model.set_segment(F, K)

    model.set_segment(B, C)
    model.set_segment(B, H)
    model.set_segment(H, C)

    model.set_segment(A, C)
    model.set_segment(A, F)
    model.set_segment(F, C)

    # 4. Collinear sections
    model.set_section([A, E, B])
    model.set_section([G, F, H])
    model.set_section([D, K, C])
    model.set_section([A, G, D])
    model.set_section([E, F, K])
    model.set_section([B, H, C])
    model.set_section([A, F, C])

    # 5. Parallelograms and Triangles
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, E, F, G])
    model.set_polygon([F, H, C, K])
    model.set_polygon([E, B, H, F])
    model.set_polygon([G, F, K, D])

    model.set_polygon([A, B, C])
    model.set_polygon([A, C, D])
    model.set_polygon([A, F, E])
    model.set_polygon([A, G, F])

    # 6. Angles
    model.set_wedge(A, B, B, D)  # < B A D )
    model.set_wedge(F, A, A, G)  # < A F G )
    model.set_wedge(C, D, D, A)  # < D C A )
    model.set_wedge(A, D, D, C)  # < D A C )

    return model


if __name__ == "__main__":
    construct_0257_g1()
