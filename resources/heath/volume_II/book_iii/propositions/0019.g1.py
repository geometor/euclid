"""Programmatic construction for Book III, Proposition 6 (0019.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0019_g1() -> Model:
    """Construct the figure 0019.g1 using geometor.model."""
    model = Model("0019.g1")

    # Points (y-inverted for standard mathematical coordinates)
    O1 = model.set_point(102, -102, classes=["auxiliary"], label="O1")
    O2 = model.set_point(82.8, -87.6, classes=["auxiliary"], label="O2")
    C = model.set_point(33.2, -50.4, classes=["given"], label="C")
    F = model.set_point(94, -96, label="F")
    E = model.set_point(142.12, -105.62, label="E")
    B = model.set_point(187.07, -114.61, label="B")
    D = model.set_point(82.8, -149.6, classes=["given"], label="D")
    A = model.set_point(85, -186.3, classes=["given"], label="A")

    # Construction circles ABC and CDE touching internally at C
    model.construct_circle(O1, C)
    model.construct_circle(O2, C)

    # Segments
    model.set_segment(F, C)
    model.set_segment(F, B)
    model.set_segment(F, E)
    model.set_segment(E, B)

    # Sections
    model.set_section([F, E, B])

    return model


if __name__ == "__main__":
    construct_0019_g1()
