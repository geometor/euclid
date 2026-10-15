"""Programmatic construction for Book I, Proposition 26 note - The Ambiguous Case (0320.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0320_g1() -> Model:
    """Construct the figure for the Ambiguous Case (0320.g1) using geometor.model."""
    model = Model("0320.g1")

    # 1. Triangle ABC
    A = model.set_point(111, -23, classes=["given"], label="A")
    B = model.set_point(18, -98, classes=["given"], label="B")
    C = model.set_point(151, -98, classes=["given"], label="C")

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_polygon([A, B, C])

    # 2. Triangle DEF with produced base EF to G and segment DG
    D = model.set_point(414, -22, classes=["given"], label="D")
    E = model.set_point(322, -98, classes=["given"], label="E")
    F = model.set_point(380, -98, classes=["given"], label="F")
    G = model.set_point(457, -98, label="G")

    model.construct_line(E, F)
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(D, G)
    model.set_segment(E, F)
    model.set_segment(F, G)
    model.set_segment(E, G)
    model.set_section([E, F, G])

    model.set_polygon([D, E, F])
    model.set_polygon([D, F, G])
    model.set_polygon([D, E, G])

    # Angles
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, A, A, C)
    model.set_wedge(C, A, A, B)

    model.set_wedge(D, E, E, F)
    model.set_wedge(D, E, E, G)
    model.set_wedge(E, D, D, F)
    model.set_wedge(F, D, D, E)
    model.set_wedge(F, D, D, G)
    model.set_wedge(G, D, D, F)

    return model


if __name__ == "__main__":
    construct_0320_g1()
