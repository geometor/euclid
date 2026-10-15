"""Programmatic construction for Book I, Common Notion 4 commentary (0245.g1).

Hilbert's proof that all right angles are congruent with one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0245_g1() -> Model:
    """Construct the figure for 0245.g1 using geometor.model."""
    model = Model("0245.g1")

    # Left figure (vertex A on base B-A-C, perpendicular AD, auxiliary rays AD'', AD''')
    B = model.set_point(20, -134, classes=["given"], label="B")
    A = model.set_point(90, -134, classes=["given"], label="A")
    C = model.set_point(160, -134, classes=["given"], label="C")
    D = model.set_point(90, -30, classes=["given"], label="D")
    Dpp = model.set_point(70, -32, classes=["given"], label="D''")
    Dppp = model.set_point(110, -32, classes=["given"], label="D'''")

    # Right figure (vertex A' on base B'-A'-C', perpendicular A'D')
    Bp = model.set_point(220, -134, classes=["given"], label="B'")
    Ap = model.set_point(290, -134, classes=["given"], label="A'")
    Cp = model.set_point(360, -134, classes=["given"], label="C'")
    Dp = model.set_point(290, -30, classes=["given"], label="D'")

    # Base lines and rays
    model.construct_line(B, C)
    model.construct_line(A, D)
    model.construct_line(A, Dpp)
    model.construct_line(A, Dppp)
    model.construct_line(Bp, Cp)
    model.construct_line(Ap, Dp)

    # Segments and sections
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(A, D)
    model.set_segment(A, Dpp)
    model.set_segment(A, Dppp)
    model.set_section([B, A, C])

    model.set_segment(Ap, Bp)
    model.set_segment(Ap, Cp)
    model.set_segment(Bp, Cp)
    model.set_segment(Ap, Dp)
    model.set_section([Bp, Ap, Cp])

    # Angles (Wedges)
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, C, C, D)
    model.set_wedge(A, B, B, Dpp)
    model.set_wedge(A, C, C, Dpp)
    model.set_wedge(A, C, C, Dppp)
    model.set_wedge(A, D, D, Dpp)
    model.set_wedge(A, D, D, Dppp)
    model.set_wedge(Ap, Bp, Bp, Dp)
    model.set_wedge(Ap, Cp, Cp, Dp)

    return model


if __name__ == "__main__":
    construct_0245_g1()
