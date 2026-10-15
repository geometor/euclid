"""Programmatic construction for Book VI, Proposition 27 Commentary (0264.g1).

Locus of points on the diagonal for application of areas with defect or excess.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0264_g1() -> Model:
    """Construct the figure for 0264.g1 (VI.27 commentary) using geometor.model."""
    model = Model("0264.g1")

    # 1. Points
    A = model.set_point(33, -122, classes=["given"], label="A")
    C = model.set_point(138, -122, label="C")
    F = model.set_point(163, -122, label="F")
    B = model.set_point(222, -122, classes=["given"], label="B")
    L = model.set_point(271, -122, label="L")

    D = model.set_point(158, -74, label="D")
    D1 = model.set_point(242, -74, label="D1")

    A1 = model.set_point(48, -89, label="A1")
    E = model.set_point(177, -89, label="E")
    H = model.set_point(236, -89, label="H")

    M = model.set_point(19, -150, label="M")
    N = model.set_point(209, -150, label="N")
    K = model.set_point(259, -150, label="K")

    # 2. Construction Lines
    model.construct_line(A, B)
    model.construct_line(B, D)

    # 3. Segments
    model.set_segment(A, C)
    model.set_segment(C, F)
    model.set_segment(F, B)
    model.set_segment(B, L)
    model.set_segment(A, F)
    model.set_segment(C, B)
    model.set_segment(F, L)
    model.set_segment(A, B)
    model.set_segment(A, L)

    model.set_segment(C, D)
    model.set_segment(D, D1)
    model.set_segment(D1, H)
    model.set_segment(H, B)
    model.set_segment(B, N)
    model.set_segment(D1, B)
    model.set_segment(H, N)

    model.set_segment(D, E)
    model.set_segment(E, B)
    model.set_segment(B, K)
    model.set_segment(D, B)
    model.set_segment(E, K)
    model.set_segment(D, K)

    model.set_segment(A1, E)
    model.set_segment(E, H)
    model.set_segment(A1, H)
    model.set_segment(E, F)

    model.set_segment(A1, A)
    model.set_segment(A, M)
    model.set_segment(A1, M)

    model.set_segment(M, N)
    model.set_segment(N, K)
    model.set_segment(M, K)
    model.set_segment(K, L)

    # 4. Collinear Sections
    model.set_section([A, C, B])
    model.set_section([A, F, B])
    model.set_section([A, B, L])
    model.set_section([D, E, B])
    model.set_section([D, B, K])

    # 5. Polygons (Parallelograms)
    model.set_polygon([C, D, D1, B])  # BD
    model.set_polygon([F, E, H, B])  # BE
    model.set_polygon([A, A1, E, F])  # AE
    model.set_polygon([A, A1, H, B])  # AH
    model.set_polygon([B, L, K, N])  # BK
    model.set_polygon([A, L, K, M])  # AK
    model.set_polygon([A, B, N, M])  # AN
    model.set_polygon([A1, H, K, M])  # ML

    return model


if __name__ == "__main__":
    construct_0264_g1()
