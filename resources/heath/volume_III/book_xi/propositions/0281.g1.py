"""Programmatic construction for Book XI, Proposition 3 Commentary Diagram 1 (0281.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0281_g1() -> Model:
    """Construct the figure 0281.g1 using geometor.model."""
    model = Model("0281.g1")

    # Plane ADE corners
    P1 = model.set_point(41.0, -85.0, classes=["plane_corner"])
    D = model.set_point(185.0, -83.0, classes=["given"], label="D")
    E = model.set_point(176.0, -148.0, classes=["given"], label="E")
    P4 = model.set_point(21.0, -151.0, classes=["plane_corner"])

    # Points of plane ABC and produced point F
    B = model.set_point(66.0, -42.0, classes=["given"], label="B")
    C = model.set_point(174.0, -32.0, classes=["given"], label="C")
    F = model.set_point(99.0, -191.0, label="F")
    A = model.set_point(81.84, -113.52, classes=["given"], label="A")
    G = model.set_point(140.25, -103.55, label="G")

    # Construction lines
    model.construct_line(B, F)
    model.construct_line(C, F)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, F)
    model.set_segment(B, F)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(C, G)
    model.set_segment(G, F)
    model.set_segment(C, F)
    model.set_segment(A, G)

    # Plane ADE and Plane ABC polygons
    model.set_polygon([P1, D, E, P4])
    model.set_polygon([A, B, C])
    model.set_polygon([B, C, F])

    return model


if __name__ == "__main__":
    construct_0281_g1()
