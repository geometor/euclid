"""Programmatic construction for Book I, Common Notion 1 commentary (0236.g1).

Apollonius's attempted proof of Common Notion 1 using three equal magnitudes A, B, C.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0236_g1() -> Model:
    """Construct the figure for 0236.g1 using geometor.model."""
    model = Model("0236.g1")

    # Three equal vertical line segments representing magnitudes A, B, C
    pt_A1 = model.set_point(26, -20, classes=["given"], label="A1")
    pt_A2 = model.set_point(26, -70, classes=["given"], label="A")

    pt_B1 = model.set_point(52, -20, classes=["given"], label="B1")
    pt_B2 = model.set_point(52, -70, classes=["given"], label="B")

    pt_C1 = model.set_point(78, -20, classes=["given"], label="C1")
    pt_C2 = model.set_point(78, -70, classes=["given"], label="C")

    model.set_segment(pt_A1, pt_A2)
    model.set_segment(pt_B1, pt_B2)
    model.set_segment(pt_C1, pt_C2)

    return model


if __name__ == "__main__":
    construct_0236_g1()
