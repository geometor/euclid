"""Programmatic construction for Book X, Proposition 28, Lemma 1 (0067.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0067_g1() -> Model:
    """Construct the figure 0067.g1 using geometor.model."""
    model = Model("0067.g1")

    # Line AB with division points D (bisecting AC) and C
    A = model.set_point(14.0, -17.0, classes=["given"], label="A")
    D = model.set_point(91.5, -17.0, label="D")
    C = model.set_point(169.0, -17.0, classes=["given"], label="C")
    B = model.set_point(219.0, -17.0, classes=["given"], label="B")

    # Base line
    model.construct_line(A, B)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(A, D)
    model.set_segment(D, C)
    model.set_segment(B, D)

    # Collinear sections
    model.set_section([A, D, C])
    model.set_section([A, C, B])
    model.set_section([D, C, B])
    model.set_section([A, D, B])

    return model


if __name__ == "__main__":
    construct_0067_g1()
