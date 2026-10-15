"""Programmatic construction for Book XI, Proposition 4 (0282.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0282_g1() -> Model:
    """Construct the figure 0282.g1 using geometor.model."""
    model = Model("0282.g1")

    # Plane of reference corners
    P1 = model.set_point(33.0, -60.0, classes=["plane_corner"])
    P2 = model.set_point(228.0, -60.0, classes=["plane_corner"])
    P3 = model.set_point(192.0, -155.0, classes=["plane_corner"])
    P4 = model.set_point(11.0, -155.0, classes=["plane_corner"])

    # Points in the plane of reference and elevated point F
    E = model.set_point(119.0, -107.0, classes=["given"], label="E")
    F = model.set_point(119.0, -22.0, classes=["given"], label="F")
    A = model.set_point(71.0, -86.0, classes=["given"], label="A")
    B = model.set_point(162.0, -125.81, classes=["given"], label="B")
    D = model.set_point(71.0, -131.0, classes=["given"], label="D")
    C = model.set_point(162.0, -85.5, classes=["given"], label="C")
    G = model.set_point(71.0, -103.0, label="G")
    H = model.set_point(162.0, -110.58, label="H")

    # Construction lines in the plane of reference
    model.construct_line(A, B)
    model.construct_line(C, D)
    model.construct_line(G, H)

    # Segments in the plane of reference
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(C, D)
    model.set_segment(C, E)
    model.set_segment(E, D)
    model.set_segment(G, H)
    model.set_segment(G, E)
    model.set_segment(E, H)
    model.set_segment(A, D)
    model.set_segment(A, G)
    model.set_segment(G, D)
    model.set_segment(C, B)
    model.set_segment(C, H)
    model.set_segment(H, B)

    # Segments from F
    model.set_segment(E, F)
    model.set_segment(F, A)
    model.set_segment(F, G)
    model.set_segment(F, D)
    model.set_segment(F, C)
    model.set_segment(F, H)
    model.set_segment(F, B)

    # Sections
    model.set_section([G, E, H])
    model.set_section([A, E, B])
    model.set_section([C, E, D])

    # Polygons (triangles and plane of reference)
    model.set_polygon([P1, P2, P3, P4])
    model.set_polygon([A, E, D])
    model.set_polygon([C, E, B])
    model.set_polygon([A, G, E])
    model.set_polygon([B, E, H])
    model.set_polygon([A, E, F])
    model.set_polygon([B, E, F])
    model.set_polygon([C, E, F])
    model.set_polygon([D, E, F])
    model.set_polygon([F, A, D])
    model.set_polygon([F, B, C])
    model.set_polygon([F, A, G])
    model.set_polygon([F, B, H])
    model.set_polygon([F, E, G])
    model.set_polygon([F, E, H])

    # Angles (wedges)
    model.set_wedge(E, A, A, D)
    model.set_wedge(E, C, C, B)
    model.set_wedge(A, D, D, E)
    model.set_wedge(B, E, E, C)
    model.set_wedge(E, A, A, G)
    model.set_wedge(E, B, B, H)
    model.set_wedge(A, F, F, D)
    model.set_wedge(B, F, F, C)
    model.set_wedge(E, G, G, F)
    model.set_wedge(E, H, H, F)

    return model


if __name__ == "__main__":
    construct_0282_g1()
