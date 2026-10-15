"""Programmatic construction for Book XIII, Proposition 14 Commentary (0481.g1).

Pappus' inscription of a regular octahedron ABCDEF in a sphere using two
equal and parallel circular sections ABC and DEF, with square ABFE and
sphere diameter AF.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0481_g1() -> Model:
    """Construct the figure 0481.g1 using geometor.model."""
    model = Model("0481.g1")

    # Sphere centre and boundary
    O = model.set_point(118.0, -118.0, classes=["auxiliary"], label="O")
    S_top = model.set_point(118.0, -20.0, classes=["auxiliary"], label="S_top")
    model.construct_circle(O, S_top)

    # Upper circular section vertices D, E, F
    D = model.set_point(76.0, -70.0, classes=["given"], label="D")
    E = model.set_point(66.0, -42.0, classes=["given"], label="E")
    F = model.set_point(188.0, -49.0, classes=["given"], label="F")

    # Lower circular section vertices A, B, C
    A = model.set_point(48.0, -187.0, classes=["given"], label="A")
    B = model.set_point(170.0, -194.0, classes=["given"], label="B")
    C = model.set_point(160.0, -166.0, classes=["given"], label="C")

    # Polygons (Octahedron, Square ABFE, Triangles ABC and DEF)
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([A, B, F, E])
    model.set_polygon([A, D, B])
    model.set_polygon([A, D, E])
    model.set_polygon([B, D, F])
    model.set_polygon([A, E, F, B, C, D])

    # Segments
    for p1, p2 in [
        (D, E), (E, F), (F, D),
        (A, B), (B, C), (C, A),
        (A, E), (A, D), (D, B), (B, F),
        (A, F), (E, C), (F, C),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0481_g1()
