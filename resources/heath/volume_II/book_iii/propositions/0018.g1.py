"""Programmatic construction for Book III, Proposition 5 (0018.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0018_g1() -> Model:
    """Construct the figure 0018.g1 using geometor.model."""
    model = Model("0018.g1")

    # Points (y-inverted for standard mathematical coordinates)
    O1 = model.set_point(76, -80, classes=["auxiliary"], label="O1")
    O2 = model.set_point(105, -102, classes=["auxiliary"], label="O2")
    C = model.set_point(105.94, -28.01, classes=["given"], label="C")
    B = model.set_point(34.0, -122.85, classes=["given"], label="B")
    A = model.set_point(24.04, -50.0, classes=["given"], label="A")
    D = model.set_point(38.5, -69.84, classes=["given"], label="D")
    E = model.set_point(92, -92, label="E")
    F = model.set_point(124, -116, label="F")
    G = model.set_point(164.32, -146.24, label="G")

    # Construction circles ABC and CDG
    model.construct_circle(O1, C)
    model.construct_circle(O2, C)

    # Segments
    model.set_segment(E, C)
    model.set_segment(E, G)
    model.set_segment(E, F)
    model.set_segment(F, G)

    # Sections
    model.set_section([E, F, G])

    return model


if __name__ == "__main__":
    construct_0018_g1()
