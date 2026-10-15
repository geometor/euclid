"""Programmatic construction for Book IX, Proposition 15 (0410.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0410_g1() -> Model:
    """Construct the figure 0410.g1 using geometor.model."""
    model = Model("0410.g1")

    # Single-letter horizontal number segments A, B, C
    A_l = model.set_point(33.0, -21.5, classes=["given"], label="A")
    A_r = model.set_point(68.0, -21.5, label="A_r")

    B_l = model.set_point(153.0, -21.5, classes=["given"], label="B")
    B_r = model.set_point(206.0, -21.5, label="B_r")

    C_l = model.set_point(80.0, -47.5, classes=["given"], label="C")
    C_r = model.set_point(163.0, -47.5, label="C_r")

    # Subdivided horizontal number segment DF (divided at E)
    D = model.set_point(86.0, -75.0, classes=["given"], label="D")
    E = model.set_point(106.0, -75.0, label="E")
    F = model.set_point(136.0, -75.0, classes=["given"], label="F")

    # Base line for DF
    model.construct_line(D, F)

    # Number segments A, B, C
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(C_l, C_r)

    # Whole and subdivided segments on DF
    model.set_segment(D, F)
    model.set_segment(D, E)
    model.set_segment(E, F)

    # Collinear section
    model.set_section([D, E, F])

    return model


if __name__ == "__main__":
    construct_0410_g1()
