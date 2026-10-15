"""Programmatic construction for Book VI, Proposition 6 (0211.g1).

If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles will be equiangular.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0211_g1() -> Model:
    """Construct the figure for 0211.g1 (VI.6) using geometor.model."""
    model = Model("0211.g1")

    # 1. Points
    A = model.set_point(38, -19, classes=["given"], label="A")
    B = model.set_point(26, -156, classes=["given"], label="B")
    C = model.set_point(122, -156, classes=["given"], label="C")
    D = model.set_point(212, -39, classes=["given"], label="D")
    E = model.set_point(204.56, -123.94, classes=["given"], label="E")
    F = model.set_point(264.08, -123.94, classes=["given"], label="F")
    G = model.set_point(291.08, -70.89, label="G")

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, D)
    model.set_segment(D, G)
    model.set_segment(G, F)

    # 5. Polygons (Triangles)
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([D, G, F])

    # 6. Angles (Wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, A, A, B)
    model.set_wedge(D, E, E, F)
    model.set_wedge(E, D, D, F)
    model.set_wedge(F, D, D, E)
    model.set_wedge(D, F, F, G)
    model.set_wedge(F, D, D, G)
    model.set_wedge(G, D, D, F)

    return model


if __name__ == "__main__":
    construct_0211_g1()
