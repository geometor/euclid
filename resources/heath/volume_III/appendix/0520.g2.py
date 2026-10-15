"""Programmatic construction for Appendix I (Book XIV), Prop. 6 Preliminary (0520.g2).

Preliminary lemma for the alternative proof of Prop. 6: if ABC is a circle with
inscribed regular pentagon, centre D, vertical diameter AE meeting BC at G,
DF = 1/2 AD, and CH = 1/3 CG, then rect. AF, BH equals the area of the pentagon.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0520_g2() -> Model:
    """Construct the figure 0520.g2 using geometor.model."""
    model = Model("0520.g2")

    # Circle centre D and inscribed regular pentagon vertices
    D = model.set_point(82.0, -88.0, classes=["given"], label="D")
    A = model.set_point(82.0, -22.0, classes=["given"], label="A")
    B = model.set_point(19.0, -68.0, classes=["given"], label="B")
    P1 = model.set_point(43.0, -141.0, classes=["auxiliary"], label="P1")
    P2 = model.set_point(121.0, -141.0, classes=["auxiliary"], label="P2")
    C = model.set_point(145.0, -68.0, classes=["given"], label="C")
    E = model.set_point(82.0, -154.0, classes=["given"], label="E")
    model.construct_circle(D, A)

    # Interior division points G, F (on AE) and H (on BC)
    G = model.set_point(82.0, -68.0, classes=["given"], label="G")
    F = model.set_point(82.0, -121.0, classes=["given"], label="F")
    H = model.set_point(125.0, -68.0, classes=["given"], label="H")

    # Polygons
    model.set_polygon([A, B, P1, P2, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, G])
    model.set_polygon([B, D, G])

    # Segments
    for p1, p2 in [
        (A, B), (B, P1), (P1, P2), (P2, C), (C, A),
        (A, E), (A, F), (A, D), (A, G),
        (G, D), (G, F), (G, E),
        (D, F), (D, E), (F, E),
        (B, C), (B, H), (B, G),
        (G, C), (G, H), (H, C),
        (B, D),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0520_g2()
