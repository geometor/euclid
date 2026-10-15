"""Programmatic construction for Book I, Common Notion 4 commentary (0243.g1).

Hilbert's proof of SAS triangle congruence (Eucl. I. 4) by reductio ad absurdum.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0243_g1() -> Model:
    """Construct the figure for 0243.g1 using geometor.model."""
    model = Model("0243.g1")

    # Left triangle ABC
    A = model.set_point(100, -25, classes=["given"], label="A")
    B = model.set_point(20, -100, classes=["given"], label="B")
    C = model.set_point(110, -100, classes=["given"], label="C")

    # Right triangle A'B'C' with point D on B'C'
    Ap = model.set_point(250, -25, classes=["given"], label="A'")
    Bp = model.set_point(170, -100, classes=["given"], label="B'")
    D = model.set_point(245, -100, classes=["given"], label="D")
    Cp = model.set_point(260, -100, classes=["given"], label="C'")

    # Base lines
    model.construct_line(B, C)
    model.construct_line(Bp, Cp)

    # Segments of triangle ABC
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)

    # Segments of triangle A'B'C' and auxiliary segment A'D
    model.set_segment(Ap, Bp)
    model.set_segment(Ap, Cp)
    model.set_segment(Ap, D)
    model.set_segment(Bp, D)
    model.set_segment(D, Cp)
    model.set_segment(Bp, Cp)

    # Collinear section on base B'D C'
    model.set_section([Bp, D, Cp])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([Ap, Bp, Cp])
    model.set_polygon([Ap, Bp, D])
    model.set_polygon([Ap, D, Cp])

    # Angles (Wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, A, A, B)

    model.set_wedge(Ap, Bp, Bp, Cp)
    model.set_wedge(Ap, Bp, Bp, D)
    model.set_wedge(Ap, D, D, Cp)
    model.set_wedge(Bp, Ap, Ap, Cp)
    model.set_wedge(Cp, Ap, Ap, Bp)
    model.set_wedge(D, Ap, Ap, Bp)

    return model


if __name__ == "__main__":
    construct_0243_g1()
