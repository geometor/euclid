"""Programmatic construction for Book I, Proposition 9 (0278.g2).

To bisect a given rectilineal angle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0278_g2() -> Model:
    """Construct the figure for Book I, Proposition 9 using geometor.model."""
    model = Model("0278.g2")

    # 1. Given rectilineal angle BAC
    A = model.set_point(52, -12, classes=["given"], label="A")
    B = model.set_point(19, -114, classes=["given"], label="B")
    C = model.set_point(85, -114, classes=["given"], label="C")

    model.construct_line(A, B)
    model.construct_line(A, C)

    # 2. Point D taken at random on AB, and AE cut off from AC equal to AD [I. 3]
    D = model.set_point(33, -72, label="D")
    E = model.set_point(71, -72, label="E")

    model.set_section([A, D, B])
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(A, B)

    model.set_section([A, E, C])
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(A, C)

    # 3. Join DE, construct equilateral triangle DEF on DE [I. 1], and join AF
    F = model.set_point(52, -105, label="F")
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(E, F)
    model.set_segment(A, F)

    model.set_polygon([A, D, E])
    model.set_polygon([D, E, F])
    model.set_polygon([A, D, F])
    model.set_polygon([A, E, F])

    return model


if __name__ == "__main__":
    construct_0278_g2()
