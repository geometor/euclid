"""Programmatic construction for Book VI, Proposition 15, supplementary case (0227.g1).

Two triangles ABC, ADE with supplementary angles BAC, DAE and reciprocally
proportional sides CA : AD = EA : AB.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0227_g1() -> Model:
    """Construct the figure for 0227.g1 (VI.15 note) using geometor.model."""
    model = Model("0227.g1")

    # 1. Points
    C = model.set_point(19.0, -114.0, classes=["given"], label="C")
    A = model.set_point(78.0, -114.0, classes=["given"], label="A")
    D = model.set_point(177.0, -114.0, classes=["given"], label="D")
    B = model.set_point(104.0, -24.0, classes=["given"], label="B")
    E = model.set_point(94.9, -55.5, classes=["given"], label="E")

    # 2. Construction Lines
    model.construct_line(C, D)
    model.construct_line(A, B)

    # 3. Segments
    model.set_segment(C, A)
    model.set_segment(A, D)
    model.set_segment(C, D)

    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(A, B)

    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, E)

    # 4. Collinear Sections
    model.set_section([C, A, D])
    model.set_section([A, E, B])

    # 5. Polygons (Triangles)
    model.set_polygon([A, B, C])
    model.set_polygon([A, D, E])
    model.set_polygon([B, A, D])
    model.set_polygon([B, C, D])
    model.set_polygon([B, D, E])

    # 6. Angles / Wedges
    model.set_wedge(A, C, C, B)
    model.set_wedge(A, E, E, D)

    return model


if __name__ == "__main__":
    construct_0227_g1()
