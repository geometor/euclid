"""Programmatic construction for Book I, Proposition 28 note - Proclus Criteria (0324.g2)."""

from __future__ import annotations

from geometor.model import Model


def construct_0324_g2() -> Model:
    """Construct the figure for Proclus' criteria for parallelism (0324.g2)."""
    model = Model("0324.g2")

    A = model.set_point(15, -62.5, classes=["given"], label="A")
    B = model.set_point(147, -62.5, classes=["given"], label="B")
    C = model.set_point(15, -102, classes=["given"], label="C")
    D = model.set_point(147, -102, classes=["given"], label="D")
    E = model.set_point(90, -35, classes=["given"], label="E")
    F = model.set_point(60, -135, classes=["given"], label="F")
    G = model.set_point(82, -62.5, label="G")
    H = model.set_point(70, -102, label="H")

    model.construct_line(A, B)
    model.construct_line(C, D)
    model.construct_line(E, F)

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

    model.set_polygon([A, G, H, C])
    model.set_polygon([B, G, H, D])

    # All 8 angles at G and H
    model.set_wedge(G, E, E, A)
    model.set_wedge(G, E, E, B)
    model.set_wedge(G, A, A, H)
    model.set_wedge(G, B, B, H)
    model.set_wedge(H, G, G, C)
    model.set_wedge(H, G, G, D)
    model.set_wedge(H, C, C, F)
    model.set_wedge(H, D, D, F)

    return model


if __name__ == "__main__":
    construct_0324_g2()
