"""Programmatic construction for Book X, Proposition 16 Lemma (0045.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0045_g1() -> Model:
    """Construct the figure 0045.g1 using geometor.model."""
    model = Model("0045.g1")

    # Bottom line AB divided at C
    A = model.set_point(20.0, -73.5, classes=["given"], label="A")
    C = model.set_point(141.0, -73.5, label="C")
    B = model.set_point(194.0, -73.5, classes=["given"], label="B")

    # Top line E-D-F completing parallelogram AD and square DB
    E = model.set_point(20.0, -20.5, label="E")
    D = model.set_point(141.0, -20.5, label="D")
    F = model.set_point(194.0, -20.5, label="F")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(E, F)
    model.construct_line(A, E)
    model.construct_line(C, D)
    model.construct_line(B, F)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(C, D)
    model.set_segment(A, E)
    model.set_segment(B, F)
    model.set_segment(E, D)
    model.set_segment(D, F)
    model.set_section([A, C, B])

    # Applied parallelogram AD (< A C D E >) and deficient square DB (< C B F D >)
    model.set_polygon([A, C, D, E])
    model.set_polygon([C, B, F, D])
    model.set_polygon([A, B, F, E])

    return model


if __name__ == "__main__":
    construct_0045_g1()
