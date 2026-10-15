"""Programmatic construction for Book I, Proposition 9 Note — Proclus' Objections (0279.g2).

Refutation of the objection that the vertex F of the equilateral triangle DEF
might fall either on one of the rays AB (first figure) or outside the angle BAC
altogether (second figure).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0279_g2() -> Model:
    """Construct the two-case figure for 0279.g2 using geometor.model."""
    model = Model("0279.g2")

    # Left Figure: F falls on ray AB
    A1 = model.set_point(91, -28, classes=["given"], label="A")
    B1 = model.set_point(18, -146, classes=["given"], label="B")
    C1 = model.set_point(155, -134, classes=["given"], label="C")
    D1 = model.set_point(56, -80, label="D")
    E1 = model.set_point(126, -80, label="E")
    F1 = model.set_point(34, -118, label="F")

    model.set_segment(A1, D1)
    model.set_segment(D1, F1)
    model.set_segment(F1, B1)
    model.set_segment(D1, B1)
    model.set_segment(A1, B1)
    model.set_segment(A1, E1)
    model.set_segment(E1, C1)
    model.set_segment(A1, C1)
    model.set_segment(D1, E1)
    model.set_segment(E1, F1)
    model.set_polygon([A1, D1, E1])
    model.set_polygon([D1, E1, F1])

    # Right Figure: F falls outside angle BAC
    A2 = model.set_point(261, -28, classes=["given"], label="A'")
    B2 = model.set_point(196, -134, classes=["given"], label="B'")
    C2 = model.set_point(328, -134, classes=["given"], label="C'")
    D2 = model.set_point(226, -80, label="D'")
    E2 = model.set_point(296, -80, label="E'")
    F2 = model.set_point(182, -118, label="F'")

    model.set_segment(A2, D2)
    model.set_segment(D2, B2)
    model.set_segment(A2, B2)
    model.set_segment(A2, E2)
    model.set_segment(E2, C2)
    model.set_segment(A2, C2)
    model.set_segment(D2, E2)
    model.set_segment(D2, F2)
    model.set_segment(E2, F2)
    model.set_polygon([A2, D2, E2])
    model.set_polygon([D2, E2, F2])

    return model


if __name__ == "__main__":
    construct_0279_g2()
