"""Programmatic construction for Book VII, Proposition 28 (0335.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0335_g1() -> Model:
    """Construct the figure 0335.g1 using geometor.model."""
    model = Model("0335.g1")

    # Horizontal number segment AC divided at B
    A = model.set_point(10.0, -12.0, classes=["given"], label="A")
    B = model.set_point(138.0, -12.0, classes=["given"], label="B")
    C = model.set_point(197.0, -12.0, classes=["given"], label="C")

    # Single-letter horizontal number segment D
    D_l = model.set_point(9.0, -43.0, classes=["given"], label="D")
    D_r = model.set_point(66.0, -43.0, label="D_r")

    # Base line AC
    model.construct_line(A, C)

    # Whole and subdivided segments on AC
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)

    # Single-letter segment D
    model.set_segment(D_l, D_r)

    # Collinear section ABC
    model.set_section([A, B, C])

    return model


if __name__ == "__main__":
    construct_0335_g1()
