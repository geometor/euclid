"""Programmatic construction for Book XI, Proposition 4 Cauchy's Proof (0284.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0284_g1() -> Model:
    """Construct the figure 0284.g1 using geometor.model."""
    model = Model("0284.g1")

    # Plane MN corners
    M = model.set_point(48.0, -81.0, classes=["given"], label="M")
    P2 = model.set_point(215.0, -81.0, classes=["plane_corner"])
    N = model.set_point(202.0, -180.0, classes=["given"], label="N")
    P4 = model.set_point(21.0, -180.0, classes=["plane_corner"])

    # Points A, B, F and C, D, E in plane MN
    A = model.set_point(107.0, -18.0, classes=["given"], label="A")
    B = model.set_point(107.0, -114.0, classes=["given"], label="B")
    F = model.set_point(107.0, -206.0, label="F")
    C = model.set_point(62.0, -168.0, classes=["given"], label="C")
    D = model.set_point(191.0, -110.0, classes=["given"], label="D")
    E = model.set_point(131.66, -136.68, label="E")

    # Construction lines
    model.construct_line(A, F)
    model.construct_line(C, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, F)
    model.set_segment(A, F)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(B, E)
    model.set_segment(C, D)
    model.set_segment(C, E)
    model.set_segment(E, D)
    model.set_segment(A, C)
    model.set_segment(A, E)
    model.set_segment(A, D)
    model.set_segment(C, F)
    model.set_segment(E, F)
    model.set_segment(D, F)

    # Polygons
    model.set_polygon([M, P2, N, P4])
    model.set_polygon([A, C, D])
    model.set_polygon([F, C, D])
    model.set_polygon([A, C, E])
    model.set_polygon([F, C, E])
    model.set_polygon([A, B, E])
    model.set_polygon([F, B, E])
    model.set_polygon([B, C, D])
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])

    # Angles
    model.set_wedge(C, A, A, D)
    model.set_wedge(C, D, D, F)
    model.set_wedge(B, A, A, E)
    model.set_wedge(B, E, E, F)

    return model


if __name__ == "__main__":
    construct_0284_g1()
