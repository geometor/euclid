"""Programmatic construction for Appendix I (Book XIV), Prop. 6 Alt. Proof (0521.g1).

Alternative proof of Prop. 6: in circle ABC with centre E, inscribed regular
pentagon with sides AB, AC and chord BC (meeting vertical diameter AF at K, with
KC = 3 CH), and inscribed equilateral triangle ADM (with chord DM perpendicular
to AF at G, where AE = 2 EG).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0521_g1() -> Model:
    """Construct the figure 0521.g1 using geometor.model."""
    model = Model("0521.g1")

    # Circle centre E and vertical diameter endpoints A, F
    E = model.set_point(84.0, -88.0, classes=["given"], label="E")
    A = model.set_point(84.0, -20.0, classes=["given"], label="A")
    F = model.set_point(84.0, -156.0, classes=["given"], label="F")
    model.construct_circle(E, A)

    # Inscribed regular pentagon vertices
    B = model.set_point(19.0, -67.0, classes=["given"], label="B")
    P1 = model.set_point(44.0, -143.0, classes=["auxiliary"], label="P1")
    P2 = model.set_point(124.0, -143.0, classes=["auxiliary"], label="P2")
    C = model.set_point(149.0, -67.0, classes=["given"], label="C")

    # Inscribed equilateral triangle ADM vertices D, M and midpoint G on AF
    G = model.set_point(84.0, -122.0, classes=["given"], label="G")
    D = model.set_point(25.1, -122.0, classes=["given"], label="D")
    M = model.set_point(142.9, -122.0, classes=["given"], label="M")

    # Intersection K of AF and BC, and division point H on KC (KC = 3 CH)
    K = model.set_point(84.0, -67.0, classes=["given"], label="K")
    H = model.set_point(127.0, -67.0, classes=["given"], label="H")

    # Polygons
    model.set_polygon([A, B, P1, P2, C])
    model.set_polygon([A, D, M])
    model.set_polygon([A, B, C])
    model.set_polygon([A, G, D])
    model.set_polygon([A, G, M])

    # Segments
    for p1, p2 in [
        (A, B), (B, P1), (P1, P2), (P2, C), (C, A),
        (A, F), (A, G), (A, E), (A, K),
        (K, E), (K, G), (K, F),
        (E, G), (E, F), (G, F),
        (B, C), (B, H), (B, K),
        (K, C), (K, H), (H, C),
        (D, M), (G, D), (G, M),
        (A, D), (A, M),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0521_g1()
