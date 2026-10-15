"""Programmatic construction for Book VI, Proposition 17 (0234.g1).

Three proportional straight lines A, B, C and auxiliary straight line D = B.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0234_g1() -> Model:
    """Construct the figure for 0234.g1 (VI.17) using geometor.model."""
    model = Model("0234.g1")

    # 1. Endpoints of the four straight lines A, B, D, C
    A1 = model.set_point(79.0, -19.0, classes=["given"], label="A1")
    A2 = model.set_point(265.0, -19.0, classes=["given"], label="A2")

    B1 = model.set_point(29.0, -53.0, classes=["given"], label="B1")
    B2 = model.set_point(149.0, -53.0, classes=["given"], label="B2")

    D1 = model.set_point(193.0, -53.0, classes=["given"], label="D1")
    D2 = model.set_point(312.0, -53.0, classes=["given"], label="D2")

    C1 = model.set_point(33.0, -84.0, classes=["given"], label="C1")
    C2 = model.set_point(108.0, -84.0, classes=["given"], label="C2")

    # 2. Segments
    model.set_segment(A1, A2)
    model.set_segment(B1, B2)
    model.set_segment(D1, D2)
    model.set_segment(C1, C2)

    return model


if __name__ == "__main__":
    construct_0234_g1()
