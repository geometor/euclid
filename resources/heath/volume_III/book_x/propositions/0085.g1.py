"""Programmatic construction for Book X, Proposition 35 (0085.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0085_g1() -> Model:
    """Construct the figure 0085.g1 using geometor.model."""
    model = Model("0085.g1")

    # Diameter AB extended to C, with E bisecting BC, F on AB, and D on semicircle ADB
    A = model.set_point(19.0, -109.0, classes=["given"], label="A")
    F = model.set_point(186.5, -109.0, label="F")
    B = model.set_point(204.0, -109.0, classes=["given"], label="B")
    E = model.set_point(257.0, -109.0, label="E")
    C = model.set_point(310.0, -109.0, classes=["given"], label="C")
    O = model.set_point(111.5, -109.0, label="O")
    D = model.set_point(186.5, -54.9, label="D")

    # Base lines and semicircle ADB
    model.construct_line(A, C)
    model.construct_circle(O, A)
    model.construct_line(A, D)
    model.construct_line(D, B)
    model.construct_line(F, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(B, E)
    model.set_segment(E, C)
    model.set_segment(A, F)
    model.set_segment(F, B)
    model.set_segment(F, D)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(A, C)
    model.set_segment(A, E)
    model.set_segment(F, C)
    model.set_segment(F, E)

    # Sections
    model.set_section([A, F, B])
    model.set_section([B, E, C])
    model.set_section([A, B, C])

    # Inscribed right triangles ADB, ADF, DFB
    model.set_polygon([A, D, B])
    model.set_polygon([A, D, F])
    model.set_polygon([D, F, B])

    # Right angles at D and F
    model.set_wedge(D, A, A, B)
    model.set_wedge(F, D, A, D)
    model.set_wedge(F, D, D, B)

    return model


if __name__ == "__main__":
    construct_0085_g1()
