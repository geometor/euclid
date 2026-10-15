"""Programmatic construction for Book I, Proposition 8 Note — Philo's Proof Case II (0277.g3).

Philo's alternative proof of I. 8, Case II: when DF, FG form an angle interior
to the figure, with DG joined through EF.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0277_g3() -> Model:
    """Construct the figure for 0277.g3 using geometor.model."""
    model = Model("0277.g3")

    # Left triangle ABC
    A = model.set_point(84, -28, classes=["given"], label="A")
    B = model.set_point(18, -86, classes=["given"], label="B")
    C = model.set_point(106, -86, classes=["given"], label="C")

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_polygon([A, B, C])

    # Right figure DEF and applied triangle EGF with DG interior
    D = model.set_point(226, -28, classes=["given"], label="D")
    E = model.set_point(150, -86, classes=["given"], label="E")
    F = model.set_point(248, -86, classes=["given"], label="F")
    G = model.set_point(226, -144, label="G")

    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(E, G)
    model.set_segment(D, F)
    model.set_segment(F, G)
    model.set_segment(D, G)

    model.set_polygon([D, E, F])
    model.set_polygon([G, E, F])
    model.set_polygon([D, E, G])
    model.set_polygon([D, F, G])

    return model


if __name__ == "__main__":
    construct_0277_g3()
