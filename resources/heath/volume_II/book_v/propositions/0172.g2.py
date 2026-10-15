"""Programmatic construction for Book V, Proposition 16 Commentary (0172.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0172_g2() -> Model:
    """Construct the figure 0172.g2 (Smith & Bryant straight-line proof of V.16)."""
    model = Model("0172.g2")

    # Top row: a (16, 24), b (136, 24), c (197, 24), d (292, 24), e (341, 24)
    a = model.set_point(16.00, -24.00, classes=["given"], label="a")
    b = model.set_point(136.00, -24.00, classes=["given"], label="b")
    c = model.set_point(197.00, -24.00, classes=["given"], label="c")
    d = model.set_point(292.00, -24.00, classes=["given"], label="d")
    e = model.set_point(341.00, -24.00, classes=["given"], label="e")

    # Bottom row: A (16, 80), B (136, 80), C (197, 80), D (292, 80), E (341, 80)
    A = model.set_point(16.00, -80.00, classes=["given"], label="A")
    B = model.set_point(136.00, -80.00, classes=["given"], label="B")
    C = model.set_point(197.00, -80.00, classes=["given"], label="C")
    D = model.set_point(292.00, -80.00, classes=["given"], label="D")
    E = model.set_point(341.00, -80.00, classes=["given"], label="E")

    # Polygons (rectangles Ab, Bc, Cd, De)
    model.set_polygon([A, E, e, a])
    model.set_polygon([A, B, b, a])
    model.set_polygon([B, C, c, b])
    model.set_polygon([C, D, d, c])
    model.set_polygon([D, E, e, d])

    # Bottom segments
    model.set_segment(A, E)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)

    # Top segments
    model.set_segment(a, e)
    model.set_segment(a, b)
    model.set_segment(b, c)
    model.set_segment(c, d)
    model.set_segment(d, e)

    # Vertical segments
    model.set_segment(A, a)
    model.set_segment(B, b)
    model.set_segment(C, c)
    model.set_segment(D, d)
    model.set_segment(E, e)

    return model


if __name__ == "__main__":
    construct_0172_g2()
