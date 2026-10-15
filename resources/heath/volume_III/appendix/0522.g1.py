"""Programmatic construction for Appendix I (Book XIV), Lemma to Prop. 8 (0522.g1).

Two straight lines AB (cut at C) and DE (cut at F) divided in extreme and mean
ratio have their segments in the same ratio: AB : AC = DE : DF.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0522_g1() -> Model:
    """Construct the figure 0522.g1 using geometor.model."""
    model = Model("0522.g1")

    # Upper line A-C-B
    A = model.set_point(14.0, -25.0, classes=["given"], label="A")
    C = model.set_point(108.0, -25.0, classes=["given"], label="C")
    B = model.set_point(168.0, -25.0, classes=["given"], label="B")

    # Lower line D-F-E
    D = model.set_point(36.0, -54.0, classes=["given"], label="D")
    F = model.set_point(98.0, -54.0, classes=["given"], label="F")
    E = model.set_point(136.0, -54.0, classes=["given"], label="E")

    # Sections
    model.set_section([A, C, B])
    model.set_section([D, F, E])

    # Segments
    for p1, p2 in [
        (A, B), (A, C), (C, B),
        (D, E), (D, F), (F, E),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0522_g1()
