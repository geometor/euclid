"""Programmatic construction for Book XII, Proposition 15 Note (0426.g1).

Legendre's cylinder theorem diagram: concentric circles with center C and radii
CD, CA, with a regular octagon GHI... circumscribed about the inner circle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0426_g1() -> Model:
    """Construct the figure 0426.g1 using geometor.model."""
    model = Model("0426.g1")

    C = model.set_point(120.0, -122.0, classes=["given"], label="C")
    D = model.set_point(120.0, -42.0, classes=["given"], label="D")
    A = model.set_point(120.0, -26.0, classes=["given"], label="A")

    # Regular octagon vertices circumscribed about circle (C, D)
    G = model.set_point(86.9, -42.0, classes=["given"], label="G")
    H = model.set_point(153.1, -42.0, classes=["given"], label="H")
    I = model.set_point(200.0, -88.9, classes=["given"], label="I")
    P4 = model.set_point(200.0, -155.1, label="P4")
    P5 = model.set_point(153.1, -202.0, label="P5")
    P6 = model.set_point(86.9, -202.0, label="P6")
    P7 = model.set_point(40.0, -155.1, label="P7")
    P8 = model.set_point(40.0, -88.9, label="P8")

    # Concentric circles
    model.construct_circle(C, D)
    model.construct_circle(C, A)

    # Radius segments and octagon sides
    model.set_segment(C, D)
    model.set_segment(D, A)
    model.set_segment(C, A)

    octagon = [G, H, I, P4, P5, P6, P7, P8]
    for idx in range(len(octagon)):
        model.set_segment(octagon[idx], octagon[(idx + 1) % len(octagon)])
    model.set_polygon(octagon)

    return model


if __name__ == "__main__":
    construct_0426_g1()
