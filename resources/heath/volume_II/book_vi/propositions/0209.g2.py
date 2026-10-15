"""Programmatic construction for Book VI, Proposition 5 (0209.g2).

Triangles DEF and GEF constructed on common side EF in Proposition 5.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0209_g2() -> Model:
    """Construct the figure for 0209.g2 (VI.5) using geometor.model."""
    model = Model("0209.g2")

    # 1. Points
    D = model.set_point(84, -29, classes=["given"], label="D")
    E = model.set_point(27, -83, classes=["given"], label="E")
    F = model.set_point(69, -75, classes=["given"], label="F")
    G = model.set_point(105, -106, label="G")

    # 3. Segments
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, D)
    model.set_segment(G, E)
    model.set_segment(G, F)

    # 5. Polygons (Triangles)
    model.set_polygon([D, E, F])
    model.set_polygon([G, E, F])

    # 6. Angles (Wedges)
    model.set_wedge(D, E, E, F)
    model.set_wedge(E, D, D, F)
    model.set_wedge(F, D, D, E)
    model.set_wedge(E, F, F, G)
    model.set_wedge(F, E, E, G)
    model.set_wedge(G, E, E, F)

    return model


if __name__ == "__main__":
    construct_0209_g2()
