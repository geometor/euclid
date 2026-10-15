"""Programmatic construction for Book I, Common Notions commentary (0254.g1).

Construction of a point M' on a circle such that the chord MM' is not greater than sigma.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0254_g1() -> Model:
    """Construct the figure for 0254.g1 using geometor.model."""
    model = Model("0254.g1")

    # Centre O, point M on circle, point P on tangent/secant from M, ray OQ meeting circle at M', and S on OP
    O = model.set_point(135, -132, classes=["given"], label="O")
    M = model.set_point(226, -79.5, classes=["given"], label="M")
    P = model.set_point(226, -52, classes=["given"], label="P")
    Mp = model.set_point(197.7, -47.8, classes=["given"], label="M'")
    Q = model.set_point(211, -30, classes=["given"], label="Q")
    S = model.set_point(211.85, -63.65, classes=["given"], label="S")

    # Circle and lines
    model.construct_circle(O, M)
    model.construct_line(M, P)
    model.construct_line(O, P)
    model.construct_line(O, Q)

    # Segments and sections
    model.set_segment(O, M)
    model.set_segment(M, P)
    model.set_segment(O, P)
    model.set_segment(O, S)
    model.set_segment(S, P)
    model.set_segment(O, Mp)
    model.set_segment(Mp, Q)
    model.set_segment(O, Q)
    model.set_segment(M, S)
    model.set_segment(S, Mp)
    model.set_segment(M, Mp)
    model.set_section([O, S, P])
    model.set_section([O, Mp, Q])
    model.set_section([M, S, Mp])

    # Polygons
    model.set_polygon([O, M, P])
    model.set_polygon([O, Mp, P])
    model.set_polygon([O, M, Mp])
    model.set_polygon([M, S, P])
    model.set_polygon([Mp, S, P])

    # Angles (Wedges)
    model.set_wedge(O, M, M, P)
    model.set_wedge(O, P, P, Q)
    model.set_wedge(O, M, M, Q)
    model.set_wedge(S, M, M, P)

    return model


if __name__ == "__main__":
    construct_0254_g1()
