"""Programmatic construction for Book II, Proposition 9 (0406.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0406_g1() -> Model:
    """Construct the figure for 0406.g1 (II.9) using geometor.model."""
    model = Model("0406.g1")

    # 1. Points
    A = model.set_point(24.0, -156.0, classes=["given"], label="A")
    C = model.set_point(146.0, -156.0, classes=["given"], label="C")
    D = model.set_point(188.0, -156.0, classes=["given"], label="D")
    B = model.set_point(268.0, -156.0, classes=["given"], label="B")

    E = model.set_point(146.0, -34.0, label="E")
    G = model.set_point(146.0, -76.0, label="G")
    F = model.set_point(188.0, -76.0, label="F")

    # 2. Segments
    model.set_segment(A, C)
    model.set_segment(C, D)
    model.set_segment(D, B)
    model.set_segment(C, B)
    model.set_segment(A, D)
    model.set_segment(A, B)

    model.set_segment(C, G)
    model.set_segment(G, E)
    model.set_segment(C, E)

    model.set_segment(D, F)
    model.set_segment(G, F)

    model.set_segment(E, A)
    model.set_segment(E, F)
    model.set_segment(F, B)
    model.set_segment(E, B)
    model.set_segment(A, F)

    # 3. Collinear Sections
    model.set_section([A, C, D])
    model.set_section([C, D, B])
    model.set_section([A, D, B])
    model.set_section([A, C, B])
    model.set_section([C, G, E])
    model.set_section([E, F, B])

    # 4. Polygons (Triangles & Parallelogram)
    model.set_polygon([A, C, E])
    model.set_polygon([E, C, B])
    model.set_polygon([A, E, B])
    model.set_polygon([E, G, F])
    model.set_polygon([F, D, B])
    model.set_polygon([A, E, F])
    model.set_polygon([A, D, F])
    model.set_polygon([C, D, F, G])

    # 5. Angles (Wedges)
    model.set_wedge(A, C, E, C)  # < E A C )
    model.set_wedge(E, A, A, C)  # < A E C )
    model.set_wedge(C, A, A, E)  # < A C E )
    model.set_wedge(C, E, E, B)  # < E C B )
    model.set_wedge(E, C, C, B)  # < C E B )
    model.set_wedge(B, E, E, C)  # < E B C )
    model.set_wedge(E, A, A, B)  # < A E B )
    model.set_wedge(E, G, G, F)  # < G E F )
    model.set_wedge(G, E, E, F)  # < E G F )
    model.set_wedge(F, E, E, G)  # < E F G )
    model.set_wedge(D, F, F, B)  # < F D B )
    model.set_wedge(F, B, B, D)  # < B F D )
    model.set_wedge(E, A, A, F)  # < A E F )
    model.set_wedge(D, A, A, F)  # < A D F )

    return model


if __name__ == "__main__":
    construct_0406_g1()
