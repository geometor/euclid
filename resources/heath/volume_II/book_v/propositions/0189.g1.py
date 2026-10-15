"""Programmatic construction for Book V, Proposition 23 Commentary (0189.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0189_g1() -> Model:
    """Construct the figure 0189.g1 (Simson's Four Magnitudes Cross Order Table) using geometor.model."""
    model = Model("0189.g1")

    # Bounding box corners
    P_1 = model.set_point(6.00, -6.00, classes=["given"], label="P_1")
    P_2 = model.set_point(124.00, -6.00, classes=["given"], label="P_2")
    P_3 = model.set_point(124.00, -54.00, classes=["given"], label="P_3")
    P_4 = model.set_point(6.00, -54.00, classes=["given"], label="P_4")
    model.set_polygon([P_1, P_2, P_3, P_4])

    # Top row magnitudes A, B, C, D
    model.set_point(26.00, -20.00, classes=["given"], label="A")
    model.set_point(52.00, -20.00, classes=["given"], label="B")
    model.set_point(78.00, -20.00, classes=["given"], label="C")
    model.set_point(104.00, -20.00, classes=["given"], label="D")

    # Bottom row magnitudes E, F, G, H
    model.set_point(26.00, -41.00, classes=["given"], label="E")
    model.set_point(52.00, -41.00, classes=["given"], label="F")
    model.set_point(78.00, -41.00, classes=["given"], label="G")
    model.set_point(104.00, -41.00, classes=["given"], label="H")

    return model


if __name__ == "__main__":
    construct_0189_g1()
