"""Programmatic construction for Book I, Proposition 8 Note — Philo's Proof Case III (0278.g1).

Philo's alternative proof of I. 8, Case III: when DF, FG form an angle exterior
to the figure, with DG joined outside F.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0278_g1() -> Model:
    """Construct the figure for 0278.g1 using geometor.model."""
    model = Model("0278.g1")

    # Left triangle ABC
    A = model.set_point(100, -28, classes=["given"], label="A")
    B = model.set_point(12, -70, classes=["given"], label="B")
    C = model.set_point(76, -70, classes=["given"], label="C")

    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_polygon([A, B, C])

    # Right figure DEF and applied triangle EGF with DG exterior
    D = model.set_point(238, -28, classes=["given"], label="D")
    E = model.set_point(148, -70, classes=["given"], label="E")
    F = model.set_point(212, -70, classes=["given"], label="F")
    G = model.set_point(238, -112, label="G")

    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(E, G)
    model.set_segment(D, F)
    model.set_segment(F, G)
    model.set_segment(D, G)

    model.set_polygon([D, E, F])
    model.set_polygon([G, E, F])
    model.set_polygon([D, F, G])
    model.set_polygon([D, E, G])
    model.set_polygon([D, E, G, F])

    return model


if __name__ == "__main__":
    construct_0278_g1()
