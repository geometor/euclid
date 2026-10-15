"""Programmatic construction for Book I, Proposition 6 Note — An-Nairīzī's Proof (0272.g1).

Alternative proof of I. 6 depending on I. 26, cutting off equal lengths BD, CE
along BA, CA and joining BE, CD.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0272_g1() -> Model:
    """Construct the figure for 0272.g1 using geometor.model."""
    model = Model("0272.g1")

    # 1. Triangle ABC with equal lengths BD, CE along BA, CA
    A = model.set_point(67, -24, classes=["given"], label="A")
    B = model.set_point(24, -117, classes=["given"], label="B")
    C = model.set_point(109, -117, classes=["given"], label="C")
    D = model.set_point(43, -77, label="D")
    E = model.set_point(91, -77, label="E")

    # Collinear sections and segments along AB and AC
    model.set_section([A, D, B])
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(A, B)

    model.set_section([A, E, C])
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(A, C)

    # Base BC and diagonals BE, CD
    model.set_segment(B, C)
    model.set_segment(B, E)
    model.set_segment(C, D)

    # Triangles compared in the proof
    model.set_polygon([A, B, C])
    model.set_polygon([D, B, C])
    model.set_polygon([E, C, B])
    model.set_polygon([A, B, E])
    model.set_polygon([A, C, D])
    model.set_polygon([A, B, D])

    return model


if __name__ == "__main__":
    construct_0272_g1()
