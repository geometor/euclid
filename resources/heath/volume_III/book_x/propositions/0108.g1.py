"""Programmatic construction for Book X, Proposition 49 (0108.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0108_g1() -> Model:
    """Construct the figure 0108.g1 using geometor.model."""
    model = Model("0108.g1")

    # Number line AB divided at C
    A = model.set_point(27.0, -20.0, classes=["given"], label="A")
    C = model.set_point(27.0, -95.0, classes=["given"], label="C")
    B = model.set_point(27.0, -144.0, classes=["given"], label="B")

    # Single-letter magnitude segment D
    D_t = model.set_point(64.5, -28.0, classes=["given"], label="D")
    D_b = model.set_point(64.5, -77.0, label="D_b")

    # Line EG divided at F
    E = model.set_point(107.5, -16.0, classes=["given"], label="E")
    F = model.set_point(107.5, -85.0, classes=["given"], label="F")
    G = model.set_point(107.5, -160.0, classes=["given"], label="G")

    # Single-letter magnitude segment H
    H_t = model.set_point(150.0, -28.0, classes=["given"], label="H")
    H_b = model.set_point(150.0, -79.0, label="H_b")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(D_t, D_b)
    model.construct_line(E, G)
    model.construct_line(H_t, H_b)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(D_t, D_b)
    model.set_segment(E, G)
    model.set_segment(E, F)
    model.set_segment(F, G)
    model.set_segment(H_t, H_b)

    # Collinear sections
    model.set_section([A, C, B])
    model.set_section([E, F, G])

    return model


if __name__ == "__main__":
    construct_0108_g1()
