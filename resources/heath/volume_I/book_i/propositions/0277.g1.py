"""Programmatic construction for Book I, Proposition 8 Note — Aristotle's Rainbow Locus (0277.g1).

Aristotle's Meteorologica III. 3 diagram showing equal broken rays ACB, AFB, ADB
reflected from A to B with perpendiculars CE, FE, DE meeting at center E on AEB.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0277_g1() -> Model:
    """Construct the figure for 0277.g1 using geometor.model."""
    model = Model("0277.g1")

    # Axis AEB and points C, F, D on the circle with center E
    A = model.set_point(28, -69, classes=["given"], label="A")
    E = model.set_point(138, -69, label="E")
    B = model.set_point(182, -69, classes=["given"], label="B")
    C = model.set_point(138, -25, label="C")
    D = model.set_point(138, -107, label="D")
    F = model.set_point(152, -73, label="F")

    # Axis segments
    model.set_section([A, E, B])
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(A, B)

    # Reflected rays from A and B to C, F, D
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(A, F)
    model.set_segment(F, B)
    model.set_segment(A, D)
    model.set_segment(D, B)

    # Perpendiculars CE, FE, DE to AEB
    model.set_segment(C, E)
    model.set_segment(F, E)
    model.set_segment(D, E)
    model.set_segment(C, D)

    # Triangles ACB, AFB, ADB
    model.set_polygon([A, C, B])
    model.set_polygon([A, F, B])
    model.set_polygon([A, D, B])

    return model


if __name__ == "__main__":
    construct_0277_g1()
