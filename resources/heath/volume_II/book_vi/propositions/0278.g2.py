"""Programmatic construction for Book VI, Proposition 32 Commentary (0278.g2).

Lachlan's substitute theorem: If two similar triangles ABC, DEF be placed so that
two sides of the one are parallel to the corresponding sides of the other,
the third sides are parallel.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0278_g2() -> Model:
    """Construct the figure for 0278.g2 (VI.32 commentary) using geometor.model."""
    model = Model("0278.g2")

    # 1. Points
    A = model.set_point(87.0, -41.0, classes=["given"], label="A")
    B = model.set_point(18.0, -119.0, classes=["given"], label="B")
    C = model.set_point(139.0, -119.0, classes=["given"], label="C")
    G = model.set_point(56.0, -76.0, label="G")
    H = model.set_point(110.33, -76.0, label="H")

    D = model.set_point(229.0, -27.0, classes=["given"], label="D")
    E = model.set_point(188.0, -76.0, classes=["given"], label="E")
    F = model.set_point(264.0, -76.0, classes=["given"], label="F")

    # 2. Construction Line
    model.construct_line(G, F)

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_segment(A, G)
    model.set_segment(G, B)
    model.set_segment(G, E)
    model.set_segment(G, F)

    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, D)

    # 4. Collinear Sections
    model.set_section([A, G, B])
    model.set_section([G, E, F])

    # 5. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([A, G, H])

    return model


if __name__ == "__main__":
    construct_0278_g2()
