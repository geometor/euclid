"""Programmatic construction for Book V, Proposition 5 (0151.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0151_g1() -> Model:
    """Construct the figure 0151.g1 for Book V, Proposition 5 using geometor.model."""
    model = Model("0151.g1")

    # Magnitude AB subdivided at E (with intermediate multiple marks A_1, A_2, E_1, E_2)
    A = model.set_point(22.0, -33.0, classes=["given"], label="A")
    A_1 = model.set_point(77.0, -33.0, label="A_1")
    A_2 = model.set_point(133.0, -33.0, label="A_2")
    E = model.set_point(188.0, -33.0, classes=["given"], label="E")
    E_1 = model.set_point(225.0, -33.0, label="E_1")
    E_2 = model.set_point(261.0, -33.0, label="E_2")
    B = model.set_point(298.0, -33.0, classes=["given"], label="B")

    # Magnitude GD subdivided at C and F
    G = model.set_point(101.0, -62.0, label="G")
    C = model.set_point(142.0, -62.0, classes=["given"], label="C")
    F = model.set_point(195.0, -62.0, classes=["given"], label="F")
    D = model.set_point(235.0, -62.0, classes=["given"], label="D")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(G, D)

    # Segments on AB
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)

    # Segments on GD
    model.set_segment(G, D)
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_segment(C, G)
    model.set_segment(G, F)

    return model


if __name__ == "__main__":
    construct_0151_g1()
