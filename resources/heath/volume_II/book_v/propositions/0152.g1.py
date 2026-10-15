"""Programmatic construction for Book V, Proposition 5 Simson note (0152.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0152_g1() -> Model:
    """Construct the figure 0152.g1 (Simson's construction for V.5) using geometor.model."""
    model = Model("0152.g1")

    # Left vertical line G-A-E-B
    G = model.set_point(24.0, -15.0, label="G")
    A = model.set_point(24.0, -78.0, classes=["given"], label="A")
    E = model.set_point(24.0, -194.0, classes=["given"], label="E")
    B = model.set_point(24.0, -272.0, classes=["given"], label="B")

    # Right vertical line C-F-D
    C = model.set_point(53.0, -140.0, classes=["given"], label="C")
    F = model.set_point(53.0, -231.0, classes=["given"], label="F")
    D = model.set_point(53.0, -272.0, classes=["given"], label="D")

    # Base lines
    model.construct_line(G, B)
    model.construct_line(C, D)

    # Segments along left line
    model.set_segment(G, B)
    model.set_segment(A, G)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(A, B)
    model.set_segment(E, G)

    # Segments along right line
    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)

    return model


if __name__ == "__main__":
    construct_0152_g1()
