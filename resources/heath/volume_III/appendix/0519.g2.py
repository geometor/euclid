"""Programmatic construction for Appendix I (Book XIV), Proposition 4 (0519.g2).

If ABC is an equilateral triangle inscribed in a circle with centre D, and DE is
perpendicular to BC, then 30 BC * DE equals the surface of the icosahedron
(20 times the area of the triangle ABC).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0519_g2() -> Model:
    """Construct the figure 0519.g2 using geometor.model."""
    model = Model("0519.g2")

    # Circle centre D and inscribed equilateral triangle ABC
    D = model.set_point(80.0, -88.0, classes=["given"], label="D")
    A = model.set_point(80.0, -20.0, classes=["given"], label="A")
    B = model.set_point(21.0, -122.0, classes=["given"], label="B")
    C = model.set_point(139.0, -122.0, classes=["given"], label="C")
    model.construct_circle(D, A)

    # Foot E of perpendicular from D to BC
    E = model.set_point(80.0, -122.0, classes=["given"], label="E")

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([D, B, C])
    model.set_polygon([D, B, E])
    model.set_polygon([D, C, E])

    # Segments
    for p1, p2 in [
        (A, B), (B, C), (B, E), (E, C), (C, A),
        (D, B), (D, C), (D, E),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0519_g2()
