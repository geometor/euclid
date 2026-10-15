"""Programmatic construction for Book IV, Proposition 10 (0102.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0102_g1() -> Model:
    """Construct the figure 0102.g1 (Golden Triangle) using geometor.model."""
    model = Model("0102.g1")

    # Points (y-inverted for standard mathematical coordinates)
    A = model.set_point(114.00, -115.00, classes=["given"], label="A")
    B = model.set_point(174.18, -35.14, classes=["given"], label="B")
    C = model.set_point(151.19, -65.64, label="C")
    D = model.set_point(209.63, -85.76, label="D")
    E = model.set_point(208.59, -144.88, label="E")
    O = model.set_point(166.57, -115.92, label="O")

    # Circles: BDE (centre A, radius AB) and circumscribed circle ACD (centre O, radius OA)
    model.construct_circle(A, B)
    model.construct_circle(O, A)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(A, D)
    model.set_segment(B, D)
    model.set_segment(C, D)

    # Golden section on AB at C
    model.set_section([A, C, B], classes=["golden"])

    # Polygons
    model.set_polygon([A, B, D])
    model.set_polygon([A, C, D])
    model.set_polygon([B, C, D])

    # Angles (wedges)
    model.set_wedge(D, B, B, C)
    model.set_wedge(C, D, D, A)
    model.set_wedge(A, D, D, C)
    model.set_wedge(A, D, D, B)
    model.set_wedge(D, C, C, B)
    model.set_wedge(B, B, C, D)
    model.set_wedge(B, A, D, B)

    return model


if __name__ == "__main__":
    construct_0102_g1()
