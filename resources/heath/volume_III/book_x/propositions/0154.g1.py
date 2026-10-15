"""Programmatic construction for Book X, Proposition 69 (0154.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0154_g1() -> Model:
    """Construct the figure 0154.g1 using geometor.model."""
    model = Model("0154.g1")

    # Side of a rational plus a medial area AB divided at E
    A = model.set_point(22.5, -15.0, classes=["given"], label="A")
    E = model.set_point(22.5, -110.0, classes=["given"], label="E")
    B = model.set_point(22.5, -160.0, classes=["given"], label="B")

    # Commensurable straight line CD divided at F
    C = model.set_point(54.5, -53.0, classes=["given"], label="C")
    F = model.set_point(54.5, -128.0, label="F")
    D = model.set_point(54.5, -157.0, classes=["given"], label="D")

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
    construct_0154_g1()
