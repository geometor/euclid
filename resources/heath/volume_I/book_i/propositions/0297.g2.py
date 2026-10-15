"""Programmatic construction for Book I, Proposition 18 Note — Porphyry's Alternative Proof (0297.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0297_g2() -> Model:
    """Construct the figure 0297.g2 using geometor.model."""
    model = Model("0297.g2")

    # Points
    A = model.set_point(12, -16, classes=["given"], label="A")
    B = model.set_point(48, -108, classes=["given"], label="B")
    D = model.set_point(68, -53, label="D")
    C = model.set_point(150, -108, classes=["given"], label="C")
    E = model.set_point(82, -168, label="E")

    # Construction lines
    model.construct_line(A, E)
    model.construct_line(A, C)

    # Segments
    model.set_segment(A, E)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(E, C)
    model.set_segment(A, B)
    model.set_segment(B, E)
    model.set_segment(A, D)
    model.set_segment(C, D)

    # Collinear / broken sections
    model.set_section([A, B, E])
    model.set_section([A, D, C])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([B, C, E])
    model.set_polygon([A, E, C])

    # Angles (wedges)
    model.set_wedge(B, A, A, C)
    model.set_wedge(B, E, E, C)
    model.set_wedge(E, A, A, C)
    model.set_wedge(C, A, A, E)
    model.set_wedge(C, A, A, B)
    model.set_wedge(C, B, B, E)
    model.set_wedge(A, B, B, C)

    return model


if __name__ == "__main__":
    construct_0297_g2()
