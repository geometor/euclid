"""Programmatic construction for Book III, Proposition 23 (0058.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0058_g2() -> Model:
    """Construct the figure 0058.g2 using geometor.model."""
    model = Model("0058.g2")

    # Base points A, B and circle centers O1 (for ACB) and O2 (for ADB) (y-inverted)
    A = model.set_point(28.00, -66.00, classes=["given"], label="A")
    B = model.set_point(164.00, -66.00, classes=["given"], label="B")
    O1 = model.set_point(96.00, -127.97, label="O1")
    O2 = model.set_point(96.00, -104.21, label="O2")
    C = model.set_point(105.21, -36.43, label="C")
    D = model.set_point(121.08, -30.35, label="D")

    # Circles for segments ACB and ADB
    model.construct_circle(O1, A)
    model.construct_circle(O2, A)

    # Segments and secant ACD
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, D)
    model.set_segment(A, D)
    model.set_segment(C, B)
    model.set_segment(D, B)
    model.set_section([A, C, D])

    # Polygons
    model.set_polygon([A, C, B])
    model.set_polygon([A, D, B])
    model.set_polygon([C, D, B])

    # Angles (wedges)
    model.set_wedge(C, A, A, B)
    model.set_wedge(D, A, A, B)

    return model


if __name__ == "__main__":
    construct_0058_g2()
