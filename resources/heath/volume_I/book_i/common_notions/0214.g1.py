"""Programmatic construction for Book I, Postulate 4 Note — Proclus' Proof (0214.g1).

Proclus' proof that all right angles (ABC, DEF) are equal to one another, by
applying DE to AB with EF falling within ABC as BG, and producing CB to H and GB to K.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0214_g1() -> Model:
    """Construct the figure for 0214.g1 using geometor.model."""
    model = Model("0214.g1")

    # Left figure: right angle ABC with CB produced to H and GB produced to K
    A = model.set_point(74.0, -15.0, classes=["given"], label="A")
    B = model.set_point(74.0, -80.0, classes=["given"], label="B")
    C = model.set_point(145.0, -80.0, classes=["given"], label="C")
    H = model.set_point(15.0, -80.0, label="H")
    G = model.set_point(135.0, -58.0, label="G")
    K = model.set_point(15.0, -101.3, label="K")

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(B, H)
    model.set_segment(C, H)
    model.set_segment(B, G)
    model.set_segment(B, K)
    model.set_segment(G, K)
    model.set_section([C, B, H])
    model.set_section([G, B, K])

    # Right figure: right angle DEF
    D = model.set_point(195.0, -15.0, classes=["given"], label="D")
    E = model.set_point(195.0, -80.0, classes=["given"], label="E")
    F = model.set_point(270.0, -80.0, classes=["given"], label="F")

    model.set_segment(D, E)
    model.set_segment(E, F)

    return model


if __name__ == "__main__":
    construct_0214_g1()
