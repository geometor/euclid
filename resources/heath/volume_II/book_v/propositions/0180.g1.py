"""Programmatic construction for Book V, Proposition 19 (0180.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0180_g1() -> Model:
    """Construct the figure 0180.g1 for Book V, Proposition 19 using geometor.model."""
    model = Model("0180.g1")

    # Top magnitude AB divided at E
    A = model.set_point(16.00, -27.00, classes=["given"], label="A")
    E = model.set_point(56.00, -27.00, classes=["given"], label="E")
    B = model.set_point(132.00, -27.00, classes=["given"], label="B")

    # Bottom magnitude CD divided at F
    C = model.set_point(16.00, -57.00, classes=["given"], label="C")
    F = model.set_point(38.00, -57.00, classes=["given"], label="F")
    D = model.set_point(83.00, -57.00, classes=["given"], label="D")

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
    construct_0180_g1()
