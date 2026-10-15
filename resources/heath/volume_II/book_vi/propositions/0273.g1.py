"""Programmatic construction for Book VI, Proposition 30 (0273.g1).

To cut a given finite straight line AB in extreme and mean ratio at E.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0273_g1() -> Model:
    """Construct the figure for 0273.g1 (VI.30) using geometor.model."""
    model = Model("0273.g1")

    # 1. Points
    A = model.set_point(27.0, -132.0, classes=["given"], label="A")
    B = model.set_point(129.0, -132.0, classes=["given"], label="B")
    C = model.set_point(27.0, -29.0, label="C")
    F = model.set_point(91.0, -29.0, label="F")
    H = model.set_point(129.0, -29.0, label="H")
    E = model.set_point(91.0, -132.0, label="E")
    G = model.set_point(27.0, -196.0, label="G")
    D = model.set_point(91.0, -196.0, label="D")

    # 2. Construction Lines
    model.construct_line(A, B)
    model.construct_line(C, G)
    model.construct_line(F, D)
    model.construct_line(C, H)

    # 3. Segments
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(A, B)

    model.set_segment(C, F)
    model.set_segment(F, H)
    model.set_segment(C, H)

    model.set_segment(G, D)

    model.set_segment(C, A)
    model.set_segment(A, G)
    model.set_segment(C, G)

    model.set_segment(F, E)
    model.set_segment(E, D)
    model.set_segment(F, D)

    model.set_segment(H, B)
    model.set_segment(B, C)

    # 4. Collinear Sections
    model.set_section([A, E, B])
    model.set_section([C, F, H])
    model.set_section([C, A, G])
    model.set_section([F, E, D])

    # 5. Polygons (Squares & Rectangles)
    model.set_polygon([C, H, B, A])  # Square BC
    model.set_polygon([C, F, D, G])  # Parallelogram CD
    model.set_polygon([A, E, D, G])  # Square AD
    model.set_polygon([C, F, E, A])  # Rectangle CE
    model.set_polygon([F, H, B, E])  # Remainder BF

    return model


if __name__ == "__main__":
    construct_0273_g1()
