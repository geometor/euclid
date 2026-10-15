"""Programmatic construction for Book X, Proposition 13 Lemma (0040.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0040_g2() -> Model:
    """Construct the figure 0040.g2 using geometor.model."""
    model = Model("0040.g2")

    # Diameter AB and midpoint M of semicircle ADB
    A = model.set_point(19.5, -90.0, classes=["given"], label="A")
    B = model.set_point(162.5, -90.0, classes=["given"], label="B")
    M = model.set_point(91.0, -90.0, label="M")
    D = model.set_point(55.0, -28.1, label="D")

    # Standalone given straight line C
    C_t = model.set_point(206.5, -18.0, classes=["given"], label="C")
    C_b = model.set_point(206.5, -90.0, label="C_b")

    # Base lines and circle (semicircle ADB)
    model.construct_line(A, B)
    model.construct_line(A, D)
    model.construct_line(D, B)
    model.construct_circle(M, B)
    model.construct_line(C_t, C_b)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(C_t, C_b)

    # Inscribed right triangle ADB
    model.set_polygon([A, D, B])

    # Right angle ADB
    model.set_wedge(D, A, A, B)

    return model


if __name__ == "__main__":
    construct_0040_g2()
