"""Programmatic construction for Book XII, Proposition 2 Commentary (0380.g1).

Square ABCD and regular octagon circumscribed about a circle with center O,
cutting off corner triangle AFG at tangent point E on arc HEK.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0380_g1() -> Model:
    """Construct the figure 0380.g1 using geometor.model."""
    model = Model("0380.g1")

    # Circle center O and circumscribed square ABCD (radius 63)
    O = model.set_point(89.0, -89.0, classes=["given"], label="O")
    A = model.set_point(26.0, -26.0, classes=["given"], label="A")
    B = model.set_point(26.0, -152.0, classes=["given"], label="B")
    C = model.set_point(152.0, -152.0, classes=["given"], label="C")
    D = model.set_point(152.0, -26.0, classes=["given"], label="D")

    # Contact points H (on AB), K (on AD), and E (on OA)
    K = model.set_point(89.0, -26.0, label="K")
    H = model.set_point(26.0, -89.0, label="H")
    E = model.set_point(44.45, -44.45, label="E")

    # Tangent FG at E meeting AH in F and AK in G
    G = model.set_point(62.90, -26.0, label="G")
    F = model.set_point(26.0, -62.90, label="F")

    # Symmetric octagon vertices on the other three corners
    G2 = model.set_point(115.10, -26.0, label="G2")
    F2 = model.set_point(152.0, -62.90, label="F2")
    F3 = model.set_point(152.0, -115.10, label="F3")
    G3 = model.set_point(115.10, -152.0, label="G3")
    G4 = model.set_point(62.90, -152.0, label="G4")
    F4 = model.set_point(26.0, -115.10, label="F4")

    # Circle
    model.construct_circle(O, K)

    # Segments
    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, A),
        (O, A), (O, E), (A, E),
        (A, K), (A, G), (G, K), (K, D),
        (A, H), (A, F), (F, H), (H, B),
        (F, G), (F, E), (E, G),
        (E, K), (E, H),
        (G2, F2), (F3, G3), (G4, F4),
    ]:
        model.set_segment(p1, p2)

    # Polygons and triangles
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, G, E])
    model.set_polygon([E, G, K])
    model.set_polygon([A, F, E])
    model.set_polygon([E, F, H])
    model.set_polygon([A, F, G])
    model.set_polygon([A, H, E, K])

    # Angles
    model.set_wedge(E, A, A, G)
    model.set_wedge(A, E, E, G)

    return model


if __name__ == "__main__":
    construct_0380_g1()
