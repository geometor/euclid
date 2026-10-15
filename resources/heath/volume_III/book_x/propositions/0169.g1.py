"""Programmatic construction for Book X, Proposition 78 (0169.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0169_g1() -> Model:
    """Construct the figure 0169.g1 using geometor.model."""
    model = Model("0169.g1")

    # Rectangle DE applied to rational straight line DI, divided by FH into DH and FE
    D = model.set_point(18.5, -18.5, classes=["given"], label="D")
    F = model.set_point(175.5, -18.5, label="F")
    G = model.set_point(199.5, -18.5, label="G")
    I = model.set_point(18.5, -112.0, classes=["given"], label="I")
    H = model.set_point(175.5, -112.0, label="H")
    E = model.set_point(199.5, -112.0, label="E")

    # Straight line AB with straight line BC subtracted, leaving AC
    A = model.set_point(54.0, -139.5, classes=["given"], label="A")
    C = model.set_point(111.0, -139.5, classes=["given"], label="C")
    B = model.set_point(168.0, -139.5, classes=["given"], label="B")

    # Base lines
    model.construct_line(D, G)
    model.construct_line(I, E)
    model.construct_line(D, I)
    model.construct_line(F, H)
    model.construct_line(G, E)
    model.construct_line(A, B)

    # Segments
    model.set_segment(D, I)
    model.set_segment(F, H)
    model.set_segment(G, E)
    model.set_segment(D, G)
    model.set_segment(D, F)
    model.set_segment(F, G)
    model.set_segment(I, E)
    model.set_segment(I, H)
    model.set_segment(H, E)

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Sections
    model.set_section([D, F, G])
    model.set_section([I, H, E])
    model.set_section([A, C, B])

    # Polygons
    model.set_polygon([D, I, E, G])
    model.set_polygon([D, I, H, F])
    model.set_polygon([F, H, E, G])

    return model


if __name__ == "__main__":
    construct_0169_g1()
