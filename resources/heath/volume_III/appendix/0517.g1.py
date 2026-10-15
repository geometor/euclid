"""Programmatic construction for Appendix I (Book XIV), Proposition 1 (0517.g1).

Hypsicles' theorem that the perpendicular DE from the centre D of a circle ABC
to the side BC of the inscribed regular pentagon is half the sum of the side DF
of the inscribed regular hexagon and the side FC of the inscribed regular decagon.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0517_g1() -> Model:
    """Construct the figure 0517.g1 using geometor.model."""
    model = Model("0517.g1")

    # Circle centre D and vertical diameter endpoints A, F
    D = model.set_point(95.0, -114.0, classes=["given"], label="D")
    A = model.set_point(95.0, -29.0, classes=["given"], label="A")
    F = model.set_point(95.0, -199.0, classes=["given"], label="F")
    model.construct_circle(D, A)

    # Side BC of the inscribed regular pentagon and perpendicular foot E
    C = model.set_point(44.0, -182.0, classes=["given"], label="C")
    B = model.set_point(146.0, -182.0, classes=["given"], label="B")
    E = model.set_point(95.0, -182.0, classes=["given"], label="E")

    # Point G on DE such that GE = EF
    G = model.set_point(95.0, -158.0, classes=["given"], label="G")

    # Polygons (triangles)
    model.set_polygon([D, B, C])
    model.set_polygon([D, C, E])
    model.set_polygon([D, B, E])
    model.set_polygon([C, D, G])
    model.set_polygon([C, G, F])
    model.set_polygon([C, E, G])
    model.set_polygon([C, E, F])
    model.set_polygon([D, C, F])

    # Segments along vertical diameter A-D-G-E-F, chord C-E-B, and radii/chords
    for p1, p2 in [
        (A, F), (A, D), (A, G), (A, E),
        (D, F), (D, E), (D, G),
        (G, F), (G, E), (E, F),
        (B, C), (C, E), (E, B),
        (D, C), (D, B), (G, C), (C, F),
    ]:
        model.set_segment(p1, p2)

    # Angles referenced in proof
    model.set_wedge(D, A, A, C)
    model.set_wedge(D, C, C, F)
    model.set_wedge(F, A, A, C)
    model.set_wedge(G, C, C, F)
    model.set_wedge(D, C, C, G)
    model.set_wedge(C, D, D, G)

    return model


if __name__ == "__main__":
    construct_0517_g1()
