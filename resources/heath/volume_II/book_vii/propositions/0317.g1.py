"""Programmatic construction for Book VII, Proposition 11 (0317.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0317_g1() -> Model:
    """Construct the figure 0317.g1 using geometor.model."""
    model = Model("0317.g1")

    # Vertical number segment AB (divided at E)
    A = model.set_point(24.0, -13.0, classes=["given"], label="A")
    E = model.set_point(24.0, -50.0, label="E")
    B = model.set_point(24.0, -111.0, classes=["given"], label="B")

    # Vertical number segment CD (divided at F)
    C = model.set_point(54.0, -26.0, classes=["given"], label="C")
    F = model.set_point(54.0, -57.0, label="F")
    D = model.set_point(54.0, -112.0, classes=["given"], label="D")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Whole and subdivided segments
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)

    # Collinear sections
    model.set_section([A, E, B])
    model.set_section([C, F, D])

    return model


if __name__ == "__main__":
    construct_0317_g1()
