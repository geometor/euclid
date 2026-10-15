"""Programmatic construction for Book III, Proposition 31 Commentary — Pappus's lemma (0070.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0070_g2() -> Model:
    """Construct the figure 0070.g2 using geometor.model."""
    model = Model("0070.g2")

    # Points (y-inverted for standard mathematical coordinates)
    D = model.set_point(102.0, -113.0, classes=["given"], label="D")
    A = model.set_point(18.0, -113.0, classes=["given"], label="A")
    C = model.set_point(186.0, -113.0, classes=["given"], label="C")
    F = model.set_point(220.0, -113.0, classes=["given"], label="F")
    M = model.set_point(161.0, -113.0, label="M")
    B = model.set_point(75.94, -33.15, label="B")
    E = model.set_point(129.74, -62.97, label="E")
    G = model.set_point(183.54, -92.79, label="G")

    # Semicircles / Circles ABC (center D) and DEF (center M)
    model.construct_circle(D, A)
    model.construct_circle(M, D)

    # Line of centres and secant FB
    model.construct_line(A, F)
    model.construct_line(F, B)

    # Segments
    model.set_segment(A, F)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(D, F)
    model.set_segment(C, F)
    model.set_segment(F, B)
    model.set_segment(B, G)
    model.set_segment(B, E)
    model.set_segment(E, G)
    model.set_segment(G, F)
    model.set_segment(E, F)
    model.set_segment(D, E)

    # Sections
    model.set_section([A, D, C])
    model.set_section([D, C, F])
    model.set_section([B, E, G])
    model.set_section([E, G, F])

    # Polygons and angles
    model.set_polygon([D, E, F])
    model.set_wedge(E, D, D, F)

    return model


if __name__ == "__main__":
    construct_0070_g2()
