"""Programmatic construction for Book XI, Proposition 1 (0276.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0276_g1() -> Model:
    """Construct the figure 0276.g1 using geometor.model."""
    model = Model("0276.g1")

    # Points of the plane of reference (unlabelled boundary corners)
    P1 = model.set_point(89.0, -24.0, classes=["plane_corner"])
    P2 = model.set_point(145.0, -92.0, classes=["plane_corner"])
    P3 = model.set_point(68.0, -184.0, classes=["plane_corner"])
    P4 = model.set_point(11.0, -115.0, classes=["plane_corner"])

    # Points A, B, C, D
    A = model.set_point(52.0, -136.0, classes=["given"], label="A")
    B = model.set_point(78.0, -102.0, classes=["given"], label="B")
    D = model.set_point(104.0, -68.0, label="D")
    C = model.set_point(78.0, -14.0, classes=["given"], label="C")

    # Construction line ABD in the plane of reference
    model.construct_line(A, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, D)
    model.set_segment(A, D)
    model.set_segment(B, C)

    # Plane boundary segments
    model.set_segment(P1, P2)
    model.set_segment(P2, P3)
    model.set_segment(P3, P4)
    model.set_segment(P4, P1)

    # Sections / broken lines
    model.set_section([A, B, D])
    model.set_section([A, B, C])

    # Plane polygon
    model.set_polygon([P1, P2, P3, P4])

    return model


if __name__ == "__main__":
    construct_0276_g1()
