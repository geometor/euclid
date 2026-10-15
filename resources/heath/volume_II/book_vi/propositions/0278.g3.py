"""Programmatic construction for Book VI, Proposition 32 Commentary (0278.g3).

Taylor's substitute theorem: If two triangles ABC, DEF have sides parallel in pairs,
the straight lines AD, BE, CF joining the corresponding vertices meet in a point G.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0278_g3() -> Model:
    """Construct the figure for 0278.g3 (VI.32 commentary) using geometor.model."""
    model = Model("0278.g3")

    # 1. Points
    A = model.set_point(22.0, -29.0, classes=["given"], label="A")
    B = model.set_point(74.0, -54.0, classes=["given"], label="B")
    C = model.set_point(19.0, -113.0, classes=["given"], label="C")
    D = model.set_point(111.0, -29.0, classes=["given"], label="D")
    E = model.set_point(144.0, -44.0, classes=["given"], label="E")
    F = model.set_point(109.0, -80.0, classes=["given"], label="F")
    G = model.set_point(245.0, -29.0, label="G")

    # 2. Construction Lines (Perspective rays meeting at G)
    model.construct_line(A, G)
    model.construct_line(B, G)
    model.construct_line(C, G)

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)

    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, D)

    model.set_segment(A, D)
    model.set_segment(D, G)
    model.set_segment(A, G)

    model.set_segment(B, E)
    model.set_segment(E, G)
    model.set_segment(B, G)

    model.set_segment(C, F)
    model.set_segment(F, G)
    model.set_segment(C, G)

    # 4. Collinear Sections
    model.set_section([A, D, G])
    model.set_section([B, E, G])
    model.set_section([C, F, G])

    # 5. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])

    return model


if __name__ == "__main__":
    construct_0278_g3()
