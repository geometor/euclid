"""Programmatic construction for Book III, Proposition 4 (0017.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0017_g1() -> Model:
    """Construct the figure 0017.g1 using geometor.model."""
    model = Model("0017.g1")

    # Points (y-inverted for standard mathematical coordinates)
    F = model.set_point(97, -89, label="F")
    A = model.set_point(24.56, -112, classes=["given"], label="A")
    C = model.set_point(167.25, -118, classes=["given"], label="C")
    B = model.set_point(93.8, -164.93, classes=["given"], label="B")
    D = model.set_point(169.44, -66, classes=["given"], label="D")
    E = model.set_point(130.85, -116.47, label="E")

    # Construction circle ABCD
    model.construct_circle(F, A)

    # Segments
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(F, E)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(B, E)
    model.set_segment(E, D)

    # Sections
    model.set_section([A, E, C])
    model.set_section([B, E, D])

    # Angles (wedges)
    model.set_wedge(E, F, F, A)
    model.set_wedge(E, F, F, B)

    return model


if __name__ == "__main__":
    construct_0017_g1()
