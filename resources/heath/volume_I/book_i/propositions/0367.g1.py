"""Programmatic construction for Proposition 47 Commentary (0367.g1).

Proof of the Pythagorean theorem by similar triangles ABC, DBA, and DAC.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0367_g1() -> Model:
    """Construct the figure of 0367.g1 using geometor.model."""
    model = Model("0367.g1")

    # Right-angled triangle ABC with right angle at A and altitude AD to BC
    A = model.set_point(65, -36, classes=["given"], label="A")
    B = model.set_point(26, -98, classes=["given"], label="B")
    C = model.set_point(184, -98, classes=["given"], label="C")
    D = model.set_point(65, -98, label="D")

    # Triangles ABC, DBA, DAC
    model.set_polygon([A, B, C])
    model.set_polygon([D, B, A])
    model.set_polygon([D, A, C])

    # Segments BC, BD, CD, BA, CA, AD
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(C, D)
    model.set_segment(B, A)
    model.set_segment(C, A)
    model.set_segment(A, D)

    # Angles
    model.set_wedge(A, B, B, C)  # < B A C )
    model.set_wedge(D, A, A, B)  # < A D B )
    model.set_wedge(D, A, A, C)  # < A D C )

    return model


if __name__ == "__main__":
    construct_0367_g1()
