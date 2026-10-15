"""Programmatic construction for Frontispiece: Bodleian MS. D'Orville 301 (0003.g1).

Constructs the Book III, Proposition 4 diagram visible on the manuscript facsimile
(circle ABCD with two intersecting non-diameter chords AC, BD meeting at E, and
center Z joined to E).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0003_g1() -> Model:
    """Construct the diagram on the Bodleian MS. D'Orville 301 facsimile."""
    model = Model("0003.g1")

    # Center Z and circumference point A for Circle ABCD
    Z = model.set_point(512, -420, classes=["given"], label="Z")
    A = model.set_point(439, -359, classes=["given"], label="A")
    model.construct_circle(Z, A)

    # Other points on the circle: B, C, D and intersection E of chords AC, BD
    B = model.set_point(450, -490, label="B")
    C = model.set_point(560, -504, label="C")
    D = model.set_point(595, -371, label="D")
    E = model.set_point(512, -445, label="E")

    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(Z, E)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(B, E)
    model.set_segment(E, D)

    return model


if __name__ == "__main__":
    construct_0003_g1()
