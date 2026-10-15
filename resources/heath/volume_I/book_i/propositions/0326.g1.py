"""Programmatic construction for Book I, Proposition 29 note - Playfair's Axiom (0326.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0326_g1() -> Model:
    """Construct the figure for the proof of I.29 by Playfair's Axiom (0326.g1)."""
    model = Model("0326.g1")

    A = model.set_point(18, -39.5, classes=["given"], label="A")
    B = model.set_point(172, -39.5, classes=["given"], label="B")
    C = model.set_point(18, -78, classes=["given"], label="C")
    D = model.set_point(172, -78, classes=["given"], label="D")
    E = model.set_point(72, -12, classes=["given"], label="E")
    F = model.set_point(132, -104, classes=["given"], label="F")
    G = model.set_point(89.5, -39.5, label="G")
    H = model.set_point(115, -78, label="H")
    K = model.set_point(15, -52, label="K")
    L = model.set_point(175, -26, label="L")

    model.construct_line(A, B)
    model.construct_line(C, D)
    model.construct_line(E, F)
    model.construct_line(K, L)

    model.set_segment(A, B)
    model.set_segment(A, G)
    model.set_segment(G, B)
    model.set_section([A, G, B])

    model.set_segment(C, D)
    model.set_segment(C, H)
    model.set_segment(H, D)
    model.set_section([C, H, D])

    model.set_segment(E, F)
    model.set_segment(E, G)
    model.set_segment(G, H)
    model.set_segment(H, F)
    model.set_section([E, G, H])
    model.set_section([G, H, F])

    model.set_segment(K, L)
    model.set_segment(K, G)
    model.set_segment(G, L)
    model.set_section([K, G, L])

    model.set_polygon([A, G, H, C])
    model.set_polygon([B, G, H, D])

    # Angles: < A G H ), < K G H ), < G H D )
    model.set_wedge(G, A, A, H)
    model.set_wedge(G, K, K, H)
    model.set_wedge(H, G, G, D)

    return model


if __name__ == "__main__":
    construct_0326_g1()
