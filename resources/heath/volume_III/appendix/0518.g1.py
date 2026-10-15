"""Programmatic construction for Appendix I (Book XIV), Lemma to Prop. 2 (0518.g1).

In a circle ABC with centre D, if AC is the side of the inscribed regular pentagon
and BE is the diameter perpendicular to AC at F, then BA^2 + AC^2 = 5 DE^2.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0518_g1() -> Model:
    """Construct the figure 0518.g1 using geometor.model."""
    model = Model("0518.g1")

    # Circle centre D and vertical diameter endpoints B, E
    D = model.set_point(96.0, -114.0, classes=["given"], label="D")
    B = model.set_point(96.0, -28.0, classes=["given"], label="B")
    E = model.set_point(96.0, -200.0, classes=["given"], label="E")
    model.construct_circle(D, B)

    # Pentagon side AC and perpendicular intersection F
    A = model.set_point(46.0, -184.0, classes=["given"], label="A")
    C = model.set_point(146.0, -184.0, classes=["given"], label="C")
    F = model.set_point(96.0, -184.0, classes=["given"], label="F")

    # Polygons
    model.set_polygon([B, A, E])
    model.set_polygon([B, A, F])
    model.set_polygon([A, F, E])

    # Segments
    for p1, p2 in [
        (B, E), (B, D), (B, F), (D, E), (D, F), (F, E),
        (A, C), (A, F), (F, C),
        (A, B), (A, E),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0518_g1()
