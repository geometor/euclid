"""Programmatic construction for Book IX, Proposition 22 (0420.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0420_g1() -> Model:
    """Construct the figure 0420.g1 using geometor.model."""
    model = Model("0420.g1")

    # Subdivided horizontal number segment AE (divided at B, C, D)
    A = model.set_point(15.0, -27.5, classes=["given"], label="A")
    B = model.set_point(65.0, -27.5, label="B")
    C = model.set_point(175.0, -27.5, label="C")
    D = model.set_point(260.0, -27.5, label="D")
    E = model.set_point(310.0, -27.5, classes=["given"], label="E")

    # Base line
    model.construct_line(A, E)

    # Whole and subdivided segments on AE
    model.set_segment(A, E)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(B, D)
    model.set_segment(B, E)
    model.set_segment(C, E)

    # Collinear sections
    model.set_section([A, B, C])
    model.set_section([B, C, D])
    model.set_section([C, D, E])
    model.set_section([A, C, E])

    return model


if __name__ == "__main__":
    construct_0420_g1()
