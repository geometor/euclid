"""Programmatic construction for Book II, Definition 2 Gnomon Instrument (0385.g1).

Constructs the L-shaped carpenter's square / gnomon instrument illustrating the
mechanical origin of the term gnomon.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0385_g1() -> Model:
    """Construct the L-shaped gnomon instrument on folio 0385."""
    model = Model("0385.g1")

    # 6 vertices of the L-shaped gnomon instrument
    A = model.set_point(39, -124, classes=["given"], label="A")
    B = model.set_point(39, -16, classes=["given"], label="B")
    C = model.set_point(71, -16, label="C")
    D = model.set_point(71, -90, label="D")
    E = model.set_point(148, -90, label="E")
    F = model.set_point(148, -124, classes=["given"], label="F")

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, A)
    model.set_polygon([A, B, C, D, E, F])

    # Right angles at outer corner A and inner corner D
    model.set_wedge(A, B, B, F)
    model.set_wedge(D, C, C, E)

    return model


if __name__ == "__main__":
    construct_0385_g1()
