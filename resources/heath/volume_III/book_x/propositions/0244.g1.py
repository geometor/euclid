"""Programmatic construction for Book X, Proposition 111 (0244.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0244_g1() -> Model:
    """Construct the figure 0244.g1 using geometor.model."""
    model = Model("0244.g1")

    # Top line AB
    A = model.set_point(30.0, -19.5, classes=["given"], label="A")
    B = model.set_point(154.0, -19.5, classes=["given"], label="B")

    # Top edge of applied rectangle and produced line: D - G - E - F
    D = model.set_point(20.5, -54.0, classes=["given"], label="D")
    G = model.set_point(78.0, -54.0, label="G")
    E = model.set_point(111.5, -54.0, label="E")
    F = model.set_point(184.0, -54.0, label="F")

    # Bottom edge of applied rectangle: C - E_b
    C = model.set_point(20.5, -219.5, classes=["given"], label="C")
    E_b = model.set_point(111.5, -219.5, label="E_b")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(D, F)
    model.construct_line(D, C)
    model.construct_line(E, E_b)
    model.construct_line(C, E_b)

    # Segments
    model.set_segment(A, B)
    model.set_segment(D, C)
    model.set_segment(E, E_b)
    model.set_segment(C, E_b)
    model.set_segment(D, F)
    model.set_segment(D, E)
    model.set_segment(D, G)
    model.set_segment(G, F)
    model.set_segment(G, E)
    model.set_segment(E, F)

    # Sections
    model.set_section([D, G, E])
    model.set_section([D, E, F])
    model.set_section([D, G, F])

    # Polygon (rectangle CE)
    model.set_polygon([D, E, E_b, C])

    return model


if __name__ == "__main__":
    construct_0244_g1()
