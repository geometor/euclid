"""Programmatic construction for Book IV, Proposition 11 Commentary (0108.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0108_g1() -> Model:
    """Construct the figure 0108.g1 (Taylor's decagon/pentagon construction) using geometor.model."""
    model = Model("0108.g1")

    # Points (y-inverted for standard mathematical coordinates)
    O = model.set_point(119.00, -120.00, classes=["given"], label="O")
    A = model.set_point(33.00, -120.00, classes=["given"], label="A")
    B = model.set_point(119.00, -34.00, classes=["given"], label="B")
    C = model.set_point(205.00, -120.00, classes=["given"], label="C")
    D = model.set_point(119.00, -206.00, classes=["given"], label="D")
    E = model.set_point(119.00, -163.00, label="E")
    F = model.set_point(80.54, -143.77, label="F")
    P1 = model.set_point(49.42, -170.55, label="P1")
    P2 = model.set_point(49.42, -69.45, label="P2")
    G = model.set_point(76.00, -120.00, label="G")

    # Given circle and auxiliary arc circle
    model.construct_circle(O, A)
    model.construct_circle(A, F)

    # Segments
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(A, O)
    model.set_segment(O, C)
    model.set_segment(B, O)
    model.set_segment(O, D)
    model.set_segment(O, E)
    model.set_segment(E, D)
    model.set_segment(A, E)
    model.set_segment(A, F)
    model.set_segment(E, F)
    model.set_segment(A, P1)
    model.set_segment(P1, G)

    # Collinear sections
    model.set_section([A, O, C])
    model.set_section([B, O, D])
    model.set_section([O, E, D])
    model.set_section([A, F, E], classes=["golden"])

    return model


if __name__ == "__main__":
    construct_0108_g1()
