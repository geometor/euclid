"""Programmatic construction for Pappus Analysis of Circle Tangent Problem (0156.g1).

Given circle ABC and points D, E on a line FED, FA is tangent to the circle at A,
secant ABE passes through E and meets the circle at B and A, and DB produced
meets the circle at C, making AC parallel to DE.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0156_g1() -> Model:
    """Construct the Pappus analysis figure on folio 0156."""
    model = Model("0156.g1")

    # Center O (unlabeled) and circumference points A, B, C
    O = model.set_point(144.5, -76.0, classes=["given"], label="O")
    A = model.set_point(89.7, -44.0, classes=["given"], label="A")
    B = model.set_point(167.0, -135.4, label="B")
    C = model.set_point(199.3, -44.0, label="C")
    model.construct_circle(O, A)

    # Collinear points F, D, E on horizontal base line
    F = model.set_point(7.5, -181.5, label="F")
    D = model.set_point(150.7, -181.5, classes=["given"], label="D")
    E = model.set_point(206.0, -181.5, classes=["given"], label="E")

    model.construct_line(F, E)
    model.set_segment(F, E)
    model.set_segment(F, D)
    model.set_segment(D, E)

    # Tangent FA
    model.construct_line(F, A)
    model.set_segment(F, A)

    # Chord AC parallel to DE
    model.construct_line(A, C)
    model.set_segment(A, C)

    # Secant ABE
    model.construct_line(A, E)
    model.set_segment(A, E)
    model.set_segment(A, B)
    model.set_segment(B, E)

    # Secant DBC
    model.construct_line(D, C)
    model.set_segment(D, C)
    model.set_segment(D, B)
    model.set_segment(B, C)

    # Referenced angles FAE, BDE, ACB
    model.set_wedge(A, F, F, E)  # < F A E )
    model.set_wedge(D, B, B, E)  # < B D E )
    model.set_wedge(C, A, A, B)  # < A C B )

    return model


if __name__ == "__main__":
    construct_0156_g1()
