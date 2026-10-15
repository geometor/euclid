"""Programmatic construction for Book X, Lemma to Proposition 54 (0119.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0119_g1() -> Model:
    """Construct the figure 0119.g1 using geometor.model."""
    model = Model("0119.g1")

    # Top row: K, G, C
    K = model.set_point(22.5, -19.0, label="K")
    G = model.set_point(88.5, -19.0, classes=["given"], label="G")
    C = model.set_point(126.5, -19.0, classes=["given"], label="C")

    # Middle row: D, B, E
    D = model.set_point(22.5, -58.0, classes=["given"], label="D")
    B = model.set_point(88.5, -58.0, classes=["given"], label="B")
    E = model.set_point(126.5, -58.0, classes=["given"], label="E")

    # Bottom row: A, F, H
    A = model.set_point(22.5, -125.0, classes=["given"], label="A")
    F = model.set_point(88.5, -125.0, classes=["given"], label="F")
    H = model.set_point(126.5, -125.0, label="H")

    # Base lines
    model.construct_line(K, C)
    model.construct_line(D, E)
    model.construct_line(A, H)
    model.construct_line(A, K)
    model.construct_line(F, G)
    model.construct_line(H, C)

    # Segments
    for p1, p2 in [
        (K, C), (K, G), (G, C),
        (D, E), (D, B), (B, E),
        (A, H), (A, F), (F, H),
        (A, K), (A, D), (D, K),
        (F, G), (F, B), (B, G),
        (H, C), (H, E), (E, C),
    ]:
        model.set_segment(p1, p2)

    # Collinear sections
    model.set_section([K, G, C])
    model.set_section([D, B, E])
    model.set_section([A, F, H])
    model.set_section([A, D, K])
    model.set_section([F, B, G])
    model.set_section([H, E, C])

    # Polygons (squares and rectangles)
    model.set_polygon([A, H, C, K])
    model.set_polygon([A, F, B, D])
    model.set_polygon([B, E, C, G])
    model.set_polygon([D, B, G, K])
    model.set_polygon([F, H, E, B])
    model.set_polygon([D, E, C, K])

    return model


if __name__ == "__main__":
    construct_0119_g1()
