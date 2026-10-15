"""Programmatic construction for Book I, Proposition 8 Note — Philo's Proof Case I (0277.g2).

Philo's alternative proof of I. 8, Case I: when FG is in a straight line with DF,
forming the single isosceles triangle DEG.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0277_g2() -> Model:
    """Construct the figure for 0277.g2 using geometor.model."""
    model = Model("0277.g2")

    # Left triangle ABC
    A = model.set_point(104, -30, classes=["given"], label="A")
    B = model.set_point(20, -92, classes=["given"], label="B")
    C = model.set_point(104, -92, classes=["given"], label="C")

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_polygon([A, B, C])

    # Right figure DEF and applied triangle EGF with D-F-G collinear
    D = model.set_point(210, -30, classes=["given"], label="D")
    E = model.set_point(124, -92, classes=["given"], label="E")
    F = model.set_point(210, -92, classes=["given"], label="F")
    G = model.set_point(210, -154, label="G")

    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(E, G)
    model.set_section([D, F, G])
    model.set_segment(D, F)
    model.set_segment(F, G)
    model.set_segment(D, G)

    model.set_polygon([D, E, F])
    model.set_polygon([G, E, F])
    model.set_polygon([D, E, G])

    return model


if __name__ == "__main__":
    construct_0277_g2()
