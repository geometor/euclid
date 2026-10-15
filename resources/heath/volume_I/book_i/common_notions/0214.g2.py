"""Programmatic construction for Book I, Postulate 4 Note — Saccheri's Third Lemma (0214.g2).

Saccheri's third lemma: if two straight lines AB, CXD meet one another at an
intermediate point X, they do not touch at that point, but cut one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0214_g2() -> Model:
    """Construct the figure for 0214.g2 using geometor.model."""
    model = Model("0214.g2")

    # Straight line AB with intermediate point X
    A = model.set_point(18.0, -32.0, classes=["given"], label="A")
    X = model.set_point(71.0, -32.0, classes=["given"], label="X")
    B = model.set_point(151.0, -32.0, classes=["given"], label="B")

    # Supposed touching line CXD meeting AB at X without cutting
    C = model.set_point(27.0, -63.0, label="C")
    D = model.set_point(125.0, -82.0, label="D")

    model.set_segment(A, X)
    model.set_segment(X, B)
    model.set_segment(A, B)
    model.set_segment(C, X)
    model.set_segment(X, D)
    model.set_section([A, X, B])
    model.set_section([C, X, D])

    return model


if __name__ == "__main__":
    construct_0214_g2()
