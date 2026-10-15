"""Programmatic construction for Book VI, Proposition 18 (0235.g1).

Given rectilinear figure CE (quadrilateral CDEF) divided into two triangles
FCD and FDE by diagonal DF.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0235_g1() -> Model:
    """Construct the figure for 0235.g1 (VI.18, given figure CE) using geometor.model."""
    model = Model("0235.g1")

    # 1. Points
    C = model.set_point(20.0, -129.0, classes=["given"], label="C")
    D = model.set_point(135.0, -129.0, classes=["given"], label="D")
    E = model.set_point(116.0, -28.0, classes=["given"], label="E")
    F = model.set_point(46.0, -70.0, classes=["given"], label="F")

    # 2. Segments
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, C)
    model.set_segment(D, F)

    # 3. Polygons
    model.set_polygon([C, D, E, F])
    model.set_polygon([F, C, D])
    model.set_polygon([F, D, E])

    # 4. Angles / Wedges
    model.set_wedge(C, F, F, D)
    model.set_wedge(D, C, C, F)
    model.set_wedge(F, C, C, D)
    model.set_wedge(D, F, F, E)
    model.set_wedge(F, D, D, E)
    model.set_wedge(E, F, F, D)
    model.set_wedge(F, C, C, E)
    model.set_wedge(D, C, C, E)

    return model


if __name__ == "__main__":
    construct_0235_g1()
