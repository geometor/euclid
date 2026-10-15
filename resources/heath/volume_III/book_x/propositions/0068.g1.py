"""Programmatic construction for Book X, Proposition 28, Lemma 2 (0068.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0068_g1() -> Model:
    """Construct the figure 0068.g1 using geometor.model."""
    model = Model("0068.g1")

    # Collinear points A, G, H, D, E, F, C, B on line AB
    A = model.set_point(15.0, -34.0, classes=["given"], label="A")
    G = model.set_point(46.0, -34.0, label="G")
    H = model.set_point(83.0, -34.0, label="H")
    D = model.set_point(101.0, -34.0, label="D")
    E = model.set_point(123.0, -34.0, label="E")
    F = model.set_point(145.0, -34.0, label="F")
    C = model.set_point(201.0, -34.0, classes=["given"], label="C")
    B = model.set_point(263.0, -34.0, classes=["given"], label="B")

    # Base line
    model.construct_line(A, B)

    # All referenced segments and sub-segments
    pts = [A, G, H, D, E, F, C, B]
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            model.set_segment(pts[i], pts[j])

    # Key collinear sections
    model.set_section([A, D, C])
    model.set_section([G, E, C])
    model.set_section([H, F, C])
    model.set_section([A, C, B])

    return model


if __name__ == "__main__":
    construct_0068_g1()
