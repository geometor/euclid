"""Programmatic construction for Book VII, Proposition 35 (0345.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0345_g1() -> Model:
    """Construct the figure 0345.g1 using geometor.model."""
    model = Model("0345.g1")

    # Single-letter number segments A and B
    A_l = model.set_point(25.0, -15.0, classes=["given"], label="A")
    A_r = model.set_point(84.0, -15.0, label="A_r")

    B_l = model.set_point(128.0, -14.0, classes=["given"], label="B")
    B_r = model.set_point(204.0, -14.0, label="B_r")

    # Subdivided horizontal number segment CD (divided at F)
    C = model.set_point(30.0, -39.0, classes=["given"], label="C")
    F = model.set_point(91.0, -39.0, label="F")
    D = model.set_point(234.0, -39.0, classes=["given"], label="D")

    # Single-letter number segment E
    E_l = model.set_point(42.0, -66.0, classes=["given"], label="E")
    E_r = model.set_point(128.0, -66.0, label="E_r")

    # Base line for CD
    model.construct_line(C, D)

    # Single-letter segments A, B, E
    model.set_segment(A_l, A_r)
    model.set_segment(B_l, B_r)
    model.set_segment(E_l, E_r)

    # Whole and subdivided segments on CD
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)

    # Collinear section
    model.set_section([C, F, D])

    return model


if __name__ == "__main__":
    construct_0345_g1()
