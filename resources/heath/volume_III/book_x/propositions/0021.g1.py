"""Programmatic construction for Book X, Proposition 2 (0021.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0021_g1() -> Model:
    """Construct the magnitude bars E, AB, CD for Book X, Proposition 2 (0021.g1)."""
    model = Model("0021.g1")

    # Single-letter magnitude E
    E_l = model.set_point(70.0, -23.5, classes=["given"], label="E")
    E_r = model.set_point(118.0, -23.5, label="E_r")

    # Subdivided magnitude AB (divided at G)
    A = model.set_point(205.0, -23.5, classes=["given"], label="A")
    G = model.set_point(230.0, -23.5, label="G")
    B = model.set_point(339.0, -23.5, classes=["given"], label="B")

    # Subdivided magnitude CD (divided at F)
    C = model.set_point(17.0, -50.0, classes=["given"], label="C")
    F = model.set_point(75.0, -50.0, label="F")
    D = model.set_point(337.0, -50.0, classes=["given"], label="D")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Magnitude E
    model.set_segment(E_l, E_r)

    # Segments on AB
    model.set_segment(A, G)
    model.set_segment(G, B)
    model.set_segment(A, B)

    # Segments on CD
    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_segment(C, D)

    # Sections
    model.set_section([A, G, B])
    model.set_section([C, F, D])

    return model


if __name__ == "__main__":
    construct_0021_g1()
