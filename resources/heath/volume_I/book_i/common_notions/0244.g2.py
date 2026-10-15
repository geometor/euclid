"""Programmatic construction for Book I, Common Notion 4 commentary (0244.g2).

Hilbert's proof of interior half-ray angle congruence.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0244_g2() -> Model:
    """Construct the figure for 0244.g2 using geometor.model."""
    model = Model("0244.g2")

    # Left figure (vertex O, rays h, k, l with points A, B, C)
    O = model.set_point(95, -98, classes=["given"], label="O")
    A = model.set_point(210, -98, classes=["given"], label="A")
    B = model.set_point(55, -35, classes=["given"], label="B")
    C = model.set_point(118, -60, classes=["given"], label="C")

    # Right figure (vertex O', rays h', k', l' with points A', B', C')
    Op = model.set_point(275, -98, classes=["given"], label="O'")
    Ap = model.set_point(390, -98, classes=["given"], label="A'")
    Bp = model.set_point(235, -35, classes=["given"], label="B'")
    Cp = model.set_point(298, -60, classes=["given"], label="C'")

    # Rays (constructed lines)
    model.construct_line(O, A)
    model.construct_line(O, B)
    model.construct_line(O, C)
    model.construct_line(Op, Ap)
    model.construct_line(Op, Bp)
    model.construct_line(Op, Cp)

    # Segments and sections
    model.set_segment(O, A)
    model.set_segment(O, B)
    model.set_segment(O, C)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(A, B)
    model.set_section([A, C, B])

    model.set_segment(Op, Ap)
    model.set_segment(Op, Bp)
    model.set_segment(Op, Cp)
    model.set_segment(Ap, Cp)
    model.set_segment(Cp, Bp)
    model.set_segment(Ap, Bp)
    model.set_section([Ap, Cp, Bp])

    # Polygons
    model.set_polygon([O, A, B])
    model.set_polygon([O, A, C])
    model.set_polygon([O, C, B])
    model.set_polygon([Op, Ap, Bp])
    model.set_polygon([Op, Ap, Cp])
    model.set_polygon([Op, Cp, Bp])

    # Angles (Wedges)
    model.set_wedge(O, A, A, B)
    model.set_wedge(O, A, A, C)
    model.set_wedge(O, C, C, B)
    model.set_wedge(Op, Ap, Ap, Bp)
    model.set_wedge(Op, Ap, Ap, Cp)
    model.set_wedge(Op, Cp, Cp, Bp)

    return model


if __name__ == "__main__":
    construct_0244_g2()
