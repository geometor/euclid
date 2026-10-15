"""Programmatic construction for Book X, Proposition 68 (0153.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0153_g1() -> Model:
    """Construct the figure 0153.g1 using geometor.model."""
    model = Model("0153.g1")

    # Major straight line AB divided at E
    A = model.set_point(24.5, -14.0, classes=["given"], label="A")
    E = model.set_point(24.5, -79.0, classes=["given"], label="E")
    B = model.set_point(24.5, -122.0, classes=["given"], label="B")

    # Commensurable straight line CD divided at F
    C = model.set_point(56.5, -44.0, classes=["given"], label="C")
    F = model.set_point(56.5, -96.0, label="F")
    D = model.set_point(56.5, -121.0, classes=["given"], label="D")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)

    # Sections
    model.set_section([A, E, B])
    model.set_section([C, F, D])

    return model


if __name__ == "__main__":
    construct_0153_g1()
