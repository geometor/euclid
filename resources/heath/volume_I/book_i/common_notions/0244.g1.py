"""Programmatic construction for Book I, Common Notion 4 commentary (0244.g1).

Hilbert's proof of the congruence of supplementary angles.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0244_g1() -> Model:
    """Construct the figure for 0244.g1 using geometor.model."""
    model = Model("0244.g1")

    # Left figure ABCD (A-B-D collinear on base, C apex)
    A = model.set_point(20, -75, classes=["given"], label="A")
    B = model.set_point(105, -75, classes=["given"], label="B")
    D = model.set_point(155, -75, classes=["given"], label="D")
    C = model.set_point(55, -25, classes=["given"], label="C")

    # Right figure A'B'C'D' (A'-B'-D' collinear on base, C' apex)
    Ap = model.set_point(200, -75, classes=["given"], label="A'")
    Bp = model.set_point(285, -75, classes=["given"], label="B'")
    Dp = model.set_point(335, -75, classes=["given"], label="D'")
    Cp = model.set_point(235, -25, classes=["given"], label="C'")

    # Base lines
    model.construct_line(A, D)
    model.construct_line(Ap, Dp)

    # Left figure segments and section
    model.set_segment(A, B)
    model.set_segment(B, D)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_section([A, B, D])

    # Right figure segments and section
    model.set_segment(Ap, Bp)
    model.set_segment(Bp, Dp)
    model.set_segment(Ap, Dp)
    model.set_segment(Ap, Cp)
    model.set_segment(Bp, Cp)
    model.set_segment(Cp, Dp)
    model.set_section([Ap, Bp, Dp])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([C, B, D])
    model.set_polygon([C, A, D])
    model.set_polygon([Ap, Bp, Cp])
    model.set_polygon([Cp, Bp, Dp])
    model.set_polygon([Cp, Ap, Dp])

    # Angles (Wedges)
    model.set_wedge(B, A, A, C)
    model.set_wedge(B, C, C, D)
    model.set_wedge(A, C, C, B)
    model.set_wedge(D, A, A, C)
    model.set_wedge(C, A, A, B)
    model.set_wedge(C, B, B, D)
    model.set_wedge(C, A, A, D)

    model.set_wedge(Bp, Ap, Ap, Cp)
    model.set_wedge(Bp, Cp, Cp, Dp)
    model.set_wedge(Ap, Cp, Cp, Bp)
    model.set_wedge(Dp, Ap, Ap, Cp)
    model.set_wedge(Cp, Ap, Ap, Bp)
    model.set_wedge(Cp, Bp, Bp, Dp)
    model.set_wedge(Cp, Ap, Ap, Dp)

    return model


if __name__ == "__main__":
    construct_0244_g1()
