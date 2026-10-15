"""Programmatic construction for Book VI, Proposition 3 Commentary (0205.g1).

Analysis and synthesis of the Circle of Apollonius (Aristotle and Eutocius).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0205_g1() -> Model:
    """Construct the figure for 0205.g1 (VI.3 commentary) using geometor.model."""
    model = Model("0205.g1")

    # 1. Points
    B = model.set_point(20, -197, classes=["given"], label="B")
    D = model.set_point(110.93, -197, label="D")
    C = model.set_point(168, -197, classes=["given"], label="C")
    O = model.set_point(264.19, -197, label="O")
    E = model.set_point(417.45, -197, label="E")
    P = model.set_point(136, -113, label="P")
    L = model.set_point(213.69, -163.91, label="L")

    # 2. Construction Lines & Circles
    model.construct_line(B, E)
    model.construct_circle(O, D)

    # 3. Segments
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(C, O)
    model.set_segment(O, E)
    model.set_segment(B, C)
    model.set_segment(D, O)
    model.set_segment(C, E)
    model.set_segment(D, E)
    model.set_segment(B, O)
    model.set_segment(B, E)
    model.set_segment(B, P)
    model.set_segment(P, D)
    model.set_segment(P, C)
    model.set_segment(P, L)
    model.set_segment(L, O)
    model.set_segment(P, O)
    model.set_segment(P, E)
    model.set_segment(C, L)

    # 4. Collinear Sections
    model.set_section([B, D, C])
    model.set_section([D, C, O])
    model.set_section([C, O, E])
    model.set_section([P, L, O])

    # 5. Polygons (Triangles)
    model.set_polygon([B, O, P])
    model.set_polygon([P, O, C])
    model.set_polygon([B, P, C])
    model.set_polygon([P, C, L])
    model.set_polygon([C, O, L])
    model.set_polygon([P, D, E])

    # 6. Angles (Wedges)
    model.set_wedge(O, B, B, P)
    model.set_wedge(P, O, O, C)
    model.set_wedge(B, O, O, P)
    model.set_wedge(P, B, B, C)
    model.set_wedge(C, L, L, P)

    return model


if __name__ == "__main__":
    construct_0205_g1()
