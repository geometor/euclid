"""Programmatic construction for Book XI, Definition 6 Commentary (0268.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0268_g1() -> Model:
    """Construct the figure 0268.g1 using geometor.model."""
    model = Model("0268.g1")

    # Points (y negated for standard Cartesian coordinates)
    M = model.set_point(27.0, -21.0, classes=["given"], label="M")
    C = model.set_point(118.0, -21.0, classes=["given"], label="C")
    E = model.set_point(90.0, -62.0, label="E")
    B = model.set_point(71.0, -80.0, classes=["given"], label="B")
    A = model.set_point(27.0, -139.0, classes=["given"], label="A")
    N = model.set_point(118.0, -139.0, classes=["given"], label="N")
    D = model.set_point(90.0, -180.0, label="D")
    P = model.set_point(71.0, -197.0, classes=["given"], label="P")

    # Construction circles (representing foreshortened arcs BEC and PDN)
    model.construct_circle(M, C)
    model.construct_circle(A, N)

    # Segments
    model.set_segment(M, A)
    model.set_segment(M, C)
    model.set_segment(M, E)
    model.set_segment(M, B)
    model.set_segment(A, N)
    model.set_segment(A, D)
    model.set_segment(A, P)
    model.set_segment(C, N)
    model.set_segment(E, D)
    model.set_segment(B, P)

    # Planes and sectors (represented as polygons)
    model.set_polygon([M, A, N, C])
    model.set_polygon([M, A, D, E])
    model.set_polygon([M, A, P, B])
    model.set_polygon([N, A, P, D])
    model.set_polygon([C, M, B, E])

    # Angles (wedges)
    model.set_wedge(A, N, N, P)
    model.set_wedge(A, N, N, D)
    model.set_wedge(A, D, D, P)
    model.set_wedge(M, B, B, C)
    model.set_wedge(M, B, B, E)
    model.set_wedge(M, E, E, C)

    return model


if __name__ == "__main__":
    construct_0268_g1()
