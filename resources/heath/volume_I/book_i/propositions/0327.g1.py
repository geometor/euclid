"""Programmatic construction for Book I, Proposition 29 note - Postulate 5 from Playfair (0327.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0327_g1() -> Model:
    """Construct the figure for proving Postulate 5 from Playfair's Axiom (0327.g1)."""
    model = Model("0327.g1")

    A = model.set_point(24, -38, classes=["given"], label="A")
    B = model.set_point(168, -17, classes=["given"], label="B")
    C = model.set_point(24, -76.5, classes=["given"], label="C")
    D = model.set_point(168, -76.5, classes=["given"], label="D")
    E = model.set_point(95.5, -27.5, label="E")
    F = model.set_point(112.5, -76.5, label="F")
    G = model.set_point(24, -27.5, label="G")
    H = model.set_point(168, -27.5, label="H")

    model.construct_line(A, B)
    model.construct_line(C, D)
    model.construct_line(G, H)
    model.construct_line(E, F)

    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_section([A, E, B])

    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_section([C, F, D])

    model.set_segment(G, H)
    model.set_segment(G, E)
    model.set_segment(E, H)
    model.set_section([G, E, H])

    model.set_segment(E, F)

    model.set_polygon([A, E, F, C])
    model.set_polygon([B, E, F, D])

    # Angles: < A E F ), < E F C ), < G E F ), < E F D ), < B E F )
    model.set_wedge(E, A, A, F)
    model.set_wedge(F, E, E, C)
    model.set_wedge(E, G, G, F)
    model.set_wedge(F, E, E, D)
    model.set_wedge(E, B, B, F)

    return model


if __name__ == "__main__":
    construct_0327_g1()
