"""Programmatic construction for Postulate 5 Commentary, Legendre (0231.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0231_g1() -> Model:
    """Construct the figure 0231.g1 (Legendre's second proof of Theorem I) using geometor.model."""
    model = Model("0231.g1")

    # Points (y negated for Cartesian coordinates)
    A = model.set_point(21, -98, classes=["given"], label="A")
    B = model.set_point(123, -98, classes=["given"], label="B")
    C = model.set_point(88, -23, classes=["given"], label="C")
    H = model.set_point(105.5, -60.5, label="H")
    D = model.set_point(190, -23, label="D")

    # Construction lines
    model.construct_line(A, B)
    model.construct_line(A, C)
    model.construct_line(B, C)
    model.construct_line(A, D)
    model.construct_line(B, D)

    # Segments (including collinear sub-segments)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(B, H)
    model.set_segment(H, C)
    model.set_segment(A, H)
    model.set_segment(H, D)
    model.set_segment(A, D)
    model.set_segment(B, D)

    # Collinear sections
    model.set_section([B, H, C])
    model.set_section([A, H, D])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, H, C])
    model.set_polygon([D, H, B])
    model.set_polygon([A, B, D])

    # Angles (wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(A, H, H, C)
    model.set_wedge(A, B, B, D)
    model.set_wedge(C, A, A, H)
    model.set_wedge(D, H, H, B)
    model.set_wedge(B, D, D, H)

    return model


if __name__ == "__main__":
    construct_0231_g1()
