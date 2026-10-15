"""Programmatic construction for Book I, Common Notion 4 commentary (0245.g2).

Hilbert's proof of SSS triangle congruence (Eucl. I. 8).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0245_g2() -> Model:
    """Construct the figure for 0245.g2 using geometor.model."""
    model = Model("0245.g2")

    # Left figure (triangles ABC and A''BC sharing base BC, with vertical chord AA'')
    A = model.set_point(90, -30, classes=["given"], label="A")
    B = model.set_point(25, -92, classes=["given"], label="B")
    C = model.set_point(118, -92, classes=["given"], label="C")
    App = model.set_point(90, -154, classes=["given"], label="A''")

    # Right figure (triangle A'B'C')
    Ap = model.set_point(225, -30, classes=["given"], label="A'")
    Bp = model.set_point(160, -92, classes=["given"], label="B'")
    Cp = model.set_point(253, -92, classes=["given"], label="C'")

    # Base lines
    model.construct_line(B, C)
    model.construct_line(A, App)
    model.construct_line(Bp, Cp)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(B, App)
    model.set_segment(C, App)
    model.set_segment(A, App)

    model.set_segment(Ap, Bp)
    model.set_segment(Ap, Cp)
    model.set_segment(Bp, Cp)

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([App, B, C])
    model.set_polygon([A, B, App])
    model.set_polygon([A, C, App])
    model.set_polygon([A, B, App, C])
    model.set_polygon([Ap, Bp, Cp])

    # Angles (Wedges)
    model.set_wedge(B, A, A, C)
    model.set_wedge(B, C, C, App)
    model.set_wedge(B, A, A, App)
    model.set_wedge(A, B, B, C)
    model.set_wedge(App, B, B, C)
    model.set_wedge(Bp, Ap, Ap, Cp)
    model.set_wedge(Ap, Bp, Bp, Cp)

    return model


if __name__ == "__main__":
    construct_0245_g2()
